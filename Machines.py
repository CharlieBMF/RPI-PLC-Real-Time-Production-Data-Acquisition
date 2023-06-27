import pymcprotocol
import time
import requests


def time_wrapper(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        if end-start > 1:
            print(f'Func {func.__name__} started: {start} finished: {end} Time: {end-start}')
        return result
    return wrap


class Machine:

    def __init__(self, id_line, id_machine, name, ip, port, endpoints, endpoints_data_values, endpoints_constant_data,
                 data_collection_signals_head, endpoints_constructors, target_network=None,
                 plc_id_in_target_network=None):
        self.id_line = id_line
        self.id_machine = id_machine
        self.name = name
        self.ip = ip
        self.port = port
        self.target_network = target_network
        self.plc_id_in_target_network = plc_id_in_target_network
        self.machine = self.define_machine_root()
        self.endpoints = endpoints
        self.endpoints_data_values = endpoints_data_values
        self.endpoints_constant_data = endpoints_constant_data
        self.endpoints_constructors = endpoints_constructors
        self.data_collection_signals_head = data_collection_signals_head

    def define_machine_root(self):
        pymc3e = pymcprotocol.Type3E()
        if self.target_network and self.plc_id_in_target_network:
            pymc3e.network = self.target_network
            pymc3e.pc = self.plc_id_in_target_network
        return pymc3e

    def connect(self):
        self.machine.connect(ip=self.ip, port=self.port)

    def close_connection(self):
        self.machine.close()

    def read_bits(self, head, size=1):
        return self.machine.batchread_bitunits(headdevice=head, readsize=size)

    def read_words(self, head, size=1):
        return self.machine.batchread_wordunits(headdevice=head, readsize=size)

    def read_random_words(self, word_devices=[], double_word_devices=[]):
        return self.machine.randomread(word_devices=word_devices, dword_devices=double_word_devices)

    def write_word(self, head, values):
        self.machine.batchwrite_wordunits(headdevice=head, values=values)

    def check_data_collection_status(self):
        plc_addresses_words = [self.endpoints_data_values[endpoint][data]['address']
                               for endpoint in self.endpoints
                               for data in self.endpoints_data_values[endpoint]
                               if self.endpoints_data_values[endpoint][data]['size'] != 2]
        plc_addresses_dwords = [self.endpoints_data_values[endpoint][data]['address']
                                for endpoint in self.endpoints
                                for data in self.endpoints_data_values[endpoint]
                                if self.endpoints_data_values[endpoint][data]['size'] == 2]

        plc_addresses_splitted_words, plc_addresses_splitted_dwords = [], []

        for address in plc_addresses_words:
            plc_addresses_splitted_words.extend(address)
        for address in plc_addresses_dwords:
            plc_addresses_splitted_dwords.extend(address)

        #print('[REQUEST] words addresses to read :', plc_addresses_splitted_words)
        #print('[REQUEST] dwords addresses to read :', plc_addresses_splitted_dwords)

        answer_keys_words, answer_keys_dwords = [], []
        for endpoint in self.endpoints:
            for data in self.endpoints_data_values[endpoint]:
                if self.endpoints_data_values[endpoint][data]['size'] != 2:
                    answer_keys_words.extend([endpoint + '|' + data]*self.endpoints_data_values[endpoint][data]['size'])
                else:
                    answer_keys_dwords.extend([endpoint + '|' + data])

        #print('[ANSWER] words addresses to read  :', answer_keys_words)
        #print('[ANSWER] dwords addresses to read  :', answer_keys_dwords)

        self.connect()
        answer_values_words, answer_values_dwords = \
            self.read_random_words(word_devices=plc_addresses_splitted_words,
                                   double_word_devices=plc_addresses_splitted_dwords)
        #self.write_word('D401', [0])
        self.close_connection()

        #print('[ANSWER] words values  :', answer_values_words)
        #print('[ANSWER] dwords values:', answer_values_dwords)
        address_values_zip = list(zip(answer_keys_words, answer_values_words)) +\
                             list(zip(answer_keys_dwords, answer_values_dwords))

        for address, value in address_values_zip:
            if address.endswith('OK Report Flag') or address.endswith('NG Report Flag'):
                trigger_status = value
                #print(trigger_status, type(trigger_status))
                if trigger_status > 0:
                #if True:
                    endpoint_name = address.split('|')[0]
                    address_values_for_endpoint = [element for element in address_values_zip
                                                   if element[0].startswith(endpoint_name)]
                    address_values_dict = {}
                    for (k, v) in address_values_for_endpoint:
                        if k not in address_values_dict.keys():
                            address_values_dict[k] = [v]
                        else:
                            address_values_dict[k] = address_values_dict[k] + [v]
                    data_values = {}

                    ## Construct data from plc as dict key:value final to json
                    for k, v in address_values_dict.items():
                        if len(v) > 1:
                            #print(v)
                            binary = [bin(b).replace('0b', '').zfill(16) for b in v]
                            halves_list = [half for word in binary for half in (word[len(word)//2:], word[:len(word) // 2])]
                            ascii_string = ''.join([chr(int(binary, 2)) for binary in halves_list])
                            #print(k, ascii_string)
                            data_values[k.split('|')[1]] = ascii_string.replace(' ', '').replace("\x00", '')
                        else:
                            data_values[k.split('|')[1]] = v[0]
                    print('data values', data_values)
                    json = {}

                    #data_values['OK Report Flag'] = 1

                    ## Construct final JSON
                    for production_data, v in data_values.items():
                        if production_data in self.endpoints_constructors[endpoint_name]['production_data']:
                            json[production_data] = v
                    if data_values['OK Report Flag'] == 1:
                        for constant_data in self.endpoints_constructors[endpoint_name]['constant_ok_part_data']:
                            json[constant_data] = self.endpoints_constant_data[endpoint_name]['constant_ok_part_data'][constant_data]
                    if data_values['NG Report Flag'] == 1:
                        for constant_data in self.endpoints_constructors[endpoint_name]['constant_ng_part_data']:
                            json[constant_data] = self.endpoints_constant_data[endpoint_name]['constant_ng_part_data'][constant_data]
                    print(['JSON'], k, json)

                    ## Report final JSON
                    u = self.endpoints_constructors[endpoint_name]['url']
                    print(u)
                    print(json)
                    response = requests.post(u, json=json)
                    print('Response text:', response.text)

                    self.connect()
                    self.write_word(self.data_collection_signals_head[k.split('|')[0]], [0, 0])
                    self.close_connection()

    def connection_data_display(self):
        print(
            '*'*20,
            f'\nLine: {self.id_line}\n'
            f'Machine: {self.id_machine}\n'
            f'Name: {self.name}\n'
            f'IP: {self.ip}\n'
            f'PORT: {self.port}\n'
            f'Target other network: {self.target_network}\n'
            f'PLC id in other network: {self.plc_id_in_target_network}\n'
        )


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
        self.plc_addresses_words = [self.endpoints_data_values[endpoint][data]['address']
                                    for endpoint in self.endpoints
                                    for data in self.endpoints_data_values[endpoint]
                                    if self.endpoints_data_values[endpoint][data]['size'] != 2]
        self.plc_addresses_dwords = [self.endpoints_data_values[endpoint][data]['address']
                                     for endpoint in self.endpoints
                                     for data in self.endpoints_data_values[endpoint]
                                     if self.endpoints_data_values[endpoint][data]['size'] == 2]
        self.plc_words_address_list = self.cumulate_words_addresses_into_list()
        self.plc_dwords_address_list = self.cumulate_dwords_addresses_into_list()
        self.words_keys, self.dwords_keys = self.generate_list_of_keys_for_address_lists()

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

    def cumulate_words_addresses_into_list(self):
        words_address_list = []
        for address in self.plc_addresses_words:
            words_address_list.extend(address)
        return words_address_list

    def cumulate_dwords_addresses_into_list(self):
        dwords_address_list = []
        for address in self.plc_addresses_dwords:
            dwords_address_list.extend(address)
        return dwords_address_list

    def generate_list_of_keys_for_address_lists(self):
        keys_words, keys_dwords = [], []
        for endpoint in self.endpoints:
            for data in self.endpoints_data_values[endpoint]:
                if self.endpoints_data_values[endpoint][data]['size'] != 2:
                    keys_words.extend([endpoint + '|' + data]*self.endpoints_data_values[endpoint][data]['size'])
                else:
                    keys_dwords.extend([endpoint + '|' + data])
        return keys_words, keys_dwords

    def read_data_from_plc(self):
        self.connect()
        answer_values_words, answer_values_dwords = \
            self.read_random_words(word_devices=self.plc_words_address_list,
                                   double_word_devices=self.plc_dwords_address_list)
        self.close_connection()
        return answer_values_words, answer_values_dwords

    def connect_keys_with_answer_values(self, answer_values_words, answer_values_dwords):
        address_values_zip = list(zip(self.words_keys, answer_values_words)) +\
                             list(zip(self.dwords_keys, answer_values_dwords))
        return address_values_zip

    @staticmethod
    def check_report_flags(value):
        trigger_status = value
        if trigger_status > 0:
            return True
        else:
            return False

    @staticmethod
    def create_keys_and_answers_dict(endpoint_name, keys_and_plc_values):
        address_values_for_endpoint = [element for element in keys_and_plc_values
                                       if element[0].startswith(endpoint_name)]
        address_values_dict = {}
        for (k, v) in address_values_for_endpoint:
            if k not in address_values_dict.keys():
                address_values_dict[k] = [v]
            else:
                address_values_dict[k] = address_values_dict[k] + [v]
        return address_values_dict

    def construct_json_from_plc_data(self, keys_answer_dict):
        data_values = {}
        for k, v in keys_answer_dict.items():
            if len(v) > 1:
                ascii_string = self.convert_decimal_from_plc_into_ascii_string(v)
                data_values[k.split('|')[1]] = ascii_string.replace(' ', '').replace("\x00", '')
            else:
                data_values[k.split('|')[1]] = v[0]
        return data_values

    @staticmethod
    def convert_decimal_from_plc_into_ascii_string(decimal_list):
        binary = [bin(b).replace('0b', '').zfill(16) for b in decimal_list]
        halves_list = [half for word in binary for half in (word[len(word) // 2:], word[:len(word) // 2])]
        ascii_string = ''.join([chr(int(binary, 2)) for binary in halves_list])
        return ascii_string

    def construct_final_json(self, endpoint_name, production_data_dict):
        final_json = {}
        for production_data, v in production_data_dict.items():
            if production_data in self.endpoints_constructors[endpoint_name]['production_data']:
                final_json[production_data] = v
        if production_data_dict['OK Report Flag'] == 1:
            for constant_data in self.endpoints_constructors[endpoint_name]['constant_ok_part_data']:
                final_json[constant_data] = self.endpoints_constant_data[endpoint_name]['constant_ok_part_data'][
                    constant_data]
        if production_data_dict['NG Report Flag'] == 1:
            for constant_data in self.endpoints_constructors[endpoint_name]['constant_ng_part_data']:
                final_json[constant_data] = self.endpoints_constant_data[endpoint_name]['constant_ng_part_data'][
                    constant_data]
                ### TUTAJ DOPISAC ZE BRAC TEZ DANE Z NG REASON (ID) Z PRODUCTION DATA #if NG REASON ID IN PRODUCTION DATA
                ### TUTAJ DOPISAC ZE ZEROWAC ID REASON Z (ID) Z PRODUCTION DATA TEN ADRES W PLC
        return final_json

    def report_data_to_api(self, endpoint_name, final_json):
        url = self.endpoints_constructors[endpoint_name]['url']
        print(url)
        print(final_json)
        response = requests.post(url, json=final_json)
        print('Response text:', response.text)

    def report_collection_data_completion_in_plc(self, endpointname):
        self.connect()
        self.write_word(self.data_collection_signals_head[endpointname], [0, 0])
        self.close_connection()

    def check_data_collection_status(self):
        self.connect()
        answer_values_words, answer_values_dwords = \
            self.read_random_words(word_devices=self.plc_words_address_list,
                                   double_word_devices=self.plc_dwords_address_list)
        self.close_connection()

        #print('[ANSWER] words values  :', answer_values_words)
        #print('[ANSWER] dwords values:', answer_values_dwords)
        address_values_zip = list(zip(self.words_keys, answer_values_words)) +\
                             list(zip(self.dwords_keys, answer_values_dwords))

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


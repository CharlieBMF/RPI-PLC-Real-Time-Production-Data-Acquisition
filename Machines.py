"""
Real Time Data collection from production line. Contains all the methods necessary to collect data.
"""

import pymcprotocol
import time
import requests


def time_wrapper(func):
    """
    Wrapper for showing function name and execution time.
    For debugging & controll
    :param func: any function
    :return: wrapped function
    """

    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        if end - start > 1:
            print(f'Func {func.__name__} started: {start} finished: {end} Time: {end - start}')
        return result

    return wrap


class Machine:
    """Class representing one Machine on the line"""

    def __init__(self, id_line, id_machine, name, ip, port, endpoints, endpoints_data_values, endpoints_constant_data,
                 data_collection_signals_head, endpoints_constructors, target_network=None,
                 plc_id_in_target_network=None):
        """
        Init for class
        :param id_line: id of a production line
        :param id_machine: id of a machine
        :param name: name of the machine
        :param ip: IP address to connect to machine
        :param port: open port for communication between the RaspberryPi and the machine
        :param endpoints: list of a reporting endpoint on machine
        :param endpoints_data_values: dict of names & specification of production data for each endpoint
        :param endpoints_constant_data: constant data which should be added during reporting to API for each endpoint
        depends on the OK or NG status. Include Result, Seriese, NG Count
        :param data_collection_signals_head: head of addresses in PLC which is controlled also by the script during
        exchanging data. Contains address for OK, NG and NG id. These addresses are reset by script after proper data
        collection
        :param endpoints_constructors: constructor which contains dictionary of data which should be included during
        construction of json to API
        :param target_network:it is possible to communicate using other communication protocols to other machines
         on the line. If the RPI to PLC, it is possible to perform routing on the PLC for a different network number
          and communicate with another PLC. This number determines to which network number routing should be performed
        :param plc_id_in_target_network: id of the PLC on routed network
        """
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
        """
        PLC controller connection object definition
        :return: connection pymcprotocol object
        """
        pymc3e = pymcprotocol.Type3E()
        if self.target_network and self.plc_id_in_target_network:
            pymc3e.network = self.target_network
            pymc3e.pc = self.plc_id_in_target_network
        return pymc3e

    def connect(self):
        """
        Establish connection with PLC
        :return:
        """
        self.machine.connect(ip=self.ip, port=self.port)

    def close_connection(self):
        """
        Closing connection with PLC
        :return:
        """
        self.machine.close()

    def read_bits(self, head, size=1):
        """
        Reading bits from PLC in order
        :param head: initial bit address
        :param size: number of consecutive bits to read
        :return: list with bit values
        """
        return self.machine.batchread_bitunits(headdevice=head, readsize=size)

    def read_words(self, head, size=1):
        """
        Reading words from PLC in order
        :param head: initial word address
        :param size: number of consecutive words to read
        :return: list with words values
        """
        return self.machine.batchread_wordunits(headdevice=head, readsize=size)

    def read_random_words(self, word_devices, double_word_devices):
        """
        Reading words from PLC not in order
        :param word_devices: list of words to read
        :param double_word_devices: list of dwords to read
        :return: list of words/dwords values
        """
        return self.machine.randomread(word_devices=word_devices, dword_devices=double_word_devices)

    def write_word(self, head, values):
        """
        Writing words to PLC
        :param head: starting register in PLC
        :param values: list of values which should be sent to the PLC starts from head number, each parameter of list
        for one register in PLC
        :return:
        """
        self.machine.batchwrite_wordunits(headdevice=head, values=values)

    def cumulate_words_addresses_into_list(self):
        """
        Creates a list of word addresses which should be read from PLC. 
        :return: list of word addresses
        """
        words_address_list = []
        for address in self.plc_addresses_words:
            words_address_list.extend(address)
        return words_address_list

    def cumulate_dwords_addresses_into_list(self):
        """
        Creates a list of dwords addresses which should be read from PLC.
        :return: list of dword addresses
        """
        dwords_address_list = []
        for address in self.plc_addresses_dwords:
            dwords_address_list.extend(address)
        return dwords_address_list

    def generate_list_of_keys_for_address_lists(self):
        """
        Create two lists of words and dwords variable names which should be read from PLC. Additionally the name of the
        value in list starts with the name of endpoint like [Marking|2D_Code, Marking|Length, Weld|2D_Code]
        :return: list of word addresses, list of dword addresses
        """
        keys_words, keys_dwords = [], []
        for endpoint in self.endpoints:
            for data in self.endpoints_data_values[endpoint]:
                if self.endpoints_data_values[endpoint][data]['size'] != 2:
                    keys_words.extend([endpoint + '|' + data] * self.endpoints_data_values[endpoint][data]['size'])
                else:
                    keys_dwords.extend([endpoint + '|' + data])
        return keys_words, keys_dwords

    def read_data_from_plc(self):
        """
        Connects with machine, reads words and dwords according to list of words and dwords created in
        cumulate_words_addresses_into list and cumulate_dwords_addresses_into_list, close connection
        :return: list of values in PLC words, list of values in PLC dwords
        """
        self.connect()
        answer_values_words, answer_values_dwords = \
            self.read_random_words(word_devices=self.plc_words_address_list,
                                   double_word_devices=self.plc_dwords_address_list)
        self.close_connection()
        return answer_values_words, answer_values_dwords

    def connect_keys_with_answer_values(self, answer_values_words, answer_values_dwords):
        """
        Creates a list which contains a zip of answer values from PLC (from read_data_from_plc method) and
        names of the value for words and dwords (from generate_list_of_keys_from_address_lists)
        :param answer_values_words: answer values from PLC for read words
        :param answer_values_dwords: answer values from PLC for read dwords
        :return: list of values from PLC and names for this value
        """
        address_values_zip = list(zip(self.words_keys, answer_values_words)) + \
                             list(zip(self.dwords_keys, answer_values_dwords))
        return address_values_zip

    def construct_json_from_plc_data(self, keys_answer_dict):
        """
        Constructs the json from production data acquired from PLC. If the length of list of value is bigger than 1
        means that it is ascii code so the value is converted from decimal into ascii code with additional method
        :param keys_answer_dict: dict of keys and values read from plc 
        :return: prepared json with production data for each endpoint
        """
        data_values = {}
        for k, v in keys_answer_dict.items():
            if len(v) > 1:
                ascii_string = self.convert_decimal_from_plc_into_ascii_string(v)
                data_values[k.split('|')[1]] = ascii_string.replace(' ', '').replace("\x00", '').replace("\r", '')
            else:
                data_values[k.split('|')[1]] = v[0]
        return data_values

    def construct_final_json(self, endpoint_name, production_data_dict):
        """
        Constructs the final json contains: 
        1. Production data
        2. Constant data which depends on the status of piece (OK/NG)
        3. NG reason id if it is NG piece
        If it is NG piece the NG reason id register is cleaned in the PLC by additional method 
        :param endpoint_name: the name of the endpoint for json
        :param production_data_dict: production data json 
        :return: full json contains all data required for each endpoint
        """
        final_json = {}
        for production_data, v in production_data_dict.items():
            if production_data in self.endpoints_constructors[endpoint_name]['production_data']:
                final_json[production_data] = v
        if production_data_dict['OK Report Flag'] == 1:
            for constant_data in self.endpoints_constructors[endpoint_name]['constant_ok_part_data']:
                final_json[constant_data] = self.endpoints_constant_data[endpoint_name]['constant_ok_part_data'][
                    constant_data]
                final_json['Ng Reason (Id)'] = 0
        if production_data_dict['NG Report Flag'] == 1:
            for constant_data in self.endpoints_constructors[endpoint_name]['constant_ng_part_data']:
                final_json[constant_data] = self.endpoints_constant_data[endpoint_name]['constant_ng_part_data'][
                    constant_data]
            if 'Ng Reason (Id)' in self.endpoints_constructors[endpoint_name]['production_data']:
                final_json['Ng Reason (Id)'] = production_data_dict['Ng Reason (Id)']
                self.clean_ng_reason_in_plc_register(endpoint_name)
        return final_json

    def report_data_to_api(self, endpoint_name, final_json):
        """
        Sends the data to the api
        :param endpoint_name: name of the endpoint
        :param final_json: full json required by the api
        :return: 
        """
        url = self.endpoints_constructors[endpoint_name]['url']
        print(url)
        print(final_json)
        response = requests.post(url, json=final_json)
        print('Response text:', response.text)

    def report_collection_data_completion_in_plc(self, endpointname):
        """
        Opens connection, reset data collection signals in the PLC if data is properly send to the API, close connection
        :param endpointname: endpoint name
        :return: 
        """
        self.connect()
        self.write_word(self.data_collection_signals_head[endpointname]['data collection'], [0, 0])
        self.close_connection()

    def clean_ng_reason_in_plc_register(self, endpointname):
        """
        Opens connection, clean ng reason id register in the plc, close connection
        :param endpointname: 
        :return: 
        """
        self.connect()
        self.write_word(self.data_collection_signals_head[endpointname]['Ng Reason (Id)'], [0])
        print('Cleaning...', self.data_collection_signals_head[endpointname]['Ng Reason (Id)'])
        self.close_connection()

    def connection_data_display(self):
        """
        Displays a data of the machine and connection
        :return: 
        """
        print(
            '*' * 20,
            f'\nLine: {self.id_line}\n'
            f'Machine: {self.id_machine}\n'
            f'Name: {self.name}\n'
            f'IP: {self.ip}\n'
            f'PORT: {self.port}\n'
            f'Target other network: {self.target_network}\n'
            f'PLC id in other network: {self.plc_id_in_target_network}\n'
        )

    @staticmethod
    def check_report_flags(value):
        """
        Checks trigger status for data collection in PLC
        :param value: value of trigger
        :return: T/F depends on the status
        """
        trigger_status = value
        if trigger_status > 0:
            return True
        else:
            return False

    @staticmethod
    def create_keys_and_answers_dict(endpoint_name, keys_and_plc_values):
        """
        Creates a dictionary for the name of values and value from the plc like {name_of_value: [v1, (..)]}. The length
        of a list depends on the length of a value configured in conf.py file
        :param endpoint_name: the name of the endpoint for the data
        :param keys_and_plc_values: list of the names and values from PLC
        :return: dictionary of names and values
        """
        address_values_for_endpoint = [element for element in keys_and_plc_values
                                       if element[0].startswith(endpoint_name)]
        address_values_dict = {}
        for (k, v) in address_values_for_endpoint:
            if k not in address_values_dict.keys():
                address_values_dict[k] = [v]
            else:
                address_values_dict[k] = address_values_dict[k] + [v]
        return address_values_dict

    @staticmethod
    def convert_decimal_from_plc_into_ascii_string(decimal_list):
        """
        Converts list of decimal values into ascii code
        :param decimal_list: list of decimal values
        :return: ascii code
        """
        binary = [bin(b).replace('0b', '').zfill(16) for b in decimal_list]
        halves_list = [half for word in binary for half in (word[len(word) // 2:], word[:len(word) // 2])]
        ascii_string = ''.join([chr(int(binary, 2)) for binary in halves_list])
        return ascii_string

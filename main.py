#!/usr/bin/python

from Machines import Machine
from conf import machines_names
import time


def create_machine_classes():
    list_of_machines = []
    for k, v in machines_names.items():
        k = Machine(id_line=v['id_line'], id_machine=v['id_machine'], name=v['name'], ip=v['ip'], port=v['port'],
                    endpoints=v['endpoints'],
                    endpoints_data_values=v['endpoints_data_values'],
                    endpoints_constant_data=v['endpoints_constant_data'],
                    endpoints_constructors=v['endpoints_constructors'],
                    data_collection_signals_head=v['data_collection_signals_head'],
                    )
        list_of_machines.append(k)
    return list_of_machines


list_of_machine_classes = create_machine_classes()
while True:
    starto = time.time()
    for machine_class in list_of_machine_classes:
        try:
            plc_words_values, plc_dwords_values = machine_class.read_data_from_plc()
        except:
            continue
        else:
            keys_and_plc_values = machine_class.connect_keys_with_answer_values(plc_words_values, plc_dwords_values)
            for address, value in keys_and_plc_values:
                if address.endswith('OK Report Flag') or address.endswith('NG Report Flag'):
                    if machine_class.check_report_flags(value):
                        endpoint_name = address.split('|')[0]
                        keys_answer_dict = machine_class.create_keys_and_answers_dict(endpoint_name, keys_and_plc_values)
                        production_data_dict = machine_class.construct_json_from_plc_data(keys_answer_dict)
                        final_json = machine_class.construct_final_json(endpoint_name, production_data_dict)
                        machine_class.report_data_to_api(endpoint_name, final_json)
                        machine_class.report_collection_data_completion_in_plc(endpoint_name)
    endo = time.time()
    print(f'Full line loop time: {endo-starto}')
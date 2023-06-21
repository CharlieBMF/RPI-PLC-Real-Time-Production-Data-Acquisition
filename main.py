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
                    )
        list_of_machines.append(k)
    return list_of_machines


list_of_machine_classes = create_machine_classes()

starto = time.time()
for i in range(0, 150):

    for machine_class in list_of_machine_classes:
        machine_class.check_data_collection_status()

endo = time.time()
print(f'Full scan time: {endo-starto}')


##################################### ASYNCIO
# async def communication_open(machine_class):
#     await machine_class.connect()
#     #await asyncio.sleep(0)
#
#
# async def communication_close(machine_class):
#     await machine_class.close_connection()
#     #await asyncio.sleep(0)
#
#
#
#
# async def main():
#     starto = time.time()
#     # c_open = [asyncio.create_task(communication_open(i)) for i in list_of_machine_classes]
#     # c_close = [asyncio.create_task(communication_close(i)) for i in list_of_machine_classes]
#     for i in range(0, 15):
#         s = time.time()
#
#         await asyncio.gather(communication_open(list_of_machine_classes[1]),
#                              communication_open(list_of_machine_classes[2]),
#                              communication_open(list_of_machine_classes[3]))
#         await asyncio.gather(communication_close(list_of_machine_classes[1]),
#                              communication_close(list_of_machine_classes[2]),
#                              communication_close(list_of_machine_classes[3]),
#                              )
#         print(f'Loop scan time: {time.time() - s}')
#     endo = time.time()
#     print(f'Full scan time: {endo-starto}')
#
# asyncio.run(main())


##################################### MULTIPROCESSING
# import asyncio
# from multiprocessing import Process, Lock
# from multiprocessing.managers import BaseManager
#
#
# class MyManager(BaseManager):
#     pass
#
#
# MyManager.register('klasa_maszyn', Machine)
#
# manager = MyManager()
# manager.start()
# f1 = manager.klasa_maszyn(id_line=machines_names['F01']['id_line'], id_machine=machines_names['F01']['id_machine'], name=machines_names['F01']['name'], ip=machines_names['F01']['ip'], port=machines_names['F01']['port'], master_on_address=machines_names['F01']['address']['master_on_address'], machine_status_address=machines_names['F01']['address']['machine_status_address'], mct_address=machines_names['F01']['address']['mct_address'])
# f2 = manager.klasa_maszyn(id_line=machines_names['F02']['id_line'], id_machine=machines_names['F02']['id_machine'], name=machines_names['F02']['name'], ip=machines_names['F02']['ip'], port=machines_names['F02']['port'], master_on_address=machines_names['F02']['address']['master_on_address'], machine_status_address=machines_names['F02']['address']['machine_status_address'], mct_address=machines_names['F02']['address']['mct_address'])
# f3 = manager.klasa_maszyn(id_line=machines_names['F03']['id_line'], id_machine=machines_names['F03']['id_machine'], name=machines_names['F03']['name'], ip=machines_names['F03']['ip'], port=machines_names['F03']['port'], master_on_address=machines_names['F03']['address']['master_on_address'], machine_status_address=machines_names['F03']['address']['machine_status_address'], mct_address=machines_names['F03']['address']['mct_address'])
# f4 = manager.klasa_maszyn(id_line=machines_names['F04']['id_line'], id_machine=machines_names['F04']['id_machine'], name=machines_names['F04']['name'], ip=machines_names['F04']['ip'], port=machines_names['F04']['port'], master_on_address=machines_names['F04']['address']['master_on_address'], machine_status_address=machines_names['F04']['address']['machine_status_address'], mct_address=machines_names['F04']['address']['mct_address'])
# f5 = manager.klasa_maszyn(id_line=machines_names['F05']['id_line'], id_machine=machines_names['F05']['id_machine'], name=machines_names['F05']['name'], ip=machines_names['F05']['ip'], port=machines_names['F05']['port'], master_on_address=machines_names['F05']['address']['master_on_address'], machine_status_address=machines_names['F05']['address']['machine_status_address'], mct_address=machines_names['F05']['address']['mct_address'])
# f6 = manager.klasa_maszyn(id_line=machines_names['F06']['id_line'], id_machine=machines_names['F06']['id_machine'], name=machines_names['F06']['name'], ip=machines_names['F06']['ip'], port=machines_names['F06']['port'], master_on_address=machines_names['F06']['address']['master_on_address'], machine_status_address=machines_names['F06']['address']['machine_status_address'], mct_address=machines_names['F06']['address']['mct_address'])
# f7 = manager.klasa_maszyn(id_line=machines_names['F07']['id_line'], id_machine=machines_names['F07']['id_machine'], name=machines_names['F07']['name'], ip=machines_names['F07']['ip'], port=machines_names['F07']['port'], master_on_address=machines_names['F07']['address']['master_on_address'], machine_status_address=machines_names['F07']['address']['machine_status_address'], mct_address=machines_names['F07']['address']['mct_address'])
# f8 = manager.klasa_maszyn(id_line=machines_names['F08']['id_line'], id_machine=machines_names['F08']['id_machine'], name=machines_names['F08']['name'], ip=machines_names['F08']['ip'], port=machines_names['F08']['port'], master_on_address=machines_names['F08']['address']['master_on_address'], machine_status_address=machines_names['F08']['address']['machine_status_address'], mct_address=machines_names['F08']['address']['mct_address'])
#
# list_of_machine_classes = [f1, f2, f3, f4]
#
# starto = time.time()
# for i in range(0, 150):
#     s = time.time()
#     p_open = [Process(target=target.connect) for target in list_of_machine_classes]
#     p_close = [Process(target=target.close_connection) for target in list_of_machine_classes]
#     for p in p_open:
#         p.start()
#     for p in p_open:
#         p.join()
#     for p in p_close:
#         p.start()
#     for p in p_close:
#         p.join()
#
# print(f'Full scan time: {time.time() - starto}')
# RPI-PLC-Real-Time-Production-Data-Acquisition
Script allowing to acquire real time data from Mitsubishi PLC on production line. Acquired data is being sent to API.

# Hardware

1) RaspberryPi4 4GB

![image](https://github.com/CharlieBMF/RPI-PLC-Real-Time-Production-Data-Acquisition/assets/109242797/77af1f65-03b1-4570-8cf1-aad30f068c34)

2) Mitsubishi PLC Q Series (possible to use different type)

![image](https://github.com/CharlieBMF/RPI-PLC-Real-Time-Production-Data-Acquisition/assets/109242797/90649183-77d0-464e-8278-05d2d856b687)

# Topology

It is necessary to connect all PLC CPU's by ETH in one network. RPI script has access to connect with each PLC. 

![image](https://github.com/CharlieBMF/RPI-PLC-Real-Time-Production-Data-Acquisition/assets/109242797/f12275a5-c30a-4335-a190-a75aca4f8a24)

# General description 

The software has been divided into 3 main scripts:
<ol>
  <li> Conf.py - defines each PLC's address, connection, endpoint, data to acquire </li>
  <li> Machines.py - defines class for each machine (PLC) with necessary methods </li>
  <li> main.py - main loop script </li>
</ol>

# conf.py

''' python 
    'F07':
        {
            'id_line': 32,
            'id_machine': 267,
            'name': 'COOL',
            'ip': '192.168.1.216',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'endpoints': ['SC_Charge'],
            'endpoints_data_values':
                {
                    'SC_Charge':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D401'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D402'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'Barcode':
                                {
                                    'address': ['W1540', 'W1541', 'W1542', 'W1543', 'W1544', 'W1545'],
                                    'type': 'ascii',
                                    'size': 6
                                },
                            'Offset (mm)':
                                {
                                    'address': ['W1550'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'Height (mm)':
                                {
                                    'address': ['W1551'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'S-Clip Lot':
                                {
                                    'address': ['W1560', 'W1561', 'W1562', 'W1563', 'W1564', 'W1565', 'W1566', 'W1567'],
                                    'type': 'ascii',
                                    'size': 8
                                },
                            'S-Clip No':
                                {
                                    'address': ['W1568', 'W1569', 'W156A', 'W156B', 'W156C', 'W156D', 'W156E', 'W156F'],
                                    'type': 'ascii',
                                    'size': 8
                                },
                            'Ng Reason (Id)':
                                {
                                    'address': ['D421'],
                                    'type': int,
                                    'size': 1,
                                },
                        },
                },
            'endpoints_constant_data':
                {
                    'SC_Charge':
                        {
                            'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                },
            'endpoints_constructors':
                {
                    'SC_Charge':
                        {
                            'production_data': ['Barcode', 'Offset (mm)', 'Height (mm)', 'S-Clip Lot', 'S-Clip No',
                                                'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/ShortingClip',
                        },
                },
            'data_collection_signals_head':
                {
                    'SC_Charge': {'data collection': 'D401', 'Ng Reason (Id)': 'D421'},
                },
        },    
        '''

# main.py

When the software starts, machine classes are created according to the machines defined in conf.py.



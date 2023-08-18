# RPI-PLC-Real-Time-Production-Data-Acquisition
Software used to read production data in real time from machines on the line. These data are sent to mssql using API, and then it is possible to analyze them, implement AI solutions, or visualize them on dashboards. The software is based on communication frames with mitsbushisi PLC controllers. It is possible to use any model (in this case, the Q series was used). The software located on the RPI microcomputer reads the data defined in the conf file from the appropriate machine using the communication frame. Then the received response is analyzed. If the appropriate flag about the report of a new item appears, further analysis of the response takes place - the data is read and placed in the corresponding table (depends on machine) in mssql with the appropriate information whether it is an item finished ok, ng or in production. Everything is done in real time with a full readout of all machines in the line taking 0.05s

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

  ```python
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
  ```

```
'id_line': id of line used to define in sql,
'id_machine': id of machine used to define in sql,
'name': name of the machine for display,
'ip': IP address of machine PLC,
'port': port used to connect to PLC,
'target_network': it is possible to use ETH connecting to one point and then change network to fiber to connect to other point, this is the number of fiber network configured in PLC None if not used
'plc_id_in_target_network': id number of PLC in fiber network, None if not used
'endpoints': list of endpoints which triggers production data acquisition, it is possible to use several endpoints on one machine, when one machine reports production data in several places
'endpoints_data_values': a dictionary defining what production data are read in individual endpoints
    {
        'SC_Charge':
            {
                'OK Report Flag': flag lights up in case of piece OK, mandatory for each endpoint
                    {
                        'address': the address of the register in the PLC that is assigned to the value
                        'type': variable type
                        'size': length of consecutive registers necessary to read
                    },
                'NG Report Flag': flag lights up in case of piece NG, mandatory for each endpoint
                    {
                        'address': the address of the register in the PLC that is assigned to the value
                        'type': variable type
                        'size': length of consecutive registers necessary to read
                    },
                'Barcode': one point production data in this example containing the barcode of a given piece
                    {
                        'address': list of addresses in plc containing a specific production data
                        'type': variable type
                        'size': length of consecutive registers necessary to read
                    },

            },
    },
'endpoints_constant_data': each point of the data report additionally contains constant data, here the values ​​and type of constant data for a given endpoint are specified
    {
        'SC_Charge': iven endpoint
            {
                'constant_ok_part_data': constant values ​​for OK elements
                'constant_ng_part_data': constant values ​​for NG elements
            },
    },
'endpoints_constructors': here the appearance of the final json is defined, which of all possible production data should be included in the final json sent to the API, and which constant data
    {
        'SC_Charge': given endpoint
            {
                'production_data': production data whose addresses and type are defined in endpoint_data_values,
                'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                'url': API address,
            },
    },
'data_collection_signals_head': addresses of additional markers used in the script, but not production data
    {
        'SC_Charge': {'data collection': signal of the need to download production data, 'Ng Reason (Id)': when an NG piece occurs, a given error occurs on the machine, it is read for later AI analysis of the reasons for the occurrence of specific production data},
    },
},
```

# main.py

When the software starts, machine classes are created according to the machines defined in conf.py.

``` python
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
```
In the main loop of the program, each of the machines included in the production line is read. If the response from the PLC for the signals OK Report Flag or NG Report Flag is considered to be one, the data is downloaded, processed into appropriate types, json is created in accordance with the data from conf, and then sent to the api.


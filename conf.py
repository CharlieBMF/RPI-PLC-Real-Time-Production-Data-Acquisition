machines_names = {
    'F01':
        {
            'id_line': 32,
            'id_machine': 233,
            'name': 'Welding & 2D Marking',
            'ip': '192.168.1.222',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'address':
                {
                    'master_on_address': 'M6',
                    'machine_status_address': 'M44',
                    'mct_address': 'D50080',
                },
            'endpoints': ['2D_Mark', 'Press_Fit', 'Weld', 'Brush'],
            'endpoints_data_values':
                {
                    '2D_Mark':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['M301'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M302'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W140', 'W141', 'W142', 'W143', 'W144', 'W145'],
                                    'type': 'ascii',
                                    'size': 6
                                },
                            'Bottle Lot':
                                {
                                    'address': ['W150', 'W151', 'W152', 'W153', 'W154', 'W155', 'W156', 'W157'],
                                    'type': 'ascii',
                                    'size': 8
                                },
                            'Bottle No':
                                {
                                    'address': ['W158', 'W159', 'W15A', 'W15B', 'W15C', 'W15D', 'W15E', 'W15F'],
                                    'type': 'ascii',
                                    'size': 8
                                },
                            'Bottle Length (mm)':
                                {
                                    'address': ['W160'],
                                    'type': 'int',
                                    'size': 1
                                },
                            # 'Ng Reason (Id)': 'XXXXX',

                        },
                    'Press_Fit':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['M321'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M322'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W170', 'W171', 'W172', 'W173', 'W174', 'W175'],
                                    'type': 'ascii',
                                    'size': 6
                                },
                            'Diffuser Lot':
                                {
                                    'address': ['W180', 'W181', 'W182', 'W183', 'W184', 'W185', 'W186', 'W187'],
                                    'type': 'ascii',
                                    'size': 8
                                },
                            'Diffuser No':
                                {
                                    'address': ['W188', 'W189', 'W18A', 'W18B', 'W18C', 'W18D', 'W18E', 'W18F'],
                                    'type': 'ascii',
                                    'size': 8
                                },
                            'DF Press Height (mm)':
                                {
                                    'address': ['W178'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'DF Force (kN)':
                                {
                                    'address': ['W17A'],
                                    'type': 'int',
                                    'size': 1
                                 },
                            # 'Ng Reason (Id)': 'XXXXX',

                        },
                    'Weld':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['M341'],
                                    'type': 'bit',
                                    'size': 1
                                 },
                            'NG Report Flag':
                                {
                                    'address': ['M342'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W1A0', 'W1A1', 'W1A2', 'W1A3', 'W1A4', 'W1A5'],
                                    'type': 'ascii',
                                    'size': 6
                                },
                            'Program No':
                                {
                                    'address': ['W1B0'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'Output (kW)':
                                {'address': ['W1B1'],
                                 'type': 'int',
                                 'size': 1
                                 },
                            'Runout (mm)':
                                {
                                    'address': ['W1B2'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'Point X':
                                {
                                    'address': ['W1B3'],
                                    'type': 'int',
                                    'size': 2
                                },
                            'Point Y':
                                {
                                    'address': ['W1B5'],
                                    'type': 'int',
                                    'size': 2
                                },
                            'Point @':
                                {
                                    'address': ['W1B7'],
                                    'type': 'int',
                                    'size': 2
                                },
                            # 'Ng Reason (Id)': 'XXXXX',

                        },
                    'Brush':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['M361'],
                                    'type': 'bit',
                                    'size': 1
                                 },
                            'NG Report Flag':
                                {
                                    'address': ['M362'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W1D0', 'W1D1', 'W1D2', 'W1D3', 'W1D4', 'W1D5'],
                                    'type': 'ascii',
                                    'size': 6
                                },
                            # 'Ng Reason (Id)': 'XXXXX',

                        },
                },
            'endpoints_constant_data':
                {
                    '2D_Mark':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Press_Fit':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Weld':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Brush':
                        {
                            'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                },
            'endpoints_constructors':
                {
                    '2D_Mark':
                        {
                            'production_data': ['2D Code', 'Bottle Lot', 'Bottle No', 'Bottle Length (mm)',
                                                'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/Marking2D',
                        },
                    'Press_Fit':
                        {
                            'production_data': ['2D Code', 'Diffuser Lot', 'Diffuser No', 'DF Press Height (mm)',
                                                'DF Force (kN)', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/Marking2D',
                        },
                    'Weld':
                        {
                            'production_data': ['2D Code', 'Program No', 'Output (kW)', 'Runout (mm)', 'Point X',
                                                'Point Y', 'Point @', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/Marking2D',
                        },
                    'Brush':
                        {
                            'production_data': ['2D Code', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/Marking2D',
                        },
                },
         },
    # 'F02':
    #     {
    #         'id_line': 32,
    #         'id_machine': 234,
    #         'name': 'Stud Bolt',
    #         'ip': '192.168.1.221',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'address':
    #             {
    #                 'master_on_address': 'M6',
    #                 'machine_status_address': 'M44',
    #                 'mct_address': 'D50080',
    #             },
    #         'production_data':
    #             {
    #                 'Weld':
    #                     {
    #                         'Data Collection Flag': 'M300',
    #                         'OK Report Flag': 'M301',
    #                         'NG Report Flag': 'M302',
    #                         'Jig No 1 Flag': 'M8611',
    #                         'Jig No 2 Flag': 'M8610',
    #                         '2D Code': 'W340',
    #                         'Bolt lot': 'W370',
    #                         'Bolt No': 'W378',
    #                         'Jig (weld)': 'W380',
    #                         '(1st side) Pilot Volt (V)': 'W350',
    #                         '(1st side) Weld Volt (V)': 'W351',
    #                         '(1st side) Weld Current (A)': 'W352',
    #                         '(1st side) Weld Cycle (ms)': 'W353',
    #                         '(1st side) Weld Depth (mm)': 'W354',
    #                         '(1st side) Weld Energy (J)': 'W355',
    #                         '(1st side) Lift (mm)': 'W356',
    #                         '(1st side) Ta (ms)': 'W357',
    #                         '(2nd side) Pilot Volt (V)': 'W360',
    #                         '(2nd side) Weld Volt (V)': 'W361',
    #                         '(2nd side) Weld Current (A)': 'W362',
    #                         '(2nd side) Weld Cycle (ms)': 'W363',
    #                         '(2nd side) Weld Depth (mm)': 'W364',
    #                         '(2nd side) Weld Energy (J)': 'W365',
    #                         '(2nd side) Lift (mm)': 'W366',
    #                         '(2nd side) Ta (ms)': 'W367',
    #                     },
    #                 'Brush':
    #                     {
    #                         'Data Collection Flag': 'M320',
    #                         'OK Report Flag': 'M321',
    #                         'NG Report Flag': 'M322',
    #                         '2D Code': 'W390',
    #                         'Jig (brush)': 'W3A0',
    #                     },
    #
    #             },
    #      },
    # 'F03':
    #     {
    #         'id_line': 32,
    #         'id_machine': 265,
    #         'name': 'Seal Tape & Inner Tube',
    #         'ip': '192.168.1.220',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'address':
    #             {
    #                 'master_on_address': 'M10',
    #                 'machine_status_address': 'M1022',
    #                 'mct_address': 'D7200',
    #             },
    #         'production_data':
    #             {
    #                 'Tape Pasting':
    #                     {
    #                         'Data Collection Flag': 'M300',
    #                         'OK Report Flag': 'M301',
    #                         'NG Report Flag': 'M302',
    #                         '2D Code': 'W654',
    #                         'Tape Lot': 'W560',
    #                         'Tape No': 'W568',
    #
    #                     },
    #                 'Img Insp':
    #                     {
    #                         'Data Collection Flag': 'M320',
    #                         'OK Report Flag': 'M321',
    #                         'NG Report Flag': 'M322',
    #                         '2D Code': 'W580',
    #                         'Space Length (mm)': 'W590',
    #                         'Tape Area (pixel)': 'W591',
    #                     },
    #                 'Press Fit':
    #                     {
    #                         'Data Collection Flag': 'M340',
    #                         'OK Report Flag': 'M341',
    #                         'NG Report Flag': 'M342',
    #                         '2D Code': 'W5A0',
    #                         'Orifice Lot': 'W5C0',
    #                         'Orifice No': 'W5C8',
    #                         'Inner Tube Lot': 'W5D0',
    #                         'Inner Tube No': 'W5D8',
    #                         'Press Height (mm)': 'W5B0',
    #                     },
    #             },
    #     },
    # 'F04':
    #     {
    #         'id_line': 32,
    #         'id_machine': 266,
    #         'name': 'GB Propellant filling',
    #         'ip': '192.168.1.219',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'address':
    #             {
    #                 'master_on_address': 'M10',
    #                 'machine_status_address': 'M1022',
    #                 'mct_address': 'D7200',
    #             },
    #         'production_data':
    #             {
    #                 'Pre Metering':
    #                     {
    #                         'Data Collection Flag': 'M320',
    #                         'OK Report Flag': 'M321',
    #                         'NG Report Flag': 'M322',
    #                         '2D Code': 'W780',
    #                         '(preFilling) Jig (PreFilling)': 'W794',
    #                         '(preFilling) PreFill Weight (g)': 'W790',
    #                         '(preFilling) Jig Weight (g)': 'W792',
    #                     },
    #                 'Charge':
    #                     {
    #                         'Data Collection Flag': 'M340',
    #                         'OK Report Flag': 'M341',
    #                         'NG Report Flag': 'M342',
    #                         '2D Code': 'W7A0',
    #                         '(Filling) CID': 'W7B0',
    #                         '(Filling) Jig (Filling)': 'W7B1',
    #                         '(Filling) Humidity': 'W7B2',
    #                         '(Filling) Temperature': 'W7B3',
    #                         '(Filling) Dewpoint': 'W7B4',
    #                         'NQ Lot': 'W7B8',
    #                     },
    #                 'Tapping':
    #                     {
    #                         'Data Collection Flag': 'M360',
    #                         'OK Report Flag': 'M361',
    #                         'NG Report Flag': 'M362',
    #                         '2D Code': 'W7C0',
    #                         '(Tapping) Height Tap (mm)': 'W7D0',
    #                         '(Tapping) Jig (Tap)': 'W7D2',
    #                     },
    #                 'Post Filling':
    #                     {
    #                         'Data Collection Flag': 'M403',
    #                         'OK Report Flag': 'M410',
    #                         'NG Report Flag': 'M411',
    #                         '2D Code': 'W800',
    #                         '(postFilling) PosFill Weight (g)': 'W810',
    #                         '(postFilling) Jig Weight (g)': 'W812',
    #                         '(postFilling) Fill Weight (g)': 'W814',
    #                         '(postFilling) Weight Setting (g)': 'W816',
    #                         '(postFilling) Jig (PstFilling)': 'W818',
    #                     },
    #                 'Holder1':
    #                     {
    #                         'Data Collection Flag': 'M420',
    #                         'OK Report Flag': 'M421',
    #                         'NG Report Flag': 'M422',
    #                         '2D Code': 'W820',
    #                         '(Holder press 1) Height (mm)': 'W830',
    #                         '(Holder press 1) Force (kN)': 'W832',
    #                         '(Holder press 1) Jig (Press)': 'W833',
    #                         'Holder1 Lot': 'W840',
    #                         'Holder1 No': 'W848',
    #                     },
    #                 'Holder2':
    #                     {
    #                         'Data Collection Flag': 'M440',
    #                         'OK Report Flag': 'M441',
    #                         'NG Report Flag': 'M442',
    #                         '2D Code': 'W850',
    #                         '(Holder press 2) Height (mm)': 'W860',
    #                         '(Holder press 2) Force (kN)': 'W862',
    #                         '(Holder press 2) Jig (Press)': 'W863',
    #                         'Holder2 Lot': 'W870',
    #                         'Holder2 No': 'W878',
    #                     },
    #             },
    #     },
    # 'F05':
    #     {
    #         'id_line': 32,
    #         'id_machine': 264,
    #         'name': 'NQ Propellant Filling',
    #         'ip': '192.168.1.218',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'address':
    #             {
    #                 'master_on_address': 'M6',
    #                 'machine_status_address': 'M44',
    #                 'mct_address': 'D50080',
    #             },
    #         'production_data':
    #             {
    #                 'Pre Metering':
    #                     {
    #                         'Data Collection Flag': 'M823',
    #                         'OK Report Flag': 'M301',
    #                         'NG Report Flag': 'M302',
    #                         '2D Code': 'W0DA0',
    #                         '(preFilling) PreFill Weight (g)': 'W0DB0',
    #                         '(preFilling) Jig Weight (g)': 'W0DB2',
    #                         '(preFilling) Jig (PreFilling)': 'W0DB4',
    #                     },
    #                 'Charge':
    #                     {
    #                         'Data Collection Flag': 'M872',
    #                         'OK Report Flag': 'M321',
    #                         'NG Report Flag': 'M322',
    #                         '2D Code': 'W0DC0',
    #                         '(Filling) CID': 'W0DD0',
    #                         '(Filling) Jig (Filling)': 'W0DD1',
    #                         '(Filling) Humidity': 'W0DD2',
    #                         '(Filling) Temperature': 'W0DD3',
    #                         '(Filling) Dewpoint': 'W0DD4',
    #                     },
    #                 'Tapping':
    #                     {
    #                         'Data Collection Flag': 'M340',
    #                         'OK Report Flag': 'M341',
    #                         'NG Report Flag': 'M342',
    #                         '2D Code': 'W0DF0',
    #                         '(Tapping) Height Tap (mm)': 'W0E00',
    #                         '(Tapping) Jig (Tap)': 'W0E02',
    #                     },
    #                 'Post Filling':
    #                     {
    #                         'Data Collection Flag': 'M832',
    #                         'OK Report Flag': 'M361',
    #                         'NG Report Flag': 'M362',
    #                         '2D Code': 'W0E30',
    #                         '(postFilling) PosFill Weight (g)': 'W0E40',
    #                         '(postFilling) Jig Weight (g)': 'W0E42',
    #                         '(postFilling) Fill Weight (g)': 'W0E44',
    #                         '(postFilling) Weight Setting (g)': 'W0E46',
    #                         '(postFilling) Jig (PstFilling)': 'W0E4A',
    #                     },
    #                 'Prop Top':
    #                     {
    #                         'Data Collection Flag': 'M832',
    #                         'OK Report Flag': 'M381',
    #                         'NG Report Flag': 'M382',
    #                         '2D Code': 'W0E50',
    #                         '(Prop Top) Height (mm)': 'W0E60',
    #                         '(Prop Top) Jig': 'W0E62'
    #                     },
    #                 'Ini Press':
    #                     {
    #                         'Data Collection Flag': 'M892',
    #                         'OK Report Flag': 'M401',
    #                         'NG Report Flag': 'M402',
    #                         '2D Code': 'W0E90',
    #                         '(Initiator) Height (mm)': 'W0EA0',
    #                         '(Initiator) Jig': 'W0EA2',
    #                         'Load Force (kN)': 'W0EA4',
    #                         'Initiator Lot': 'W0EB0',
    #                         'Initiator No': 'W0EB8',
    #                         'O-Ring Lot': 'W0EC0',
    #                         'O-Ring No': 'W0EC8',
    #                     },
    #                 'Crimping':
    #                     {
    #                         'Data Collection Flag': 'M420',
    #                         'OK Report Flag': 'M421',
    #                         'NG Report Flag': 'M422',
    #                         '2D Code': 'W0EE0',
    #                         '(Crimping) Height (mm)': 'W0EF0',
    #                         '(Crimping) Jig': 'W0EF2',
    #                     },
    #                 'Ini Measure':
    #                     {
    #                         'Data Collection Flag': 'M440',
    #                         'OK Report Flag': 'M441',
    #                         'NG Report Flag': 'M442',
    #                         '2D Code': 'W0F00',
    #                         'Offset Initiator': 'W0F10'
    #                     },
    #             },
    #     },
    # 'F06':
    #     {
    #         'id_line': 32,
    #         'id_machine': 236,
    #         'name': 'Air Leak test',
    #         'ip': '192.168.1.217',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'address':
    #             {
    #                 'master_on_address': 'M6',
    #                 'machine_status_address': 'M44',
    #                 'mct_address': 'D50080',
    #             },
    #         'production_data':
    #             {
    #                 'Air Leak1':
    #                     {
    #                         'Data Collection Flag': 'M305',
    #                         'OK Report Flag': 'M301',
    #                         'NG Report Flag': 'M302',
    #                         '2D Code': 'W1340',
    #                         'Pressure Large (kPa)': 'W1350',
    #                         'Pressure Small (kPa)': 'W1351',
    #                         'Leak (Pa)': 'W1352',
    #                         'Leak Cycle (sec)': 'W1353',
    #                         'Program No': 'W1354',
    #                     },
    #                 'Air Leak2':
    #                     {
    #                         'Data Collection Flag': 'M325',
    #                         'OK Report Flag': 'M321',
    #                         'NG Report Flag': 'M322',
    #                         '2D Code': 'W1360',
    #                         'Pressure Large (kPa)': 'W1370',
    #                         'Pressure Small (kPa)': 'W1371',
    #                         'Leak (Pa)': 'W1372',
    #                         'Leak Cycle (sec)': 'W1373',
    #                         'Program No': 'W1374',
    #                     },
    #                 'Air Leak3':
    #                     {
    #                         'Data Collection Flag': 'M345',
    #                         'OK Report Flag': 'M341',
    #                         'NG Report Flag': 'M342',
    #                         '2D Code': 'W1380',
    #                         'Pressure Large (kPa)': 'W1390',
    #                         'Pressure Small (kPa)': 'W1391',
    #                         'Leak (Pa)': 'W1392',
    #                         'Leak Cycle (sec)': 'W1393',
    #                         'Program No': 'W1394',
    #                     },
    #                 'Barcode':
    #                     {
    #                         'Data Collection Flag': 'M385',
    #                         'OK Report Flag': 'M381',
    #                         'NG Report Flag': 'M382',
    #                         '2D Code': 'W13D0',
    #                         'Barcode Lot': 'W13E0',
    #                         'Barcode No': 'W13E8',
    #                         'Barcode': 'W13D8',
    #                     },
    #             },
    #     },
    # 'F07':
    #     {
    #         'id_line': 32,
    #         'id_machine': 267,
    #         'name': 'COOL',
    #         'ip': '192.168.1.216',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'address':
    #             {
    #                 'master_on_address': 'M6',
    #                 'machine_status_address': 'M44',
    #                 'mct_address': 'D50080',
    #             },
    #         'production_data':
    #             {
    #                 'SC Charge':
    #                     {
    #                         'Data Collection Flag': 'M305',
    #                         'OK Report Flag': 'M301',
    #                         'NG Report Flag': 'M302',
    #                         'Barcode': 'W1540',
    #                         'Offset (mm)': 'W1550',
    #                         'Height (mm)': 'W1551',
    #                         'S-Clip Lot': 'W1560',
    #                         'S-Clip No': 'W1568',
    #                     },
    #             },
    #     },
    # 'F08':
    #     {
    #         'id_line': 32,
    #         'id_machine': 269,
    #         'name': 'FW & Electrical tester',
    #         'ip': '192.168.1.215',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'address':
    #             {
    #                 'master_on_address': 'M100',
    #                 'machine_status_address': 'M24',
    #                 'mct_address': 'D7600',
    #             },
    #         'production_data':
    #             {
    #                 'CL Pasting':
    #                     {
    #                         'Data Collection Flag': 'M305',
    #                         'OK Report Flag': 'M301',
    #                         'NG Report Flag': 'M302',
    #                         'Barcode': 'W1770',
    #                         'Caution Label Lot)': 'W1780',
    #                         'Caution Label No': 'W1788',
    #                     },
    #                 'Weight':
    #                     {
    #                         'Data Collection Flag': 'M325',
    #                         'OK Report Flag': 'M321',
    #                         'NG Report Flag': 'M322',
    #                         'Barcode': 'W17C0',
    #                         'Finel Weigh Weight (g)': 'W17D0',
    #                     },
    #                 'ETest1':
    #                     {
    #                         'Data Collection Flag': 'M345',
    #                         'OK Report Flag': 'M341',
    #                         'NG Report Flag': 'M342',
    #                         'Barcode': 'W17F0',
    #                         'Resistance (om)': 'W1800',
    #                         'Isolation (om)': 'W1801',
    #                         'Current (mA)': 'W1803',
    #                         'Cycle (sec)': 'W1804',
    #                         'Pin resistance (om)': 'W1806',
    #                         'Pin grounding2 (om)': 'W1807',
    #                         'S.Clip grounding1 (om)': 'W1805',
    #                     },
    #                 'ETest2':
    #                     {
    #                         'Data Collection Flag': 'M365',
    #                         'OK Report Flag': 'M361',
    #                         'NG Report Flag': 'M362',
    #                         'Barcode': 'W1820',
    #                         'Resistance (om)': 'W1830',
    #                         'Isolation (om)': 'W1831',
    #                         'Current (mA)': 'W1833',
    #                         'Cycle (sec)': 'W1834',
    #                         'Pin resistance (om)': 'W1836',
    #                         'Pin grounding2 (om)': 'W1837',
    #                         'S.Clip grounding1 (om)': 'W1835',
    #                     },
    #             },
    #     },
}

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
    'F02':
        {
            'id_line': 32,
            'id_machine': 234,
            'name': 'Stud Bolt',
            'ip': '192.168.1.221',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'endpoints': ['Weld', 'Brush'],
            'endpoints_data_values':
                {
                    'Weld':
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
                                    'size': 1,
                                },
                            '2D Code':
                                {
                                    'address': ['W340', 'W341', 'W342', 'W343', 'W344', 'W345'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            'Bolt lot':
                                {
                                    'address': ['W370', 'W371', 'W372', 'W373', 'W374', 'W375', 'W376', 'W377'],
                                    'type': 'ascii',
                                    'size': 8
                                },

                            'Bolt No':
                                {
                                    'address': ['W378', 'W379', 'W37A', 'W37B', 'W37C', 'W37D', 'W37E', 'W37F'],
                                    'type': 'ascii',
                                    'size': 8
                                },
                            'Jig (weld)':
                                {
                                    'address': ['W380'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Pilot Volt (V)':
                                {
                                    'address': ['W350'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Weld Volt (V)':
                                {
                                    'address': ['W351'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Weld Current (A)':
                                {
                                    'address': ['W352'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Weld Cycle (ms)':
                                {
                                    'address': ['W353'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Weld Depth (mm)':
                                {
                                    'address': ['W354'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Weld Energy (J)':
                                {
                                    'address': ['W355'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Lift (mm)':
                                {
                                    'address': ['W356'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(1st side) Ta (ms)':
                                {
                                    'address': ['W357'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Pilot Volt (V)':
                                {
                                    'address': ['W360'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Weld Volt (V)':
                                {
                                    'address': ['W361'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Weld Current (A)':
                                {
                                    'address': ['W362'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Weld Cycle (ms)':
                                {
                                    'address': ['W363'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Weld Depth (mm)':
                                {
                                    'address': ['W364'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Weld Energy (J)':
                                {
                                    'address': ['W365'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Lift (mm)':
                                {
                                    'address': ['W366'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(2nd side) Ta (ms)':
                                {
                                    'address': ['W367'],
                                    'type': 'int',
                                    'size': 1
                                },
                            # 'Ng Reason (Id)': 'XXXXX',

                        },
                    'Brush':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M320'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W390', 'W391', 'W392', 'W393', 'W394', 'W395'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            'Jig (brush)':
                                {
                                    'address': ['W3A0'],
                                    'type': 'int',
                                    'size': 1
                                },
                        },
                },
            'endpoints_constant_data':
                {
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
                            'production_data': ['2D Code', 'Jig (brush)', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/Marking2D',
                        },
                },
         },
    'F03':
        {
            'id_line': 32,
            'id_machine': 265,
            'name': 'Seal Tape & Inner Tube',
            'ip': '192.168.1.220',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'endpoints': ['Tape_Pasting', 'Img_Insp', 'Press_Fit'],
            'endpoints_data_values':
                {
                    'Tape_Pasting':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M300'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W654'],
                                },
                            'Tape Lot':
                                {
                                    'address': ['W560'],
                                },
                            'Tape No':
                                {
                                    'address': ['W568'],
                                },

                        },
                    'Img_Insp':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M320'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W580'],
                                },
                            'Space Length (mm)':
                                {
                                    'address': ['W590'],
                                },
                            'Tape Area (pixel)':
                                {
                                    'address': ['W591'],
                                },
                        },
                    'Press_Fit':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M340'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W5A0'],
                                },
                            'Orifice Lot':
                                {
                                    'address': ['W5C0'],
                                },
                            'Orifice No':
                                {
                                    'address': ['W5C8'],
                                },
                            'Inner Tube Lot':
                                {
                                    'address': ['W5D0'],
                                },
                            'Inner Tube No':
                                {
                                    'address': ['W5D8'],
                                },
                            'Press Height (mm)':
                                {
                                    'address': ['W5B0'],
                                },
                        },
                },
        },
    'F04':
        {
            'id_line': 32,
            'id_machine': 266,
            'name': 'GB Propellant filling',
            'ip': '192.168.1.219',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'endpoints': ['Pre_Metering', 'Charge', 'Tapping', 'Post_Filling', 'Holder1', 'Holder2'],
            'endpoints_data_values':
                {
                    'Pre_Metering':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M320'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W780'],
                                },
                            '(preFilling) Jig (PreFilling)':
                                {
                                    'address': ['W794'],
                                },
                            '(preFilling) PreFill Weight (g)':
                                {
                                    'address': ['W790'],
                                },
                            '(preFilling) Jig Weight (g)':
                                {
                                    'address': ['W792'],
                                },
                        },
                    'Charge':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M340'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address':['W7A0'],
                                },
                            '(Filling) CID':
                                {
                                    'address': ['W7B0'],
                                },
                            '(Filling) Jig (Filling)':
                                {
                                    'address': ['W7B1'],
                                },
                            '(Filling) Humidity':
                                {
                                    'address': ['W7B2'],
                                },
                            '(Filling) Temperature':
                                {
                                    'address': ['W7B3'],
                                },
                            '(Filling) Dewpoint':
                                {
                                    'address': ['W7B4'],
                                },
                            'NQ Lot':
                                {
                                    'address': ['W7B8'],
                                },
                        },
                    'Tapping':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M360'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W7C0'],
                                },
                            '(Tapping) Height Tap (mm)':
                                {
                                    'address': ['W7D0'],
                                },
                            '(Tapping) Jig (Tap)':
                                {
                                    'address': ['W7D2'],
                                },
                        },
                    'Post_Filling':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M403'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M410'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M411'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W800'],
                                },
                            '(postFilling) PosFill Weight (g)':
                                {
                                    'address': ['W810'],
                                },
                            '(postFilling) Jig Weight (g)':
                                {
                                    'address': ['W812'],
                                },
                            '(postFilling) Fill Weight (g)':
                                {
                                    'address': ['W814'],
                                },
                            '(postFilling) Weight Setting (g)':
                                {
                                    'address': ['W816'],
                                },
                            '(postFilling) Jig (PstFilling)':
                                {
                                    'address': ['W818'],
                                },
                        },
                    'Holder1':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M420'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M421'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M422'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W820'],
                                },
                            '(Holder press 1) Height (mm)':
                                {
                                    'address': ['W830'],
                                },
                            '(Holder press 1) Force (kN)':
                                {
                                    'address': ['W832'],
                                },
                            '(Holder press 1) Jig (Press)':
                                {
                                    'address': ['W833'],
                                },
                            'Holder1 Lot':
                                {
                                    'address': ['W840'],
                                },
                            'Holder1 No':
                                {
                                    'address': ['W848'],
                                },
                        },
                    'Holder2':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M440'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M441'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M442'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W850'],
                                },
                            '(Holder press 2) Height (mm)':
                                {
                                    'address': ['W860'],
                                },
                            '(Holder press 2) Force (kN)':
                                {
                                    'address': ['W862'],
                                },
                            '(Holder press 2) Jig (Press)':
                                {
                                    'address': ['W863'],
                                },
                            'Holder2 Lot':
                                {
                                    'address': ['W870'],
                                },
                            'Holder2 No':
                                {
                                    'address': ['W878'],
                                },
                        },
                },
        },
    'F05':
        {
            'id_line': 32,
            'id_machine': 264,
            'name': 'NQ Propellant Filling',
            'ip': '192.168.1.218',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'endpoints': ['Pre_Metering', 'Charge', 'Tapping', 'Post_Filling', 'Prop_Top', 'Ini_Press',
                          'Crimping', 'Ini_Measure'],
            'endpoints_data_values':
                {
                    'Pre_Metering':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M823'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W0DA0'],
                                },
                            '(preFilling) PreFill Weight (g)':
                                {
                                    'address': ['W0DB0'],
                                },
                            '(preFilling) Jig Weight (g)':
                                {
                                    'address': ['W0DB2'],
                                },
                            '(preFilling) Jig (PreFilling)':
                                {
                                    'address': ['W0DB4'],
                                },
                        },
                    'Charge':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M872'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W0DC0'],
                                },
                            '(Filling) CID':
                                {
                                    'address': 'W0DD0',
                                },
                            '(Filling) Jig (Filling)':
                                {
                                    'address': ['W0DD1'],
                                },
                            '(Filling) Humidity':
                                {
                                    'address': ['W0DD2'],
                                },
                            '(Filling) Temperature':
                                {
                                    'address': ['W0DD3'],
                                },
                            '(Filling) Dewpoint':
                                {
                                    'address': ['W0DD4'],
                                },
                        },
                    'Tapping':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M340'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W0DF0'],
                                },
                            '(Tapping) Height Tap (mm)':
                                {
                                    'address': ['W0E00'],
                                },
                            '(Tapping) Jig (Tap)':
                                {
                                    'address': ['W0E02'],
                                },
                        },
                    'Post_Filling':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M832'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W0E30'],
                                },
                            '(postFilling) PosFill Weight (g)':
                                {
                                    'address': ['W0E40'],
                                },
                            '(postFilling) Jig Weight (g)':
                                {
                                    'address': ['W0E42'],
                                },
                            '(postFilling) Fill Weight (g)':
                                {
                                    'address': ['W0E44'],
                                },
                            '(postFilling) Weight Setting (g)':
                                {
                                    'address': ['W0E46'],
                                },
                            '(postFilling) Jig (PstFilling)':
                                {
                                    'address': ['W0E4A'],
                                },
                        },
                    'Prop_Top':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M832'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M381'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M382'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W0E50'],
                                },
                            '(Prop Top) Height (mm)':
                                {
                                    'address': ['W0E60'],
                                },
                            '(Prop Top) Jig':
                                {
                                    'address': ['W0E62'],
                                },
                        },
                    'Ini_Press':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M892'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M401'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M402'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W0E90'],
                                },
                            '(Initiator) Height (mm)':
                                {
                                    'address': ['W0EA0'],
                                },
                            '(Initiator) Jig':
                                {
                                    'address': ['W0EA2'],
                                },
                            'Load Force (kN)':
                                {
                                    'address': ['W0EA4'],
                                },
                            'Initiator Lot':
                                {
                                    'address': ['W0EB0'],
                                },
                            'Initiator No':
                                {
                                    'address': ['W0EB8'],
                                },
                            'O-Ring Lot':
                                {
                                    'address': ['W0EC0'],
                                },
                            'O-Ring No':
                                {
                                    'address': ['W0EC8'],
                                },
                        },
                    'Crimping':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M420'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M421'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M422'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W0EE0'],
                                },
                            '(Crimping) Height (mm)':
                                {
                                    'address': ['W0EF0'],
                                },
                            '(Crimping) Jig':
                                {
                                    'address': ['W0EF2'],
                                },
                        },
                    'Ini_Measure':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M440'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M441'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M442'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W0F00'],
                                },
                            'Offset Initiator':
                                {
                                    'address': ['W0F10'],
                                },
                        },
                },
        },
    'F06':
        {
            'id_line': 32,
            'id_machine': 236,
            'name': 'Air Leak test',
            'ip': '192.168.1.217',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'endpoints': ['Air_Leak1', 'Air_Leak2', 'Air_Leak3', 'Barcode'],
            'endpoints_data_values':
                {
                    'Air_Leak1':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M305'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W1340'],
                                },
                            'Pressure Large (kPa)':
                                {
                                    'address': ['W1350'],
                                },
                            'Pressure Small (kPa)':
                                {
                                    'address': ['W1351'],
                                },
                            'Leak (Pa)':
                                {
                                    'address': ['W1352'],
                                },
                            'Leak Cycle (sec)':
                                {
                                    'address': ['W1353'],
                                },
                            'Program No':
                                {
                                    'address': ['W1354'],
                                },
                        },
                    'Air_Leak2':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M325'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W1360'],
                                },
                            'Pressure Large (kPa)':
                                {
                                    'address': ['W1370'],
                                },
                            'Pressure Small (kPa)':
                                {
                                    'address': ['W1371'],
                                },
                            'Leak (Pa)':
                                {
                                    'address': ['W1372'],
                                },
                            'Leak Cycle (sec)':
                                {
                                    'address': ['W1373'],
                                },
                            'Program No':
                                {
                                    'address': ['W1374'],
                                },
                        },
                    'Air_Leak3':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M345'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                                    'address': ['W1380'],
                                },
                            'Pressure Large (kPa)':
                                {
                                    'address': ['W1390'],
                                },
                            'Pressure Small (kPa)':
                                {
                                    'address': ['W1391'],
                                },
                            'Leak (Pa)':
                                {
                                    'address': ['W1392'],
                                },
                            'Leak Cycle (sec)':
                                {
                                    'address': ['W1393'],
                                },
                            'Program No':
                                {
                                    'address': ['W1394'],
                                },
                        },
                    'Barcode':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M385'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M381'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M382'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W13D0'],
                                },
                            'Barcode Lot':
                                {
                                    'address': ['W13E0'],
                                },
                            'Barcode No':
                                {
                                    'address': [ 'W13E8'],
                                },
                            'Barcode':
                                {
                                    'address': ['W13D8'],
                                },
                        },
                },
        },
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
                            'Data Collection Flag':
                                {
                                    'address': ['M305'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                            'Barcode':
                                {
                                    'address': ['W1540'],
                                },
                            'Offset (mm)':
                                {
                                    'address': ['W1550'],
                                },
                            'Height (mm)':
                                {
                                    'address': ['W1551'],
                                },
                            'S-Clip Lot':
                                {
                                    'address': ['W1560'],
                                },
                            'S-Clip No':
                                {
                                    'address': ['W1568'],
                                },
                        },
                },
        },
    'F08':
        {
            'id_line': 32,
            'id_machine': 269,
            'name': 'FW & Electrical tester',
            'ip': '192.168.1.215',
            'port': 40020,
            'target_network': None,
            'plc_id_in_target_network': None,
            'endpoints': ['CL_Pasting', 'Weight', 'ETest1', 'ETest2', ],
            'endpoints_data_values':
                {
                    'CL_Pasting':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M305'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                            'Barcode':
                                {
                                    'address': ['W1770'],
                                },
                            'Caution Label Lot)':
                                {
                                    'address': ['W1780'],
                                },
                            'Caution Label No':
                                {
                                    'address': ['W1788'],
                                },
                        },
                    'Weight':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M325'],
                                },
                            'OK Report Flag':
                                {
                                    'address': ['M321'],
                                },
                            'NG Report Flag':
                                {
                                    'address': ['M322'],
                                },
                            'Barcode':
                                {
                                    'address': ['W17C0'],
                                },
                            'Finel Weigh Weight (g)':
                                {
                                    'address': ['W17D0'],
                                },
                        },
                    'ETest1':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M345'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                            'Barcode':
                                {
                                    'address': ['W17F0'],
                                },
                            'Resistance (om)':
                                {
                                    'address': ['W1800'],
                                },
                            'Isolation (om)':
                                {
                                    'address': ['W1801'],
                                },
                            'Current (mA)':
                                {
                                    'address': ['W1803'],
                                },
                            'Cycle (sec)':
                                {
                                    'address': ['W1804'],
                                },
                            'Pin resistance (om)':
                                {
                                    'address': ['W1806'],
                                },
                            'Pin grounding2 (om)':
                                {
                                    'address': ['W1807'],
                                },
                            'S.Clip grounding1 (om)':
                                {
                                    'address': ['W1805'],
                                },
                        },
                    'ETest2':
                        {
                            'Data Collection Flag':
                                {
                                    'address': ['M365'],
                                    'type': 'bit',
                                    'size': 1
                                },
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
                            'Barcode':
                                {
                                    'address': ['W1820'],
                                },
                            'Resistance (om)':
                                {
                                    'address': ['W1830'],
                                },
                            'Isolation (om)':
                                {
                                    'address': ['W1831'],
                                },
                            'Current (mA)':
                                {
                                    'address': ['W1833'],
                                },
                            'Cycle (sec)':
                                {
                                    'address': ['W1834'],
                                },
                            'Pin resistance (om)':
                                {
                                    'address': ['W1836'],
                                },
                            'Pin grounding2 (om)':
                                {
                                    'address': ['W1837'],
                                },
                            'S.Clip grounding1 (om)':
                                {
                                    'address': ['W1835'],
                                },
                        },
                },
        },
}

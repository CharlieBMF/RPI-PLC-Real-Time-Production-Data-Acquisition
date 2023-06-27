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
                                    'address': ['D403'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D404'],
                                    'type': 'int',
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
                                    'address': ['D405'],
                                    'type': 'int',
                                    'size': 1
                                 },
                            'NG Report Flag':
                                {
                                    'address': ['D406'],
                                    'type': 'int',
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
                                    'address': ['D407'],
                                    'type': 'int',
                                    'size': 1
                                 },
                            'NG Report Flag':
                                {
                                    'address': ['D408'],
                                    'type': 'int',
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
            'data_collection_signals_head':
                {
                    '2D_Mark': 'D401',
                    'Press_Fit': 'D403',
                    'Weld': 'D405',
                    'Brush': 'D407',
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
                                    'address': ['D401'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D402'],
                                    'type': 'int',
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
                            'OK Report Flag':
                                {
                                    'address': ['D403'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D404'],
                                    'type': 'int',
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
                            # 'Ng Reason (Id)': 'XXXXX',
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
                            'url': 'http://hamster.dsse.local/EN3/PutData/StudBolt',
                        },
                    'Brush':
                        {
                            'production_data': ['2D Code', 'Jig (brush)', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/StudBolt',
                        },
                },
            'data_collection_signals_head':
                {
                    'Weld': 'D401',
                    'Brush': 'D403',
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
                            'OK Report Flag':
                                {
                                    'address': ['D401'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D402'],
                                    'type': 'bit',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W654', 'W655', 'W656', 'W657', 'W658', 'W659'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            'Tape Lot':
                                {
                                    'address': ['W560', 'W561', 'W562', 'W563', 'W564', 'W565', 'W566', 'W567'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            'Tape No':
                                {
                                    'address': ['W568', 'W569', 'W56A', 'W56B', 'W56C', 'W56D', 'W56E', 'W56F'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            # 'Ng Reason (Id)': 'XXXXX',

                        },
                    'Img_Insp':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D403'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D404'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W580', 'W581', 'W582', 'W583', 'W584', 'W585'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            'Space Length (mm)':
                                {
                                    'address': ['W590'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'Tape Area (pixel)':
                                {
                                    'address': ['W591'],
                                    'type': 'int',
                                    'size': 1
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                    'Press_Fit':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D405'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D406'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W5A0', 'W5A1', 'W5A2', 'W5A3', 'W5A4', 'W5A5'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            'Orifice Lot':
                                {
                                    'address': ['W5C0', 'W5C1', 'W5C2', 'W5C3', 'W5C4', 'W5C5', 'W5C6', 'W5C7'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            'Orifice No':
                                {
                                    'address': ['W5C8', 'W5C9', 'W5CA', 'W5CB', 'W5CC', 'W5CD', 'W5CE', 'W5CF'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            'Inner Tube Lot':
                                {
                                    'address': ['W5D0', 'W5D1', 'W5D2', 'W5D3', 'W5D4', 'W5D5', 'W5D6', 'W5D7'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            'Inner Tube No':
                                {
                                    'address': ['W5D8', 'W5D9', 'W5DA', 'W5DB', 'W5DC', 'W5DD', 'W5DE', 'W5DF'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            'Press Height (mm)':
                                {
                                    'address': ['W5B0'],
                                    'type': 'int',
                                    'size': 2
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                },
            'endpoints_constant_data':
                {
                    'Tape_Pasting':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Img_Insp':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Press_Fit':
                        {
                            'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                },
            'endpoints_constructors':
                {
                    'Tape_Pasting':
                        {
                            'production_data': ['2D Code', 'Tape Lot', 'Tape No', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/SealTape',
                        },
                    'Img_Insp':
                        {
                            'production_data': ['2D Code', 'Space Length (mm)',  'Tape Area (pixel)', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/SealTape',
                        },
                    'Press_Fit':
                        {
                            'production_data': ['2D Code', 'Orifice Lot', 'Orifice No', 'Inner Tube Lot',
                                                'Inner Tube No', 'Press Height (mm)', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/SealTape',
                        },
                },
            'data_collection_signals_head':
                {
                    'Tape_Pasting': 'D401',
                    'Img_Insp': 'D403',
                    'Press_Fit': 'D405',
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
                            '2D Code':
                                {
                                    'address': ['W780', 'W781', 'W782', 'W783', 'W784', 'W785'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            '(preFilling) Jig (PreFilling)':
                                {
                                    'address': ['W794'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(preFilling) PreFill Weight (g)':
                                {
                                    'address': ['W790'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(preFilling) Jig Weight (g)':
                                {
                                    'address': ['W792'],
                                    'type': 'int',
                                    'size': 2
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                    'Charge':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D403'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D404'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W7A0', 'W7A1', 'W7A2', 'W7A3', 'W7A4', 'W7A5'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            '(Filling) CID':
                                {
                                    'address': ['W7B0'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(Filling) Jig (Filling)':
                                {
                                    'address': ['W7B1'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(Filling) Humidity':
                                {
                                    'address': ['W7B2'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(Filling) Temperature':
                                {
                                    'address': ['W7B3'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(Filling) Dewpoint':
                                {
                                    'address': ['W7B4'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NQ Lot':
                                {
                                    'address': ['W7B8', 'W7B9', 'W7BA', 'W7BB', 'W7BC', 'W7BD', 'W7BE', 'W7BF'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                    'Tapping':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D405'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D406'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W7C0', 'W7C1', 'W7C2', 'W7C3', 'W7C4', 'W7C5'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            '(Tapping) Height Tap (mm)':
                                {
                                    'address': ['W7D0'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(Tapping) Jig (Tap)':
                                {
                                    'address': ['W7D2'],
                                    'type': 'int',
                                    'size': 1
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                    'Post_Filling':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D407'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D408'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W800', 'W801', 'W802', 'W803', 'W804', 'W805'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            '(postFilling) PosFill Weight (g)':
                                {
                                    'address': ['W810'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(postFilling) Jig Weight (g)':
                                {
                                    'address': ['W812'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(postFilling) Fill Weight (g)':
                                {
                                    'address': ['W814'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(postFilling) Weight Setting (g)':
                                {
                                    'address': ['W816'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(postFilling) Jig (PstFilling)':
                                {
                                    'address': ['W818'],
                                    'type': 'int',
                                    'size': 1
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                    'Holder1':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D409'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D410'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W820', 'W821', 'W822', 'W823', 'W824', 'W825'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            '(Holder press 1) Height (mm)':
                                {
                                    'address': ['W830'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(Holder press 1) Force (kN)':
                                {
                                    'address': ['W832'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(Holder press 1) Jig (Press)':
                                {
                                    'address': ['W833'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'Holder1 Lot':
                                {
                                    'address': ['W840', 'W841', 'W842', 'W843', 'W844', 'W845', 'W846', 'W847'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            'Holder1 No':
                                {
                                    'address': ['W848', 'W841', 'W842', 'W843', 'W844', 'W845', 'W846', 'W847'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                    'Holder2':
                        {
                            'OK Report Flag':
                                {
                                    'address': ['D411'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'NG Report Flag':
                                {
                                    'address': ['D412'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '2D Code':
                                {
                                    'address': ['W850', 'W851', 'W852', 'W853', 'W854', 'W855'],
                                    'type': 'ascii',
                                    'size': 6,
                                },
                            '(Holder press 2) Height (mm)':
                                {
                                    'address': ['W860'],
                                    'type': 'int',
                                    'size': 2
                                },
                            '(Holder press 2) Force (kN)':
                                {
                                    'address': ['W862'],
                                    'type': 'int',
                                    'size': 1
                                },
                            '(Holder press 2) Jig (Press)':
                                {
                                    'address': ['W863'],
                                    'type': 'int',
                                    'size': 1
                                },
                            'Holder2 Lot':
                                {
                                    'address': ['W870', 'W871', 'W872', 'W873', 'W874', 'W875', 'W876', 'W877'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            'Holder2 No':
                                {
                                    'address': ['W878', 'W879', 'W87A', 'W87B', 'W87C', 'W87D', 'W87E', 'W87F'],
                                    'type': 'ascii',
                                    'size': 8,
                                },
                            # 'Ng Reason (Id)': 'XXXXX',
                        },
                },
            'endpoints_constant_data':
                {
                    'Pre_Metering':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Charge':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Tapping':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Post_Filling':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Holder1':
                        {
                            'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                    'Holder2':
                        {
                            'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 0},
                            'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
                        },
                },
            'endpoints_constructors':
                {
                    'Pre_Metering':
                        {
                            'production_data': ['2D Code', '(preFilling) Jig (PreFilling)',
                                                '(preFilling) PreFill Weight (g)', '(preFilling) Jig Weight (g)',
                                                'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/HolderPress',
                        },
                    'Charge':
                        {
                            'production_data': ['2D Code', '(Filling) CID', '(Filling) Jig (Filling)',
                                                '(Filling) Humidity', '(Filling) Temperature', '(Filling) Dewpoint',
                                                'NQ Lot', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/HolderPress',
                        },
                    'Tapping':
                        {
                            'production_data': ['2D Code', '(Tapping) Height Tap (mm)', '(Tapping) Jig (Tap)',
                                                'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/HolderPress',
                        },
                    'Post_Filling':
                        {
                            'production_data': ['2D Code', '(postFilling) PosFill Weight (g)',
                                                '(postFilling) Jig Weight (g)', '(postFilling) Fill Weight (g)',
                                                '(postFilling) Weight Setting (g)', '(postFilling) Jig (PstFilling)',
                                                'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/HolderPress',
                        },
                    'Holder1':
                        {
                            'production_data': ['2D Code', '(Holder press 1) Height (mm)',
                                                '(Holder press 1) Force (kN)', '(Holder press 1) Jig (Press)',
                                                'Holder1 Lot', 'Holder1 No', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/HolderPress',
                        },
                    'Holder2':
                        {
                            'production_data': ['2D Code', '(Holder press 2) Height (mm)',
                                                '(Holder press 2) Force (kN)', '(Holder press 2) Jig (Press)',
                                                'Holder2 Lot', 'Holder2 No', 'Ng Reason (Id)'],
                            'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
                            'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
                            'url': 'http://hamster.dsse.local/EN3/PutData/HolderPress',
                        },
                },
            'data_collection_signals_head':
                {
                    'Pre_Metering': 'D401',
                    'Charge': 'D403',
                    'Tapping': 'D405',
                    'Post_Filling': 'D407',
                    'Holder1': 'D409',
                    'Holder2': 'D411',
                },
        },
    # 'F05':
    #     {
    #         'id_line': 32,
    #         'id_machine': 264,
    #         'name': 'NQ Propellant Filling',
    #         'ip': '192.168.1.218',
    #         'port': 40020,
    #         'target_network': None,
    #         'plc_id_in_target_network': None,
    #         'endpoints': ['Pre_Metering', 'Charge', 'Tapping', 'Post_Filling', 'Prop_Top', 'Ini_Press',
    #                       'Crimping', 'Ini_Measure'],
    #         'endpoints_data_values':
    #             {
    #                 'Pre_Metering':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D401'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D402'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0DA0', 'W0DA1', 'W0DA2', 'W0DA3', 'W0DA4', 'W0DA5'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         '(preFilling) PreFill Weight (g)':
    #                             {
    #                                 'address': ['W0DB0'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(preFilling) Jig Weight (g)':
    #                             {
    #                                 'address': ['W0DB2'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(preFilling) Jig (PreFilling)':
    #                             {
    #                                 'address': ['W0DB4'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Charge':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D403'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D404'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0DC0', 'W0DC1', 'W0DC2', 'W0DC3', 'W0DC4', 'W0DC5'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         '(Filling) CID':
    #                             {
    #                                 'address': ['W0DD0'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '(Filling) Jig (Filling)':
    #                             {
    #                                 'address': ['W0DD1'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '(Filling) Humidity':
    #                             {
    #                                 'address': ['W0DD2'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '(Filling) Temperature':
    #                             {
    #                                 'address': ['W0DD3'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '(Filling) Dewpoint':
    #                             {
    #                                 'address': ['W0DD4'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Tapping':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D405'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D406'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0DF0', 'W0DF1', 'W0DF2', 'W0DF3', 'W0DF4', 'W0DF5'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         '(Tapping) Height Tap (mm)':
    #                             {
    #                                 'address': ['W0E00'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(Tapping) Jig (Tap)':
    #                             {
    #                                 'address': ['W0E02'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Post_Filling':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D407'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D408'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0E30', 'W0E31', 'W0E32', 'W0E33', 'W0E34', 'W0E35'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         '(postFilling) PosFill Weight (g)':
    #                             {
    #                                 'address': ['W0E40'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(postFilling) Jig Weight (g)':
    #                             {
    #                                 'address': ['W0E42'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(postFilling) Fill Weight (g)':
    #                             {
    #                                 'address': ['W0E44'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(postFilling) Weight Setting (g)':
    #                             {
    #                                 'address': ['W0E46'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(postFilling) Jig (PstFilling)':
    #                             {
    #                                 'address': ['W0E4A'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Prop_Top':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D409'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D410'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0E50', 'W0E51', 'W0E52', 'W0E53', 'W0E54', 'W0E55'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         '(Prop Top) Height (mm)':
    #                             {
    #                                 'address': ['W0E60'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(Prop Top) Jig':
    #                             {
    #                                 'address': ['W0E62'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Ini_Press':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D411'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D412'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0E90', 'W0E91', 'W0E92', 'W0E93', 'W0E94', 'W0E95'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         '(Initiator) Height (mm)':
    #                             {
    #                                 'address': ['W0EA0'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(Initiator) Jig':
    #                             {
    #                                 'address': ['W0EA2'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Load Force (kN)':
    #                             {
    #                                 'address': ['W0EA4'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Initiator Lot':
    #                             {
    #                                 'address': ['W0EB0', 'W0EB1', 'W0EB2', 'W0EB3', 'W0EB4', 'W0EB5', 'W0EB6', 'W0EB7'],
    #                                 'type': 'ascii',
    #                                 'size': 8,
    #                             },
    #                         'Initiator No':
    #                             {
    #                                 'address': ['W0EB8', 'W0EB9', 'W0EBA', 'W0EBB', 'W0EBC', 'W0EBD', 'W0EBE', 'W0EBF'],
    #                                 'type': 'ascii',
    #                                 'size': 8,
    #                             },
    #                         'O-Ring Lot':
    #                             {
    #                                 'address': ['W0EC0', 'W0EC1', 'W0EC2', 'W0EC3', 'W0EC4', 'W0EC5', 'W0EC6', 'W0EC7'],
    #                                 'type': 'ascii',
    #                                 'size': 8,
    #                             },
    #                         'O-Ring No':
    #                             {
    #                                 'address': ['W0EC8', 'W0EC9', 'W0ECA', 'W0ECB', 'W0ECC', 'W0ECD', 'W0ECE', 'W0ECF'],
    #                                 'type': 'ascii',
    #                                 'size': 8,
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Crimping':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D413'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D414'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0EE0', 'W0EE1', 'W0EE2', 'W0EE3', 'W0EE4', 'W0EE5'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         '(Crimping) Height (mm)':
    #                             {
    #                                 'address': ['W0EF0'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         '(Crimping) Jig':
    #                             {
    #                                 'address': ['W0EF2'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Ini_Measure':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D415'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D416'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W0F00', 'W0F01', 'W0F02', 'W0F03', 'W0F04', 'W0F05'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         'Offset Initiator':
    #                             {
    #                                 'address': ['W0F10'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #             },
    #         'endpoints_constant_data':
    #             {
    #                 'Pre_Metering':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'Charge':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 2, 'Seriese': 0}
    #                     },
    #                 'Tapping':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'Post_Filling':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'Prop_Top':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'Ini_Press':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'Crimping':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'Ini_Measure':
    #                     {
    #                         'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #             },
    #         'endpoints_constructors':
    #             {
    #                 'Pre_Metering':
    #                     {
    #                         'production_data': ['2D Code', '(preFilling) PreFill Weight (g)',
    #                                             '(preFilling) Jig Weight (g)', '(preFilling) Jig (PreFilling)',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #                 'Charge':
    #                     {
    #                         'production_data': ['2D Code', '(Filling) CID', '(Filling) Jig (Filling)',
    #                                             '(Filling) Humidity', '(Filling) Temperature', '(Filling) Dewpoint',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #                 'Tapping':
    #                     {
    #                         'production_data': ['2D Code', '(Tapping) Height Tap (mm)', '(Tapping) Jig (Tap)',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #                 'Post_Filling':
    #                     {
    #                         'production_data': ['2D Code', '(postFilling) PosFill Weight (g)',
    #                                             '(postFilling) Jig Weight (g)', '(postFilling) Fill Weight (g)',
    #                                             '(postFilling) Weight Setting (g)', '(postFilling) Jig (PstFilling)',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #                 'Prop_Top':
    #                     {
    #                         'production_data': ['2D Code', '(Prop Top) Height (mm)', '(Prop Top) Jig',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #                 'Ini_Press':
    #                     {
    #                         'production_data': ['2D Code', '(Initiator) Height (mm)', '(Initiator) Jig',
    #                                             'Load Force (kN)', 'Initiator Lot', 'Initiator No', 'O-Ring Lot',
    #                                             'O-Ring No', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #                 'Crimping':
    #                     {
    #                         'production_data': ['2D Code', '(Crimping) Height (mm)', '(Crimping) Jig',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #                 'Ini_Measure':
    #                     {
    #                         'production_data': ['2D Code', 'Offset Initiator', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/InitiatorCrimping',
    #                     },
    #             },
    #         'data_collection_signals_head':
    #             {
    #                 'Pre_Metering': 'D401',
    #                 'Charge': 'D403',
    #                 'Tapping': 'D405',
    #                 'Post_Filling': 'D407',
    #                 'Prop_Top': 'D409',
    #                 'Ini_Press': 'D411',
    #                 'Crimping': 'D413',
    #                 'Ini_Measure': 'D415',
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
    #         'endpoints': ['Air_Leak1', 'Air_Leak2', 'Air_Leak3', 'Barcode'],
    #         'endpoints_data_values':
    #             {
    #                 'Air_Leak1':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D401'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D402'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W1340', 'W1341', 'W1342', 'W1343', 'W1344', 'W1345'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         'Pressure Large (kPa)':
    #                             {
    #                                 'address': ['W1350'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Pressure Small (kPa)':
    #                             {
    #                                 'address': ['W1351'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Leak (Pa)':
    #                             {
    #                                 'address': ['W1352'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Leak Cycle (sec)':
    #                             {
    #                                 'address': ['W1353'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Program No':
    #                             {
    #                                 'address': ['W1354'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Air_Leak2':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D403'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D404'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W1360', 'W1361', 'W1362', 'W1363', 'W1364', 'W1365'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         'Pressure Large (kPa)':
    #                             {
    #                                 'address': ['W1370'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Pressure Small (kPa)':
    #                             {
    #                                 'address': ['W1371'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Leak (Pa)':
    #                             {
    #                                 'address': ['W1372'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Leak Cycle (sec)':
    #                             {
    #                                 'address': ['W1373'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Program No':
    #                             {
    #                                 'address': ['W1374'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Air_Leak3':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D405'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D406'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W1380', 'W1381', 'W1382', 'W1383', 'W1384', 'W1385'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         'Pressure Large (kPa)':
    #                             {
    #                                 'address': ['W1390'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Pressure Small (kPa)':
    #                             {
    #                                 'address': ['W1391'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Leak (Pa)':
    #                             {
    #                                 'address': ['W1392'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Leak Cycle (sec)':
    #                             {
    #                                 'address': ['W1393'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Program No':
    #                             {
    #                                 'address': ['W1394'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Barcode':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D407'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D408'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         '2D Code':
    #                             {
    #                                 'address': ['W13D0', 'W13D1', 'W13D2', 'W13D3', 'W13D4', 'W13D5'],
    #                                 'type': 'ascii',
    #                                 'size': 6,
    #                             },
    #                         'Barcode Lot':
    #                             {
    #                                 'address': ['W13E0', 'W13E1', 'W13E2', 'W13E3', 'W13E4', 'W13E5', 'W13E6', 'W13E7'],
    #                                 'type': 'ascii',
    #                                 'size': 8
    #                             },
    #                         'Barcode No':
    #                             {
    #                                 'address': ['W13E8', 'W13E9', 'W13EA', 'W13EB', 'W13EC', 'W13ED', 'W13EE', 'W13EF'],
    #                                 'type': 'ascii',
    #                                 'size': 8
    #                             },
    #                         'Barcode':
    #                             {
    #                                 'address': ['W13D8', 'W13D9', 'W13DA', 'W13DB', 'W13DC', 'W13DD'],
    #                                 'type': 'ascii',
    #                                 'size': 6
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #             },
    #         'endpoints_constant_data':
    #             {
    #                 'Air_Leak1':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 1},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 1}
    #                     },
    #                 'Air_Leak2':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 2},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 2}
    #                     },
    #                 'Air_Leak3':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 3},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 3}
    #                     },
    #                 'Barcode':
    #                     {
    #                         'constant_ok_part_data': {'Result': 1, 'NG Count': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1}
    #                     },
    #             },
    #         'endpoints_constructors':
    #             {
    #                 'Air_Leak1':
    #                     {
    #                         'production_data': ['2D Code', 'Pressure Large (kPa)', 'Pressure Small (kPa)', 'Leak (Pa)',
    #                                             'Leak Cycle (sec)', 'Program No', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/AirLeak',
    #                     },
    #                 'Air_Leak2':
    #                     {
    #                         'production_data': ['2D Code', 'Pressure Large (kPa)', 'Pressure Small (kPa)', 'Leak (Pa)',
    #                                             'Leak Cycle (sec)', 'Program No', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/AirLeak',
    #                     },
    #                 'Air_Leak3':
    #                     {
    #                         'production_data': ['2D Code', 'Pressure Large (kPa)', 'Pressure Small (kPa)', 'Leak (Pa)',
    #                                             'Leak Cycle (sec)', 'Program No', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/AirLeak',
    #                     },
    #                 'Barcode':
    #                     {
    #                         'production_data': ['2D Code', 'Barcode Lot', 'Barcode No', 'Barcode', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/AirLeak',
    #                     },
    #             },
    #         'data_collection_signals_head':
    #             {
    #                 'Air_Leak1': 'D401',
    #                 'Air_Leak2': 'D403',
    #                 'Air_Leak3': 'D405',
    #                 'Barcode': 'D407',
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
    #         'endpoints': ['SC_Charge'],
    #         'endpoints_data_values':
    #             {
    #                 'SC_Charge':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D401'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D402'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Barcode':
    #                             {
    #                                 'address': ['W1540', 'W1541', 'W1542', 'W1543', 'W1544', 'W1545'],
    #                                 'type': 'ascii',
    #                                 'size': 6
    #                             },
    #                         'Offset (mm)':
    #                             {
    #                                 'address': ['W1550'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Height (mm)':
    #                             {
    #                                 'address': ['W1551'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'S-Clip Lot':
    #                             {
    #                                 'address': ['W1560', 'W1561', 'W1562', 'W1563', 'W1564', 'W1565', 'W1566', 'W1567'],
    #                                 'type': 'ascii',
    #                                 'size': 8
    #                             },
    #                         'S-Clip No':
    #                             {
    #                                 'address': ['W1568', 'W1569', 'W156A', 'W156B', 'W156C', 'W156D', 'W156E', 'W156F'],
    #                                 'type': 'ascii',
    #                                 'size': 8
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #             },
    #         'endpoints_constant_data':
    #             {
    #                 'SC_Charge':
    #                     {
    #                         'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #             },
    #         'endpoints_constructors':
    #             {
    #                 'SC_Charge':
    #                     {
    #                         'production_data': ['Barcode', 'Offset (mm)', 'Height (mm)', 'S-Clip Lot', 'S-Clip No',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/ShortingClip',
    #                     },
    #             },
    #         'data_collection_signals_head':
    #             {
    #                 'SC_Charge': 'D401',
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
    #         'endpoints': ['CL_Pasting', 'Weight', 'ETest1', 'ETest2'],
    #         'endpoints_data_values':
    #             {
    #                 'CL_Pasting':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D401'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D402'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Barcode':
    #                             {
    #                                 'address': ['W1770', 'W1771', 'W1772', 'W1773', 'W1774', 'W1775'],
    #                                 'type': 'ascii',
    #                                 'size': 6
    #                             },
    #                         'Caution Label Lot':
    #                             {
    #                                 'address': ['W1780', 'W1781', 'W1782', 'W1783', 'W1784', 'W1785', 'W1786', 'W1787'],
    #                                 'type': 'ascii',
    #                                 'size': 8
    #                             },
    #                         'Caution Label No':
    #                             {
    #                                 'address': ['W1788', 'W1789', 'W178A', 'W178B', 'W178C', 'W178D', 'W178E', 'W178F'],
    #                                 'type': 'ascii',
    #                                 'size': 8
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'Weight':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D403'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D404'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Barcode':
    #                             {
    #                                 'address': ['W17C0', 'W17C1', 'W17C2', 'W17C3', 'W17C4', 'W17C5'],
    #                                 'type': 'ascii',
    #                                 'size': 6
    #                             },
    #                         'Finel Weigh Weight (g)':
    #                             {
    #                                 'address': ['W17D0'],
    #                                 'type': 'int',
    #                                 'size': 2
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'ETest1':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D405'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D406'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Barcode':
    #                             {
    #                                 'address': ['W17F0', 'W17F1', 'W17F2', 'W17F3', 'W17F4', 'W17F5'],
    #                                 'type': 'ascii',
    #                                 'size': 6
    #                             },
    #                         'Resistance (om)':
    #                             {
    #                                 'address': ['W1800'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Isolation (om)':
    #                             {
    #                                 'address': ['W1801'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Current (mA)':
    #                             {
    #                                 'address': ['W1803'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Cycle (sec)':
    #                             {
    #                                 'address': ['W1804'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Pin resistance (om)':
    #                             {
    #                                 'address': ['W1806'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Pin grounding2 (om)':
    #                             {
    #                                 'address': ['W1807'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'S.Clip grounding1 (om)':
    #                             {
    #                                 'address': ['W1805'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #                 'ETest2':
    #                     {
    #                         'OK Report Flag':
    #                             {
    #                                 'address': ['D407'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'NG Report Flag':
    #                             {
    #                                 'address': ['D408'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Barcode':
    #                             {
    #                                 'address': ['W1820', 'W1821', 'W1822', 'W1823', 'W1824', 'W1825'],
    #                                 'type': 'ascii',
    #                                 'size': 6
    #                             },
    #                         'Resistance (om)':
    #                             {
    #                                 'address': ['W1830'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Isolation (om)':
    #                             {
    #                                 'address': ['W1831'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Current (mA)':
    #                             {
    #                                 'address': ['W1833'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Cycle (sec)':
    #                             {
    #                                 'address': ['W1834'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Pin resistance (om)':
    #                             {
    #                                 'address': ['W1836'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'Pin grounding2 (om)':
    #                             {
    #                                 'address': ['W1837'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         'S.Clip grounding1 (om)':
    #                             {
    #                                 'address': ['W1835'],
    #                                 'type': 'int',
    #                                 'size': 1
    #                             },
    #                         # 'Ng Reason (Id)': 'XXXXX',
    #                     },
    #             },
    #         'endpoints_constant_data':
    #             {
    #                 'CL_Pasting':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'Weight':
    #                     {
    #                         'constant_ok_part_data': {'Result': 0, 'NG Count': 0, 'Seriese': 0},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 0}
    #                     },
    #                 'ETest1':
    #                     {
    #                         'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 1},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 1}
    #                     },
    #                 'ETest2':
    #                     {
    #                         'constant_ok_part_data': {'Result': 1, 'NG Count': 0, 'Seriese': 2},
    #                         'constant_ng_part_data': {'Result': -1, 'NG Count': 1, 'Seriese': 2}
    #                     },
    #             },
    #         'endpoints_constructors':
    #             {
    #                 'CL_Pasting':
    #                     {
    #                         'production_data': ['Barcode', 'Caution Label Lot', 'Caution Label No', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/FinalWeight',
    #                     },
    #                 'Weight':
    #                     {
    #                         'production_data': ['2D Code', 'Finel Weigh Weight (g)', 'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/FinalWeight',
    #                     },
    #                 'ETest1':
    #                     {
    #                         'production_data': ['Barcode', 'Resistance (om)', 'Isolation (om)', 'Current (mA)', 'Cycle (sec)',
    #                                             'Pin resistance (om)', 'Pin grounding2 (om)', 'S.Clip grounding1 (om)',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/FinalWeight',
    #                     },
    #                 'ETest2':
    #                     {
    #                         'production_data': ['Barcode', 'Resistance (om)', 'Isolation (om)', 'Current (mA)', 'Cycle (sec)',
    #                                             'Pin resistance (om)', 'Pin grounding2 (om)', 'S.Clip grounding1 (om)',
    #                                             'Ng Reason (Id)'],
    #                         'constant_ok_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'constant_ng_part_data': ['Result', 'NG Count', 'Seriese'],
    #                         'url': 'http://hamster.dsse.local/EN3/PutData/FinalWeight',
    #                     },
    #             },
    #         'data_collection_signals_head':
    #             {
    #                 'CL_Pasting': 'D401',
    #                 'Weight': 'D403',
    #                 'ETest1': 'D405',
    #                 'ETest2': 'D407',
    #             },
    #     },
}

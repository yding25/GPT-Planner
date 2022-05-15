import numpy as np
from utility import predicate_generator


def situation_simulator(task_id):
    if task_id == 1:
        situations = {
            0: 'there is a power outage.',
            1: 'the vacuum is not working.',
            2: 'the vacuum is missing.',
            3: 'the vacuum cannot be turned on.',
            4: 'the vacuum plug is damaged.',
            5: 'the outlet is missing.',
            6: 'the vacuum is not plugged.',
            7: 'the vacuum canister is full.',
            8: 'the vacuum power cord is too short.',
            9: 'the robot cannot reach the vacuum.',
            10: 'the vacuum switch is not working.',
            11: 'the vacuum power cord is broken.',
            12: 'the vacuum is battery powered and does not need plug in.',
            13: 'the robot slips and falls.',
            14: 'the robot drops the vacuum.',
            15: 'the plug is damaged.',
            16: 'the outlet is broken.'
        }

        situations_opp = {
            0: 'power available.',
            1: 'vacuum work.',
            2: 'vacuum found.',
            3: 'vacuum turned on.',
            4: 'vacuum plug good to use.',
            5: 'outlet found.',
            6: 'vacuum plugged.',
            7: 'vacuum canister empty.',
            8: 'vacuum power cord long.',
            9: 'robot reaching the vacuum.',
            10: 'vacuum switch working.',
            11: 'vacuum power cord good to use.',
            12: 'vacuum plug needed.',
            13: 'robot standing.',
            14: 'robot picking up vacuum.',
            15: 'plug undamaged.',
            16: 'outlet good.'
        }

        situations_object = {
            0: 'power',
            1: 'vacuum',
            2: 'vacuum',
            3: 'vacuum',
            4: 'vacuum plug',
            5: 'outlet',
            6: 'vacuum',
            7: 'vacuum canister',
            8: 'vacuum power cord',
            9: 'robot',
            10: 'vacuum switch',
            11: 'vacuum power cord',
            12: 'vacuum plug',
            13: 'robot',
            14: 'robot',
            15: 'vacuum plug',
            16: 'outlet'
        }

        situations_prob = {
            0: 28 / 91.,
            1: 12 / 91.,
            2: 10 / 91.,
            3: 10 / 91.,
            4: 7 / 91.,
            5: 6 / 91.,
            6: 3 / 91.,
            7: 3 / 91.,
            8: 2 / 91.,
            9: 2 / 91.,
            10: 2 / 91.,
            11: 1 / 91.,
            12: 1 / 91.,
            13: 1 / 91.,
            14: 1 / 91.,
            15: 1 / 91.,
            16: 1 / 91.
        }

        situations_action = {
            0: ['turnon_vacuum', 'clean_area'],
            1: ['turnon_vacuum', 'clean_area'],
            2: ['grasp_vacuum'],
            3: ['grasp_vacuum'],
            4: ['plug_vacuum'],
            5: ['plug_vacuum'],
            6: ['plug_vacuum'],
            7: ['grasp_vacuum', 'clean_area'],
            8: ['plug_vacuum'],
            9: ['clean_area'],
            10: ['turnon_vacuum'],
            11: ['plug_vacuum'],
            12: ['plug_vacuum'],
            13: ['find_table'],
            14: ['grasp_vacuum'],
            15: ['turnon_vacuum'],
            16: ['plug_vacuum']
        }

        actions_prob = {
            0: [9 / 28., 19 / 28.],
            1: [11 / 12., 1 / 12.],
            2: [10 / 10.],
            3: [10 / 10.],
            4: [7 / 7.],
            5: [6 / 6.],
            6: [3 / 3.],
            7: [2 / 3., 1 / 3.],
            8: [2 / 2.],
            9: [2 / 2.],
            10: [2 / 2.],
            11: [1 / 1.],
            12: [1 / 1.],
            13: [1 / 1.],
            14: [1 / 1.],
            15: [1 / 1.],
            16: [1 / 1.]
        }

        # randomly select a situation
        situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

        # test
        # situation_index = 0

        situation = situations[situation_index]
        situation_opp = situations_opp[situation_index]
        situation_object = situations_object[situation_index]
        situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
        situation_predicate = predicate_generator(situation)

        # test
        # situation_action = 'clean_area'

        return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

    if task_id == 4:
        situations = {
            0: 'the cup is broken.',
            1: 'the faucet has no water.',
            2: 'the cup is dirty.',
            3: 'the cup is missing.',
            4: 'the water is dirty.',
            5: 'the water is hot.',
            6: 'the faucet is broken.',
            7: 'the faucet cannot be turned on.',
            8: 'the faucet is not found.',
            9: 'the faucet is dripping.',
            10: 'the cup is in the box.',
            11: 'the water spills on the ground.',
            12: 'the cup is not full.',
            13: 'the water is drunk by others.',
            14: 'the cup full of water falls down.'
        }

        situations_opp = {
            0: 'a cup not broken.',
            1: 'a faucet have water.',
            2: 'a cup clean.',
            3: 'a cup found.',
            4: 'water clean.',
            5: 'water not hot.',
            6: 'a faucet not broken.',
            7: 'a faucet easy to be turned on.',
            8: 'a faucet found.',
            9: 'a faucet not dripping.',
            10: 'a cup took out from the box.',
            11: 'a ground dry.',
            12: 'a cup full.',
            13: 'water not drunk by others.',
            14: 'a cup full of water not falling down.'
        }

        situations_object = {
            0: 'cup',
            1: 'faucet',
            2: 'cup',
            3: 'cup',
            4: 'water',
            5: 'water',
            6: 'faucet',
            7: 'faucet',
            8: 'faucet',
            9: 'faucet',
            10: 'cup',
            11: 'water',
            12: 'cup',
            13: 'water',
            14: 'cup'
        }

        situations_prob = {
            0: 23 / 95.,
            1: 23 / 95.,
            2: 14 / 95.,
            3: 10 / 95.,
            4: 7 / 95.,
            5: 3 / 95.,
            6: 3 / 95.,
            7: 2 / 95.,
            8: 3 / 95.,
            9: 1 / 95.,
            10: 1 / 95.,
            11: 1 / 95.,
            12: 2 / 95.,
            13: 1 / 95.,
            14: 1 / 95.
        }

        situations_action = {
            0: ['find_cup', 'hold_cup', 'fill_cup'],
            1: ['turnon_faucet', 'fill_cup'],
            2: ['find_cup', 'hold_cup'],
            3: ['find_cup', 'hold_cup'],
            4: ['turnon_faucet', 'fill_cup', 'place_cup'],
            5: ['find_cup', 'fill_cup'],
            6: ['turnon_faucet'],
            7: ['turnon_faucet'],
            8: ['find_faucet'],
            9: ['place_cup'],
            10: ['find_cup'],
            11: ['fill_cup'],
            12: ['fill_cup', 'place_cup'],
            13: ['place_cup'],
            14: ['place_cup']
        }

        actions_prob = {
            0: [1 / 23., 16 / 23., 6 / 23.],
            1: [15 / 23., 8 / 23.],
            2: [13 / 14., 1 / 14.],
            3: [9 / 10., 1 / 10.],
            4: [2 / 7., 3 / 7., 2 / 7.],
            5: [2 / 3., 1 / 3.],
            6: [3 / 3.],
            7: [2 / 2.],
            8: [1 / 1.],
            9: [1 / 1.],
            10: [1 / 1.],
            11: [1 / 1.],
            12: [1 / 2., 1 / 2.],
            13: [1 / 1.],
            14: [1 / 1.]
        }

        # randomly select a situation
        situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

        # test
        # situation_index = 2

        situation = situations[situation_index]
        situation_opp = situations_opp[situation_index]
        situation_object = situations_object[situation_index]
        situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
        situation_predicate = predicate_generator(situation)

        return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

    if task_id == 6:
        situations = {
            0: 'the plate is broken.',
            1: 'the plate is not found.',
            2: 'the plate is dirty.',
            3: 'the fork is dirty.',
            4: 'the fork is not found.',
            5: 'the table is dirty.',
            6: 'the table is not found.',
            7: 'the cupboard cannot open.',
            8: 'the plate falls on the ground.',
            9: 'the table does not have enough space.',
            10: 'the fork falls on the ground.',
            11: 'the cupboard has some mites.',
            12: 'the cupboard is broken.',
            13: 'the fork is already on the table.',
            14: 'the fork is broken.',
            15: 'the table is broken.',
            16: 'the robot is stopped due to obstacles.'
        }

        situations_opp = {
            0: 'a plate not broken.',
            1: 'a plate found.',
            2: 'a plate clean.',
            3: 'a fork dirty.',
            4: 'a fork found.',
            5: 'a table clean.',
            6: 'a table found.',
            7: 'a cupboard open.',
            8: 'a plate grasped.',
            9: 'a table big enough.',
            10: 'a fork grasped.',
            11: 'mites in a cupboard killed.',
            12: 'a cupboard not broken.',
            13: 'a fork not on the table.',
            14: 'a fork broken.',
            15: 'a table broken.',
            16: 'there are no obstacles.'
        }

        situations_object = {
            0: 'plate',
            1: 'plate',
            2: 'plate',
            3: 'fork',
            4: 'fork',
            5: 'table',
            6: 'table',
            7: 'cupboard',
            8: 'plate',
            9: 'table',
            10: 'fork',
            11: 'cupboard',
            12: 'cupboard',
            13: 'fork',
            14: 'fork',
            15: 'table',
            16: 'obstacle'
        }

        situations_prob = {
            0: 21 / 92.,
            1: 13 / 92.,
            2: 12 / 92.,
            3: 8 / 92.,
            4: 7 / 92.,
            5: 6 / 92.,
            6: 4 / 92.,
            7: 4 / 92.,
            8: 4 / 92.,
            9: 4 / 92.,
            10: 3 / 92.,
            11: 1 / 92.,
            12: 1 / 92.,
            13: 1 / 92.,
            14: 1 / 92.,
            15: 1 / 92.,
            16: 1 / 92.
        }

        situations_action = {
            0: ['open_cupboard', 'find_plate'],
            1: ['find_cupboard', 'find_plate'],
            2: ['find_plate', 'takeout_plate', 'place_plate'],
            3: ['find_fork', 'takeout_fork', 'place_fork'],
            4: ['find_fork', 'takeout_fork'],
            5: ['find_table', 'place_plate'],
            6: ['find_table'],
            7: ['open_cupboard'],
            8: ['takeout_plate', 'place_plate'],
            9: ['place_plate', 'place_fork'],
            10: ['takeout_fork', 'place_fork'],
            11: ['open_cupboard'],
            12: ['open_cupboard'],
            13: ['find_fork'],
            14: ['find_fork'],
            15: ['find_table'],
            16: ['walk']
        }

        actions_prob = {
            0: [3 / 21., 18 / 21.],
            1: [2 / 13., 11 / 13.],
            2: [4 / 12., 4 / 12., 4 / 12.],
            3: [5 / 8., 2 / 8., 1 / 8.],
            4: [6 / 7., 1 / 7.],
            5: [2 / 6., 4 / 6.],
            6: [4 / 4.],
            7: [4 / 4.],
            8: [2 / 4., 2 / 4.],
            9: [2 / 4., 2 / 4.],
            10: [2 / 3., 1 / 3.],
            11: [1 / 1.],
            12: [1 / 1.],
            13: [1 / 1.],
            14: [1 / 1.],
            15: [1 / 1.],
            16: [1 / 1.]
        }

        # randomly select a situation
        situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

        # test
        # situation_index = 0

        situation = situations[situation_index]
        situation_opp = situations_opp[situation_index]
        situation_object = situations_object[situation_index]
        situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
        situation_predicate = predicate_generator(situation)

        return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

    if task_id == 9:
        situations = {
            0: 'the sink is full.',
            1: 'the plate is broken.',
            2: 'the plate is already clean.',
            3: 'the dirty plate is missing on table.',
            4: 'the plate is dropped.',
            5: 'the plate is missing.',
            6: 'the table is missing.',
            7: 'the sink is too dirty.',
            8: 'there is no water in sink.',
            9: 'the table is dirty.',
            10: 'the table is broken.',
            11: 'the sink cannot be found.',
            12: 'the plate is grabbed by dog.',
            13: 'the door of dinning room is locked.',
            14: 'the dirty plate has already been placed in the sink.',
            15: 'people are not finishing food.'
        }

        situations_opp = {
            0: 'a sink empty.',
            1: 'a plate unbroken.',
            2: 'a plat dirty',
            3: 'a plate found',
            4: 'a plate not dropped.',
            5: 'a plate found.',
            6: 'a table found.',
            7: 'a sink clean.',
            8: 'water in the sink.',
            9: 'a table clean.',
            10: 'a table good.',
            11: 'a sink found.',
            12: 'a plate on the table.',
            13: 'a door open.',
            14: 'a plate on the table.',
            15: 'people finishing food.'
        }

        situations_object = {
            0: 'sink',
            1: 'plate',
            2: 'plate',
            3: 'plate',
            4: 'plate',
            5: 'plate',
            6: 'table',
            7: 'sink',
            8: 'water',
            9: 'table',
            10: 'table',
            11: 'sink',
            12: 'plate',
            13: 'door',
            14: 'plate',
            15: 'people'
        }

        situations_prob = {
            0: 24 / 91.,
            1: 17 / 91.,
            2: 11 / 91.,
            3: 11 / 91.,
            4: 9 / 91.,
            5: 6 / 91.,
            6: 2 / 91.,
            7: 2 / 91.,
            8: 1 / 91.,
            9: 1 / 91.,
            10: 1 / 91.,
            11: 1 / 91.,
            12: 1 / 91.,
            13: 1 / 91.,
            14: 2 / 91.,
            15: 1 / 91.
        }

        situations_action = {
            0: ['walk_sink', 'place_plate'],
            1: ['grasp_plate'],
            2: ['grasp_plate', 'place_plate'],
            3: ['grasp_plate', 'place_plate'],
            4: ['grasp_plate', 'walk_sink', 'place_plate'],
            5: ['grasp_plate', 'walk_sink'],
            6: ['walk_table'],
            7: ['walk_sink'],
            8: ['walk_sink'],
            9: ['walk_table'],
            10: ['walk_table'],
            11: ['walk_sink'],
            12: ['grasp_plate'],
            13: ['walk'],
            14: ['grasp_plate'],
            15: ['walk']
        }

        actions_prob = {
            0: [23 / 24., 1 / 24.],
            1: [17 / 17.],
            2: [8 / 11., 3 / 11.],
            3: [8 / 11., 3 / 11.],
            4: [6 / 9., 1 / 9., 2 / 9.],
            5: [5 / 6., 1 / 6.],
            6: [2 / 2.],
            7: [2 / 2.],
            8: [1 / 1.],
            9: [1 / 1.],
            10: [1 / 1.],
            11: [1 / 1.],
            12: [1 / 1.],
            13: [1 / 1.],
            14: [1 / 1.],
            15: [1 / 1.]
        }

        # randomly select a situation
        situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

        # test
        # situation_index = 0

        situation = situations[situation_index]
        situation_opp = situations_opp[situation_index]
        situation_object = situations_object[situation_index]
        situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
        situation_predicate = predicate_generator(situation)

        return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

    if task_id == 10:
        situations = {
            0: 'the bottle of soda is not available.',
            1: 'the glass is broken.',
            2: 'the bottle of soda is missing.',
            3: 'the glass is dirty.',
            4: 'the glass falls down.',
            5: 'the bottle of soda spills.',
            6: 'the glass is missing.',
            7: 'the bottle of soda is flat.',
            8: 'the bottle of soda cannot be opened.',
            9: 'the bottle of soda is empty.',
            10: 'the bottle of soda is dropped.',
            11: 'the robot cannot recognize the bottle, and take beer out.',
            12: 'the bottle of soda is sticky and leaking.',
            13: 'the bottle of soda is not chill.',
            14: 'the bottle of soda is too frozen.'
        }

        situations_opp = {
            0: 'bottle of soda available.',
            1: 'a glass good.',
            2: 'bottle of soda found.',
            3: 'a glass clean',
            4: 'a glass picked up.',
            5: 'a ground clean.',
            6: 'a glass found.',
            7: 'bottle of soda full of carbon dioxide.',
            8: 'bottle of soda easy to be opened.',
            9: 'bottle of soda full of liquid.',
            10: 'bottle of soda grasped.',
            11: 'a robot successfully recognizing and grasping the bottle of soda.',
            12: 'bottle of soda clean.',
            13: 'bottle of soda chilled.',
            14: 'bottle of soda not too frozen.'
        }

        situations_object = {
            0: 'soda',
            1: 'glass',
            2: 'soda',
            3: 'glass',
            4: 'glass',
            5: 'soda',
            6: 'glass',
            7: 'soda',
            8: 'soda',
            9: 'soda',
            10: 'soda',
            11: 'robot',
            12: 'soda',
            13: 'soda',
            14: 'soda'
        }

        situations_prob = {
            0: 18 / 90.,
            1: 11 / 90.,
            2: 11 / 90.,
            3: 9 / 90.,
            4: 8 / 90.,
            5: 8 / 90.,
            6: 7 / 90.,
            7: 5 / 90.,
            8: 4 / 90.,
            9: 3 / 90.,
            10: 2 / 90.,
            11: 1 / 90.,
            12: 1 / 90.,
            13: 1 / 90.,
            14: 1 / 90.
        }

        situations_action = {
            0: ['find_soda', 'grasp_soda'],
            1: ['find_glass', 'move_glass'],
            2: ['find_soda'],
            3: ['find_glass'],
            4: ['pour_soda', 'place_glass'],
            5: ['find_glass', 'pour_soda'],
            6: ['find_glass'],
            7: ['place_glass'],
            8: ['pour_soda'],
            9: ['find_soda'],
            10: ['pour_soda'],
            11: ['find_soda'],
            12: ['find_soda'],
            13: ['grasp_soda'],
            14: ['grasp_soda']
        }

        actions_prob = {
            0: [14 / 18., 4 / 18.],
            1: [8 / 11., 3 / 11.],
            2: [11 / 11.],
            3: [9 / 9.],
            4: [2 / 8., 6 / 8.],
            5: [2 / 8., 6 / 8.],
            6: [7 / 7.],
            7: [5 / 5.],
            8: [4 / 4.],
            9: [3 / 3.],
            10: [2 / 2.],
            11: [1 / 1.],
            12: [1 / 1.],
            13: [1 / 1.],
            14: [1 / 1.]
        }

        # randomly select a situation
        situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

        # test
        # situation_index = 2

        situation = situations[situation_index]
        situation_opp = situations_opp[situation_index]
        situation_object = situations_object[situation_index]
        situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
        situation_predicate = predicate_generator(situation)

        # test
        # situation_action = 'find_soda'

        return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

    if task_id == 11:
        situations = {
            0: 'the chair is broken.',
            1: 'the burger is missing.',
            2: 'the fork is missing.',
            3: 'the plate is dirty.',
            4: 'the plate is missing.',
            5: 'the chair is occupied.',
            6: 'the fork is dirty.',
            7: 'the burger spills.',
            8: 'the burger is overcooked.',
            9: 'the chair is missing.',
            10: 'the chair is dirty.',
            11: 'the plate is placed already.',
            12: 'the table is dirty.',
            13: 'the spoon is missing.',
            14: 'the plate is not available.',
            15: 'the plate is broken.',
            16: 'the fork is broken.',
            17: 'the burger smells bad.',
            18: 'the burger is not enough for a person.',
            19: 'the burger is expired.',
            20: 'the burger is dirty.',
            21: 'the chair slipped.',
            22: 'the chair is wet.'
        }

        situations_opp = {
            0: 'a chair unbroken.',
            1: 'a burger found.',
            2: 'a fork found.',
            3: 'a plate clean.',
            4: 'a plate found.',
            5: 'a chair available.',
            6: 'a fork clean.',
            7: 'a ground clean',
            8: 'a burger well-cooked.',
            9: 'a chair found.',
            10: 'a chair clean.',
            11: 'a plate not placed on the table.',
            12: 'a table clean.',
            13: 'a spoon found.',
            14: 'a plate available.',
            15: 'a plate unbroken.',
            16: 'a fork unbroken.',
            17: 'a burger good.',
            18: 'a burger enough for a person.',
            19: 'a burger in good condition.',
            20: 'a burger clean.',
            21: 'a chair not slipped.',
            22: 'a chair dry.'
        }

        situations_object = {
            0: 'chair',
            1: 'burger',
            2: 'fork',
            3: 'plate',
            4: 'plate',
            5: 'chair',
            6: 'fork',
            7: 'burger',
            8: 'burger',
            9: 'chair',
            10: 'chair',
            11: 'plate',
            12: 'table',
            13: 'spoon',
            14: 'plate',
            15: 'plate',
            16: 'fork',
            17: 'burger',
            18: 'burger',
            19: 'burger',
            20: 'burger',
            21: 'chair',
            22: 'chair'
        }

        situations_prob = {
            0: 23 / 84.,
            1: 15 / 84.,
            2: 10 / 84.,
            3: 5 / 84.,
            4: 4 / 84.,
            5: 4 / 84.,
            6: 3 / 84.,
            7: 2 / 84.,
            8: 2 / 84.,
            9: 2 / 84.,
            10: 2 / 84.,
            11: 1 / 84.,
            12: 1 / 84.,
            13: 1 / 84.,
            14: 1 / 84.,
            15: 1 / 84.,
            16: 1 / 84.,
            17: 1 / 84.,
            18: 1 / 84.,
            19: 1 / 84.,
            20: 1 / 84.,
            21: 1 / 84.,
            22: 1 / 84.
        }

        situations_action = {
            0: ['find_chair', 'pull_chair'],
            1: ['find_burger'],
            2: ['find_fork'],
            3: ['find_plate'],
            4: ['find_plate'],
            5: ['find_chair'],
            6: ['find_fork'],
            7: ['place_plate'],
            8: ['find_burger'],
            9: ['find_chair'],
            10: ['find_chair'],
            11: ['place_plate'],
            12: ['find_table'],
            13: ['place_plate'],
            14: ['find_plate'],
            15: ['find_plate'],
            16: ['find_burger'],
            17: ['find_burger'],
            18: ['find_burger'],
            19: ['find_burger'],
            20: ['find_burger'],
            21: ['find_chair'],
            22: ['find_chair']
        }

        actions_prob = {
            0: [12 / 23., 11 / 23.],
            1: [15 / 15.],
            2: [10 / 10.],
            3: [5 / 5.],
            4: [4 / 4.],
            5: [4 / 4.],
            6: [3 / 3.],
            7: [2 / 2.],
            8: [2 / 2.],
            9: [2 / 2.],
            10: [2 / 2.],
            11: [1 / 1.],
            12: [1 / 1.],
            13: [1 / 1.],
            14: [1 / 1.],
            15: [1 / 1.],
            16: [1 / 1.],
            17: [1 / 1.],
            18: [1 / 1.],
            19: [1 / 1.],
            20: [1 / 1.],
            21: [1 / 1.],
            22: [1 / 1.]
        }

        # randomly select a situation
        situation_index = np.random.choice(list(range(0, len(situations))), p=list(situations_prob.values()))

        # test
        # situation_index = 0

        situation = situations[situation_index]
        situation_opp = situations_opp[situation_index]
        situation_object = situations_object[situation_index]
        situation_action = np.random.choice(situations_action[situation_index], p=actions_prob[situation_index])
        situation_predicate = predicate_generator(situation)

        return situation_index, situation, situation_opp, situation_object, situation_predicate, situation_action

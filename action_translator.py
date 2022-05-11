def action_translator(action, task_id):
    if task_id == 1:
        action_qualified = []
        for index in range(len(action)):
            item = action[index]
            if index >= 1:
                if '_' in item:
                    item = item[:-2]
                    action_qualified.append(item)
                else:
                    action_qualified.append(item)
            else:
                action_qualified.append(item)
        action = action_qualified

        sentence = None

        if 'walk' in action[0]:
            sentence = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'takeout_vacuum' in action[0]:
            sentence = 'a robot takes out a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_table' in action[0]:
            sentence = 'a robot find a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'plug_vacuum' in action[0]:
            sentence = 'a robot plugs a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'turnon_vacuum' in action[0]:
            sentence = 'a robot turns on a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'clean_table' in action[0]:
            sentence = 'a robot clean a ' + action[3] + ' using ' + action[2] + ' in ' + action[4] + ' room.'

        if 'turnoff_vacuum' in action[0]:
            sentence = 'a robot turns off a ' + action[2] + 'in' + action[4] + ' room' + ' after a table is clean.'

        if 'unplug_vacuum' in action[0]:
            sentence = 'a robot unplugs a ' + action[2] + ' in ' + action[4] + ' room.'

        if sentence is None:
            print('Error -- cannot find corresponding action.')
        else:
            return sentence

    if task_id == 4:
        action_qualified = []
        for index in range(len(action)):
            item = action[index]
            if index >= 1:
                if '_' in item:
                    item = item[:-2]
                    action_qualified.append(item)
                else:
                    action_qualified.append(item)
            else:
                action_qualified.append(item)
        action = action_qualified

        sentence = None

        if 'walk' in action[0]:
            sentence = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_faucet' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'turnon_faucet' in action[0]:
            sentence = 'a robot turns on a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_cup' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'hold_cup' in action[0]:
            sentence = 'a robot holds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'fill_cup' in action[0]:
            sentence = 'a robot fills a ' + action[2] + ' with water from ' + action[3] + ' in ' + action[4] + ' room.'

        if 'move_cup' in action[0]:
            sentence = 'a robot moves a ' + action[2] + ' from ' + action[3] + ' room to ' + action[4] + ' room.'

        if 'place_cup' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' on ' + action[3] + ' in ' + action[4] + ' room.'

        if 'turnoff_faucet' in action[0]:
            sentence = 'a robot turns off a ' + action[2] + ' in ' + action[3] + ' room.'

        if sentence is None:
            print('Error -- cannot find corresponding action.')
        else:
            return sentence

    if task_id == 6:
        action_qualified = []
        for index in range(len(action)):
            item = action[index]
            if index >= 1:
                if '_' in item:
                    item = item[:-2]
                    action_qualified.append(item)
                else:
                    action_qualified.append(item)
            else:
                action_qualified.append(item)
        action = action_qualified

        sentence = None

        if 'walk' in action[0]:
            sentence = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_table' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_cupboard' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_plate' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_fork' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'takeout_plate' in action[0]:
            sentence = 'a robot takes out a ' + action[2] + ' from a ' + action[3] + '.'

        if 'takeout_fork' in action[0]:
            sentence = 'a robot takes out a ' + action[2] + ' from a ' + action[3] + '.'

        if 'open_cupboard' in action[0]:
            sentence = 'a robot opens a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'close_cupboard' in action[0]:
            sentence = 'a robot closes a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'move_plate' in action[0]:
            sentence = 'a robot moves a ' + action[2] + ' from ' + action[3] + ' room to ' + action[4] + ' room.'

        if 'move_fork' in action[0]:
            sentence = 'a robot moves a ' + action[2] + ' from ' + action[3] + ' room to ' + action[4] + ' room.'

        if 'place_plate' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' on ' + action[3] + ' in ' + action[4] + ' room.'

        if 'place_fork' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' on ' + action[3] + ' in ' + action[4] + ' room.'

        if sentence is None:
            print('Cannot find corresponding action.')
        else:
            return sentence

    if task_id == 9:
        action_qualified = []
        for index in range(len(action)):
            item = action[index]
            if index >= 1:
                if '_' in item:
                    item = item[:-2]
                    action_qualified.append(item)
                else:
                    action_qualified.append(item)
            else:
                action_qualified.append(item)
        action = action_qualified

        sentence = None

        if 'walk' in action[0]:
            sentence = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_table' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'walk_table' in action[0]:
            sentence = 'a robot walks to a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'grasp_plate' in action[0]:
            sentence = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'walk_sink' in action[0]:
            sentence = 'a robot walks to a ' + action[2] + ' in ' + action[4] + ' room.'

        if 'place_plate' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' in ' + action[3] + ' room.'

        if sentence is None:
            print('Cannot find corresponding action.')
        else:
            return sentence

    if task_id == 10:
        action_qualified = []
        for index in range(len(action)):
            item = action[index]
            if index >= 1:
                if '_' in item:
                    item = item[:-2]
                    action_qualified.append(item)
                else:
                    action_qualified.append(item)
            else:
                action_qualified.append(item)
        action = action_qualified

        sentence = None

        if 'walk' in action[0]:
            sentence = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_coke' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'grasp_coke' in action[0]:
            sentence = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_glass' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'pour_coke' in action[0]:
            sentence = 'a robot pours ' + action[2] + ' into ' + action[3] + ' in ' + action[4] + ' room.'

        if 'move_glass' in action[0]:
            sentence = 'a robot moves a ' + action[2] + ' in ' + action[3] + ' room' + ' near a table in ' + action[4] + ' room.'

        if 'place_glass' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' on a table in ' + action[4] + ' room.'

        if sentence is None:
            print('Cannot find corresponding action.')
        else:
            return sentence

    if task_id == 11:
        action_qualified = []
        for index in range(len(action)):
            item = action[index]
            if index >= 1:
                if '_' in item:
                    item = item[:-2]
                    action_qualified.append(item)
                else:
                    action_qualified.append(item)
            else:
                action_qualified.append(item)
        action = action_qualified

        sentence = None

        if 'walk' in action[0]:
            sentence = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_table' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'walk_table' in action[0]:
            sentence = 'a robot walks to a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_chair' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'pull_chair' in action[0]:
            sentence = 'a robot pulls up a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_burger' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'grasp_burger' in action[0]:
            sentence = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'find_plate' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'place_burger' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' on a plate in ' + action[4] + ' room.'

        if 'find_fork' in action[0]:
            sentence = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'

        if 'place_fork' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' on a plate in ' + action[3] + ' room.'

        if 'move_plate' in action[0]:
            sentence = 'a robot moves a ' + action[4] + ' in ' + action[5] + ' room on a table ' + ' in ' + action[7] + ' room.'

        if 'place_plate' in action[0]:
            sentence = 'a robot places a ' + action[2] + ' on a table ' + ' in ' + action[4] + ' room.'

        if sentence is None:
            print('Cannot find corresponding action.')
        else:
            return sentence
# test
# print(translator(['walk', 'rob1', 'dining', 'kitchen']))

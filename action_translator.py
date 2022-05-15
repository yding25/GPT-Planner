def action_translator(action, task_id):
    def process(action):
        # ------------------------------------------
        # remove '_X'; e.g., vacuum_1 -> vacuum
        # ------------------------------------------
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
        return action_qualified

    if task_id == 1:
        action = process(action)  # process action
        # ------------------------------------------
        # translate pddl language into natural language
        # ------------------------------------------
        sentence_completed = None
        sentence_simplified = None
        if 'walk' in action[0]:
            sentence_completed = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'

        if 'grasp_vacuum' in action[0]:
            sentence_completed = 'a robot grasps a ' + action[2] + ' in a ' + action[3] + ' room.'
            sentence_simplified = 'a robot grasps a ' + action[2] + '.'

        if 'find_table' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in a ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'plug_vacuum' == action[0]:
            sentence_completed = 'a robot plugs a ' + action[2] + ' using ' + action[3] + ' in a ' + action[4] + ' room.'
            sentence_simplified = 'a robot plugs a ' + action[2] + ' using ' + action[3] + '.'

        if 'turnon_vacuum' in action[0]:
            sentence_completed = 'a robot turns on a ' + action[2] + ' in a ' + action[3] + ' room.'
            sentence_simplified = 'a robot turns on a ' + action[2] + '.'

        if 'clean_area' in action[0]:
            sentence_completed = 'a robot cleans the area beside a ' + action[3] + ' using ' + action[2] + ' in a ' + action[4] + ' room.'
            sentence_simplified = 'a robot cleans the area beside a ' + action[3] + ' using ' + action[2] + '.'

        if 'turnoff_vacuum' in action[0]:
            sentence_completed = 'a robot turns off a ' + action[2] + 'in a ' + action[3] + ' room' + ' after the floor is clean.'
            sentence_simplified = 'a robot turns off a ' + action[2] + '.'

        if 'unplug_vacuum' == action[0]:
            sentence_completed = 'a robot unplugs a ' + action[2] + ' in a ' + action[3] + ' room.'
            sentence_simplified = 'a robot unplugs a ' + action[2] + '.'

        if sentence_completed is None:
            print('Error: not find corresponding action.')
        else:
            return sentence_completed, sentence_simplified

    if task_id == 4:
        action = process(action)  # process action
        # ------------------------------------------
        # translate pddl language into natural language
        # ------------------------------------------
        sentence_completed = None
        sentence_simplified = None
        if 'walk' in action[0]:
            sentence_completed = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks from a ' + action[2] + ' room to a ' + action[3] + ' room.'

        if 'find_faucet' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'turnon_faucet' in action[0]:
            sentence_completed = 'a robot turns on a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot turns on a ' + action[2] + '.'

        if 'find_cup' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'hold_cup' in action[0]:
            sentence_completed = 'a robot holds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot holds a ' + action[2] + '.'

        if 'fill_cup' in action[0]:
            sentence_completed = 'a robot fills a ' + action[2] + ' with water from ' + action[3] + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot fills a ' + action[2] + ' with water from ' + action[3] + '.'

        if 'move_cup' in action[0]:
            sentence_completed = 'a robot moves a ' + action[2] + ' from ' + action[3] + ' room to ' + action[4] + ' room.'
            sentence_simplified = 'a robot moves a ' + action[2] + '.'

        if 'place_cup' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' on ' + action[3] + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + ' on ' + action[3] + '.'

        if 'turnoff_faucet' in action[0]:
            sentence_completed = 'a robot turns off a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot turns off a ' + action[2] + '.'

        if sentence_completed is None:
            print('Error: not find corresponding action.')
        else:
            return sentence_completed, sentence_simplified

    if task_id == 6:
        action = process(action)  # process action
        # ------------------------------------------
        # translate pddl language into natural language
        # ------------------------------------------
        sentence_completed = None
        sentence_simplified = None
        if 'walk' in action[0]:
            sentence_completed = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_cupboard' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'open_cupboard' in action[0]:
            sentence_completed = 'a robot opens a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot opens a ' + action[2] + '.'

        if 'close_cupboard' in action[0]:
            sentence_completed = 'a robot closes a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot closes a ' + action[2] + '.'

        if 'find_table' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'find_plate' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'takeout_plate' in action[0]:
            sentence_completed = 'a robot takes out a ' + action[2] + ' from a ' + action[3] + '.'
            sentence_simplified = 'a robot takes out a ' + action[2] + ' from a ' + action[3] + '.'

        if 'move_plate' in action[0]:
            sentence_completed = 'a robot moves a ' + action[2] + ' from ' + action[3] + ' room to ' + action[4] + ' room.'
            sentence_simplified = 'a robot moves a ' + action[2] + '.'

        if 'place_plate' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' on ' + action[3] + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + ' on ' + action[3] + '.'

        if 'find_fork' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'takeout_fork' in action[0]:
            sentence_completed = 'a robot takes out a ' + action[2] + ' from a ' + action[3] + '.'
            sentence_simplified = 'a robot takes out a ' + action[2] + ' from a ' + action[3] + '.'

        if 'move_fork' in action[0]:
            sentence_completed = 'a robot moves a ' + action[2] + ' from ' + action[3] + ' room to ' + action[4] + ' room.'
            sentence_simplified = 'a robot moves a ' + action[2] + '.'

        if 'place_fork' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' on ' + action[3] + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + ' on ' + action[3] + '.'

        if sentence_completed is None:
            print('Cannot find corresponding action.')
        else:
            return sentence_completed, sentence_simplified

    if task_id == 9:
        action = process(action)  # process action
        # ------------------------------------------
        # translate pddl language into natural language
        # ------------------------------------------
        sentence_completed = None
        sentence_simplified = None
        if 'walk' in action[0]:
            sentence_completed = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_table' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'walk_table' in action[0]:
            sentence_completed = 'a robot walks to a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks to a ' + action[2] + '.'

        if 'grasp_plate' in action[0]:
            sentence_completed = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot grasps a ' + action[2] + '.'

        if 'walk_sink' in action[0]:
            sentence_completed = 'a robot walks to a ' + action[2] + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot walks to a ' + action[2] + '.'

        if 'place_plate' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + '.'

        if sentence_completed is None:
            print('Cannot find corresponding action.')
        else:
            return sentence_completed, sentence_simplified

    if task_id == 10:
        action = process(action)  # process action
        # ------------------------------------------
        # translate pddl language into natural language
        # ------------------------------------------
        sentence_completed = None
        sentence_simplified = None
        if 'walk' in action[0]:
            sentence_completed = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_glass' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'grasp_glass' in action[0]:
            sentence_completed = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot grasps a ' + action[2] + '.'

        if 'move_glass' in action[0]:
            sentence_completed = 'a robot moves a ' + action[2] + ' in ' + action[3] + ' room' + ' near a table in ' + action[4] + ' room.'
            sentence_simplified = 'a robot moves a ' + action[2] + ' near a table.'

        if 'place_glass' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' on a table in ' + action[4] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + ' on a table.'

        if 'find_soda' in action[0]:
            sentence_completed = 'a robot finds a bottle of ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a bottle of ' + action[2] + '.'

        if 'grasp_soda' in action[0]:
            sentence_completed = 'a robot grasps a bottle of ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot grasps a bottle of ' + action[2] + '.'

        if 'move_soda' in action[0]:
            sentence_completed = 'a robot moves a bottle of ' + action[2] + ' in ' + action[3] + ' room' + ' near a glass in ' + action[4] + ' room.'
            sentence_simplified = 'a robot moves a bottle of ' + action[2] + ' near a glass.'

        if 'pour_soda' in action[0]:
            sentence_completed = 'a robot pours a bottle of ' + action[2] + ' into ' + action[3] + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot pours a bottle of ' + action[2] + ' into ' + action[3] + '.'

        if sentence_completed is None:
            print('Cannot find corresponding action.')
        else:
            return sentence_completed, sentence_simplified

    if task_id == 11:
        action = process(action)  # process action
        # ------------------------------------------
        # translate pddl language into natural language
        # ------------------------------------------
        sentence_completed = None
        sentence_simplified = None
        if 'walk' in action[0]:
            sentence_completed = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks ' + 'from ' + action[2] + ' room to ' + action[3] + ' room.'

        if 'find_table' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'walk_table' in action[0]:
            sentence_completed = 'a robot walks to a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot walks to a ' + action[2] + '.'

        if 'find_chair' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'pull_chair' in action[0]:
            sentence_completed = 'a robot pulls up a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot pulls up a ' + action[2] + '.'

        if 'find_plate' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'grasp_plate' in action[0]:
            sentence_completed = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot grasps a ' + action[2] + '.'

        if 'move_plate' in action[0]:
            sentence_completed = 'a robot moves a ' + action[2] + ' in ' + action[3] + ' room near a ' + action[4] + ' in ' + action[5] + ' room.'
            sentence_simplified = 'a robot moves a ' + action[2] + ' near a table.'

        if 'place_plate' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' on a table ' + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + ' on a table.'

        if 'find_burger' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'grasp_burger' in action[0]:
            sentence_completed = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot grasps a ' + action[2] + '.'

        if 'move_burger' in action[0]:
            sentence_completed = 'a robot moves a ' + action[2] + ' in ' + action[3] + ' room near a ' + action[4] + ' in ' + action[5] + ' room.'
            sentence_simplified = 'a robot moves a ' + action[4] + ' near a ' + action[3] + '.'

        if 'place_burger' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' on a ' + action[3] + ' in ' + action[4] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + ' on a plate.'

        if 'find_fork' in action[0]:
            sentence_completed = 'a robot finds a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot finds a ' + action[2] + '.'

        if 'grasp_fork' in action[0]:
            sentence_completed = 'a robot grasps a ' + action[2] + ' in ' + action[3] + ' room.'
            sentence_simplified = 'a robot grasps a ' + action[2] + '.'

        if 'move_fork' in action[0]:
            sentence_completed = 'a robot moves a ' + action[2] + ' in ' + action[3] + ' room near a ' + action[4] + ' in ' + action[5] + ' room.'
            sentence_simplified = 'a robot moves a ' + action[4] + ' near a plate.'

        if 'place_fork' in action[0]:
            sentence_completed = 'a robot places a ' + action[2] + ' on a plate in ' + action[3] + ' room.'
            sentence_simplified = 'a robot places a ' + action[2] + ' on a plate.'

        if sentence_completed is None:
            print('Cannot find corresponding action.')
        else:
            return sentence_completed, sentence_simplified
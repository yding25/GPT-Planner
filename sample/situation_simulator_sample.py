import numpy as np
from utility import predicate_generator


def situation_simulator(task_id):
    if task_id == 1:
        group1 = 'there is a power outage.'
        opp_group1 = 'power available.'
        group1_object = 'power'
        group1_prob = 28 / 93.
        group1_actions = ['find_table', 'plug_vacuum', 'turnon_vacuum', 'clean_table']
        group1_action_prob = [1 / 28., 8 / 28., 16 / 28., 3 / 28.]

        group2 = 'the vacuum is not working.'
        opp_group2 = 'the vacuum work.'
        group2_object = 'vacuum'
        group2_prob = 12 / 93.
        group2_actions = ['takeout_vacuum', 'turnon_vacuum', 'clean_table']
        group2_action_prob = [2 / 12., 9/ 12., 1 / 12.]

        group3 = 'the vacuum is missing.'
        opp_group3 = 'the vacuum found.'
        group3_object = 'vacuum'
        group3_prob = 10 / 93.
        group3_actions = ['takeout_vacuum']
        group3_action_prob = [10 / 10.]

        group4 = 'the vacuum cannot turn on.'
        opp_group4 = 'the vacuum turning on.'
        group4_object = 'vacuum'
        group4_prob = 10 / 93.
        group4_actions = ['takeout_vacuum']
        group4_action_prob = [10 / 10.]

        group5 = 'the vacuum plug is damaged.'
        opp_group5 = 'the vacuum plug good to use.'
        group5_object = 'vacuum'
        group5_prob = 7 / 93.
        group5_actions = ['find_table', 'plug_vacuum', 'clean_table']
        group5_action_prob = [1 / 7., 5/ 7., 1/ 7.]

        group6 = 'the outlet is missing.'
        opp_group6 = 'outlet found.'
        group6_object = 'outlet'
        group6_prob = 4 / 93.
        group6_actions = ['plug_vacuum']
        group6_action_prob = [4 / 4.]

        group7 = 'the vacuum is not plugged.'
        opp_group7 = 'the vacuum plugged.'
        group7_object = 'vacuum'
        group7_prob = 3 / 93.
        group7_actions = ['plug_vacuum', 'clean_table']
        group7_action_prob = [2 / 3., 1 / 3.]

        group8 = 'the vacuum canister is full.'
        opp_group8 = 'the vacuum canister empty.'
        group8_object = 'canister'
        group8_prob = 3 / 93.
        group8_actions = ['takeout_vacuum', 'find_table', 'clean_table']
        group8_action_prob = [1 / 3., 1 / 3., 1 / 3.]

        group9 = 'the vacuum power cord is too short.'
        opp_group9 = 'the vacuum power cord long.'
        group9_object = 'power cord'
        group9_prob = 2 / 93.
        group9_actions = ['plug_vacuum']
        group9_action_prob = [ 2 / 2.]

        group10 = 'the robot cannot reach the vacuum.'
        opp_group10 = 'the robot reaching the vacuum.'
        group10_object = 'robot'
        group10_prob = 2 / 93.
        group10_actions = ['takeout_vacuum', 'clean_table']
        group10_action_prob = [1 / 2., 1 / 2.]

        group11 = 'the plug is missing.'
        opp_group11 = 'the plug is found.'
        group11_object = 'plug'
        group11_prob = 2 / 93.
        group11_actions = ['plug_vacuum']
        group11_action_prob = [2 / 2.]

        group12 = 'the vacuum switch is not working.'
        opp_group12 = 'the vacuum switch working.'
        group12_object = 'vacuum switch'
        group12_prob = 2 / 93.
        group12_actions = ['turnon_vacuum']
        group12_action_prob = [1 / 1.]

        group13 = 'the vacuum power cord is broken.'
        opp_group13 = 'the vacuum power cord good.'
        group13_object = 'power cord'
        group13_prob = 1 / 93.
        group13_actions = ['plug_vacuum']
        group13_action_prob = [1 / 1.]

        group14 = 'the vacuum is battery powered and does not need plug in.'
        opp_group14 = 'the plug needed.'
        group14_object = 'plug'
        group14_prob = 1 / 93.
        group14_actions = ['plug_vacuum']
        group14_action_prob = [1 / 1.]

        group15 = 'the table is very clean.'
        opp_group15 = 'the table .....'
        group15_object = 'table'
        group15_prob = 1 / 93.
        group15_actions = ['clean_table']
        group15_action_prob = [1 / 1.]

        group16 = 'the table is too dirty.'
        opp_group16 = 'the table clean.'
        group16_object = 'table'
        group16_prob = 1 / 93.
        group16_actions = ['clean_table']
        group16_action_prob = [1 / 1.]

        group17 = 'the robot slips and falls.'
        opp_group17 = 'the robot standing.'
        group17_object = 'robot'
        group17_prob = 1 / 93.
        group17_actions = ['find_table']
        group17_action_prob = [1 / 1.]

        group18 = 'the robot drops the vacuum.'
        opp_group18 = 'the robot picking up vacuum.'
        group18_object = 'robot'
        group18_prob = 1 / 93.
        group18_actions = ['takeout_vacuum']
        group18_action_prob = [1 / 1.]

        group19 = 'the plug is damaged.'
        opp_group19 = 'the plug undamaged.'
        group19_object = 'plug'
        group19_prob = 1 / 93.
        group19_actions = ['turnon_vacuum']
        group19_action_prob = [1 / 1.]

        group20 = 'the outlet is broken.'
        opp_group20 = 'the outlet good.'
        group20_object = 'outlet'
        group20_prob = 1 / 93.
        group20_actions = ['plug_vacuum']
        group20_action_prob = [1 / 1.]

        # ------------------------------------------
        # random select
        # ------------------------------------------
        groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12,
                  group13, group14, group15, group16, group17, group18, group19, group20]
        opp_groups = [opp_group1, opp_group2, opp_group3, opp_group4, opp_group5, opp_group6, opp_group7, opp_group8,
                      opp_group9, opp_group10, opp_group11, opp_group12, opp_group13, opp_group14, opp_group15,
                      opp_group16, opp_group17, opp_group18, opp_group19, opp_group20]
        group_objects = [group1_object, group2_object, group3_object, group4_object, group5_object, group6_object,
                         group7_object, group8_object, group9_object, group10_object, group11_object, group12_object,
                         group13_object, group14_object, group15_object, group16_object, group17_object, group18_object,
                         group19_object, group20_object]
        group_probs = np.array(
            [group1_prob, group2_prob, group3_prob, group4_prob, group5_prob, group6_prob, group7_prob,
             group8_prob, group9_prob, group10_prob, group11_prob, group12_prob, group13_prob, group14_prob,
             group15_prob, group16_prob, group17_prob, group18_prob, group19_prob, group20_prob])
        group_actions = [group1_actions, group2_actions, group3_actions, group4_actions, group5_actions,
                         group6_actions, group7_actions, group8_actions, group9_actions, group10_actions,
                         group11_actions,
                         group12_actions, group13_actions, group14_actions, group15_actions, group16_actions,
                         group17_actions, group18_actions, group19_actions, group20_actions]
        group_action_probs = [group1_action_prob, group2_action_prob, group3_action_prob, group4_action_prob,
                              group5_action_prob,
                              group6_action_prob, group7_action_prob, group8_action_prob, group9_action_prob,
                              group10_action_prob,
                              group11_action_prob, group12_action_prob,
                              group13_action_prob, group14_action_prob, group15_action_prob, group16_action_prob,
                              group17_action_prob, group18_action_prob, group19_action_prob, group20_action_prob]
        # select group index
        group_index = np.random.choice(list(range(0, 20)), p=group_probs)

        # ------------------------------------------
        # test
        # group_index = 1
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action, group_index

    if task_id == 4:
        group1 = 'a cup is broken.'
        opp_group1 = 'a cup not broken.'
        group1_object = 'cup'
        group1_prob = 23 / 95.
        group1_actions = ['find_cup', 'hold_cup', 'fill_cup']
        group1_action_prob = [1 / 23., 16 / 23., 6 / 23.]

        group2 = 'a faucet has no water.'
        opp_group2 = 'a faucet have water.'
        group2_object = 'faucet'
        group2_prob = 23 / 95.
        group2_actions = ['walk', 'turnon_faucet', 'find_cup', 'find_cup', 'fill_cup']
        group2_action_prob = [1 / 23., 11 / 23., 2 / 23., 1 / 23., 8 / 23.]

        group3 = 'a cup is dirty.'
        opp_group3 = 'a cup clean.'
        group3_object = 'cup'
        group3_prob = 14 / 95.
        group3_actions = ['find_cup', 'hold_cup']
        group3_action_prob = [13 / 14., 1 / 14.]

        group4 = 'a cup is missing.'
        opp_group4 = 'a cup found.'
        group4_object = 'cup'
        group4_prob = 10 / 95.
        group4_actions = ['find_cup', 'hold_cup']
        group4_action_prob = [9 / 10., 1 / 10.]

        group5 = 'water is dirty.'
        opp_group5 = 'water clean.'
        group5_object = 'water'
        group5_prob = 7 / 95.
        group5_actions = ['turnon_faucet', 'find_cup', 'fill_cup', 'place_cup']
        group5_action_prob = [1 / 7., 1 / 7., 3 / 7., 2 / 7.]

        group6 = 'water is hot.'
        opp_group6 = 'water cold.'
        group6_object = 'water'
        group6_prob = 3 / 95.
        group6_actions = ['find_cup', 'fill_cup']
        group6_action_prob = [2 / 3., 1 / 3.]

        group7 = 'a faucet is broken.'
        opp_group7 = 'a faucet not broken.'
        group7_object = 'faucet'
        group7_prob = 3 / 95.
        group7_actions = ['turnon_faucet', 'find_cup', 'place_cup']
        group7_action_prob = [1 / 3., 1 / 3., 1 / 3.]

        group8 = 'a faucet cannot be turned on.'
        opp_group8 = 'a faucet turned on.'
        group8_object = 'faucet'
        group8_prob = 1 / 95.
        group8_actions = ['turnon_faucet']
        group8_action_prob = [1 / 1.]

        # group9 = 'a sink is not found.'
        # opp_group9 = 'a sink found.'
        # group9_object = 'sink'
        # group9_prob = 2 / 95.
        # group9_actions = ['find_faucet']
        # group9_action_prob = [2 / 2.]

        group9 = 'a faucet is not found.'
        opp_group9 = 'a faucet found.'
        group9_object = 'faucet'
        group9_prob = 2 / 95.
        group9_actions = ['find_faucet']
        group9_action_prob = [1 / 1.]

        group10 = 'a faucet is dripping.'
        opp_group10 = 'a faucet not dripping.'
        group10_object = 'faucet'
        group10_prob = 1 / 95.
        group10_actions = ['place_cup']
        group10_action_prob = [1 / 1.]

        group11 = 'a faucet cannot be turned on.'
        opp_group11 = 'a faucet turned on.'
        group11_object = 'faucet'
        group11_prob = 1 / 95.
        group11_actions = ['turnon_faucet']
        group11_action_prob = [1 / 1.]

        group12 = 'a faucet is not found.'
        opp_group12 = 'a faucet found.'
        group12_object = 'faucet'
        group12_prob = 1 / 95.
        group12_actions = ['find_faucet']
        group12_action_prob = [1 / 1.]

        group13 = 'a cup is in the box.'
        opp_group13 = 'a cup took out from the box.'
        group13_object = 'cup'
        group13_prob = 1 / 95.
        group13_actions = ['find_cup']
        group13_action_prob = [1 / 1.]

        group14 = 'water spills on the ground.'
        opp_group14 = 'the ground dry.'
        group14_object = 'water'
        group14_prob = 1 / 95.
        group14_actions = ['fill_cup']
        group14_action_prob = [1 / 1.]

        group15 = 'a cup is not full.'
        opp_group15 = 'a cup is full.'
        group15_object = 'cup'
        group15_prob = 2 / 95.
        group15_actions = ['fill_cup', 'place_cup']
        group15_action_prob = [1 / 2., 1 / 2.]

        group16 = 'water is drunk by others.'
        opp_group16 = 'water not drunk by others.'
        group16_object = 'water'
        group16_prob = 1 / 95.
        group16_actions = ['place_cup']
        group16_action_prob = [1 / 1.]

        group17 = 'a cup full of water falls down.'
        opp_group17 = 'a cup full of water not fall down.'
        group17_object = 'cup'
        group17_prob = 1 / 95.
        group17_actions = ['place_cup']
        group17_action_prob = [1 / 1.]

        # ------------------------------------------
        # random select
        # ------------------------------------------
        groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12,
                  group13, group14, group15, group16, group17]
        opp_groups = [opp_group1, opp_group2, opp_group3, opp_group4, opp_group5, opp_group6, opp_group7, opp_group8,
                      opp_group9, opp_group10, opp_group11, opp_group12, opp_group13, opp_group14, opp_group15, opp_group16, opp_group17]
        group_objects = [group1_object, group2_object, group3_object, group4_object, group5_object, group6_object, group7_object, group8_object, group9_object, group10_object, group11_object, group12_object,
                  group13_object, group14_object, group15_object, group16_object, group17_object]
        group_probs = np.array(
            [group1_prob, group2_prob, group3_prob, group4_prob, group5_prob, group6_prob, group7_prob,
             group8_prob, group9_prob, group10_prob, group11_prob, group12_prob, group13_prob, group14_prob,
             group15_prob, group16_prob, group17_prob])
        group_actions = [group1_actions, group2_actions, group3_actions, group4_actions, group5_actions,
                       group6_actions, group7_actions, group8_actions, group9_actions, group10_actions, group11_actions,
                       group12_actions, group13_actions, group14_actions, group15_actions, group16_actions, group17_actions]
        group_action_probs = [group1_action_prob, group2_action_prob, group3_action_prob, group4_action_prob, group5_action_prob,
                            group6_action_prob, group7_action_prob, group8_action_prob, group9_action_prob, group10_action_prob,
                            group11_action_prob, group12_action_prob,
                            group13_action_prob, group14_action_prob, group15_action_prob, group16_action_prob,
                            group17_action_prob]
        # select group index
        group_index = np.random.choice(list(range(0, 17)), p=group_probs)

        # ------------------------------------------
        # test
        # group_index = 1
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action, group_index

    if task_id == 6:
        group1 = 'a plate is broken.'
        opp_group1 = 'a plate not broken.'
        group1_object = 'plate'
        group1_prob = 21 / 92.
        group1_actions = ['walk', 'open_cupboard', 'find_plate', 'takeout_plate', 'find_table', 'place_plate']
        group1_action_prob = [2 / 21., 1 / 21., 1 / 21., 7/21., 2/21, 8/21]

        group2 = 'a plate is not found.'
        opp_group2 = 'a plate found.'
        group2_object = 'plate'
        group2_prob = 13 / 92.
        group2_actions = ['find_cupboard', 'find_plate', 'place_fork', 'takeout_plate']
        group2_action_prob = [2 / 13., 9 / 13., 1 / 13., 1 / 13.]

        group3 = 'a plate is dirty.'
        opp_group3 = 'a plate clean.'
        group3_object = 'plate'
        group3_prob = 12 / 92.
        group3_actions = ['find_plate', 'takeout_plate', 'place_plate']
        group3_action_prob = [4 / 12., 4 / 12., 4 / 12.]

        group4 = 'a fork is dirty.'
        opp_group4 = 'a fork dirty.'
        group4_object = 'fork'
        group4_prob = 8 / 92.
        group4_actions = ['find_fork', 'takeout_fork', 'place_fork']
        group4_action_prob = [5 / 8., 2 / 8., 1 / 8.]

        group5 = 'a fork is not found.'
        opp_group5 = 'fork found.'
        group5_object = 'fork'
        group5_prob = 7 / 92.
        group5_actions = ['find_fork', 'takeout_fork']
        group5_action_prob = [6 / 7., 1 / 7.]

        group6 = 'a table is dirty.'
        opp_group6 = 'a table clean.'
        group6_object = 'table'
        group6_prob = 6 / 92.
        group6_actions = ['find_table', 'place_plate']
        group6_action_prob = [2 / 6., 4 / 6.]

        group7 = 'a table is not found.'
        opp_group7 = 'table found.'
        group7_object = 'table'
        group7_prob = 4 / 92.
        group7_actions = ['find_plate', 'takeout_plate', 'place_plate']
        group7_action_prob = [2 / 4., 1 / 4., 1 / 4.]

        group8 = 'a cupboard cannot open.'
        opp_group8 = 'a cupboard open.'
        group8_object = 'cupboard'
        group8_prob = 4 / 92.
        group8_actions = ['open_cupboard']
        group8_action_prob = [4 / 4.]

        group9 = 'a plate falls on the ground.'
        opp_group9 = 'a plate not fell on the ground.'
        group9_object = 'plate'
        group9_prob = 4 / 92.
        group9_actions = ['takeout_plate', 'find_table', 'place_plate']
        group9_action_prob = [2 / 4., 1 / 4., 1 / 4.]

        group10 = 'a table does not have enough space.'
        opp_group10 = 'a table is big enough.'
        group10_object = 'table'
        group10_prob = 4 / 92.
        group10_actions = ['place_plate', 'place_fork']
        group10_action_prob = [2 / 4., 2 / 4.]

        group11 = 'a fork falls on the ground.'
        opp_group11 = 'a fork not fell on the ground.'
        group11_object = 'fork'
        group11_prob = 3 / 92.
        group11_actions = ['find_fork', 'takeout_fork', 'place_fork']
        group11_action_prob = [1 / 3., 1 / 3., 1 / 3.]

        group12 = 'a cupboard has some mites.'
        opp_group12 = 'a cupboard not have mites.'
        group12_object = 'cupboard'
        group12_prob = 1 / 92.
        group12_actions = ['open_cupboard']
        group12_action_prob = [1 / 1.]

        group13 = 'a cupboard is broken.'
        opp_group13 = 'a cupboard not broken.'
        group13_object = 'cupboard'
        group13_prob = 1 / 92.
        group13_actions = ['open_cupboard']
        group13_action_prob = [1 / 1.]

        group14 = 'a fork is already on the table.'
        opp_group14 = 'a fork not on the table.'
        group14_object = 'fork'
        group14_prob = 1 / 92.
        group14_actions = ['find_fork']
        group14_action_prob = [1 / 1.]

        group15 = 'a fork is broken.'
        opp_group15 = 'a fork broken.'
        group15_object = 'fork'
        group15_prob = 1 / 92.
        group15_actions = ['find_fork']
        group15_action_prob = [1 / 1.]

        group16 = 'a table is broken.'
        opp_group16 = 'a table broken.'
        group16_object = 'table'
        group16_prob = 1 / 92.
        group16_actions = ['find_table']
        group16_action_prob = [1 / 1.]

        group17 = 'there are some obstacles and robot cannot move to the target area.'
        opp_group17 = 'there are no obstacles.'
        group17_object = 'obstacle'
        group17_prob = 1 / 92.
        group17_actions = ['walk']
        group17_action_prob = [1 / 1.]

        # ------------------------------------------
        # random select
        # ------------------------------------------
        groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12,
                  group13, group14, group15, group16, group17]
        opp_groups = [opp_group1, opp_group2, opp_group3, opp_group4, opp_group5, opp_group6, opp_group7, opp_group8,
                      opp_group9, opp_group10, opp_group11, opp_group12, opp_group13, opp_group14, opp_group15, opp_group16, opp_group17]
        group_objects = [group1_object, group2_object, group3_object, group4_object, group5_object, group6_object, group7_object, group8_object, group9_object, group10_object, group11_object, group12_object,
                  group13_object, group14_object, group15_object, group16_object, group17_object]
        group_probs = np.array(
            [group1_prob, group2_prob, group3_prob, group4_prob, group5_prob, group6_prob, group7_prob,
             group8_prob, group9_prob, group10_prob, group11_prob, group12_prob, group13_prob, group14_prob,
             group15_prob, group16_prob, group17_prob])
        group_actions = [group1_actions, group2_actions, group3_actions, group4_actions, group5_actions,
                       group6_actions, group7_actions, group8_actions, group9_actions, group10_actions, group11_actions,
                       group12_actions, group13_actions, group14_actions, group15_actions, group16_actions, group17_actions]
        group_action_probs = [group1_action_prob, group2_action_prob, group3_action_prob, group4_action_prob, group5_action_prob,
                            group6_action_prob, group7_action_prob, group8_action_prob, group9_action_prob, group10_action_prob,
                            group11_action_prob, group12_action_prob,
                            group13_action_prob, group14_action_prob, group15_action_prob, group16_action_prob,
                            group17_action_prob]
        # select group index
        group_index = np.random.choice(list(range(0, 17)), p=group_probs)

        # ------------------------------------------
        # test
        # group_index = 0
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action, group_index

    if task_id == 9:
        group1 = 'the sink is full.'
        opp_group1 = 'the sink empty'
        group1_object = 'sink'
        group1_prob = 24 / 95.
        group1_actions = ['find_table', 'walk_table', 'grasp_plate', 'walk_sink', 'place_plate']
        group1_action_prob = [1 / 24., 2/ 24., 9 / 24., 11 / 24., 1/ 24.]

        group2 = 'the plate is broken.'
        opp_group2 = 'the plate unbroken.'
        group2_object = 'plate'
        group2_prob = 17 / 95.
        group2_actions = ['grasp_plate', 'walk_sink', 'place_plate']
        group2_action_prob = [6 / 17., 5 / 17., 6 / 17.]

        group3 = 'the plate is clean.'
        opp_group3 = 'the plate.......'
        group3_object = 'plate'
        group3_prob = 11 / 95.
        group3_actions = ['grasp_plate', 'place_plate']
        group3_action_prob = [8 / 11., 3 / 11.]

        group4 = 'the dirty plate is missing on table.'
        opp_group4 = '.......'
        group4_object = 'plate'
        group4_prob = 11 / 95.
        group4_actions = ['grasp_plate', 'place_plate']
        group4_action_prob = [8 / 11., 3 / 11.]

        group5 = 'the plate is dropped.'
        opp_group5 = 'the plate not dropped.'
        group5_object = 'plate'
        group5_prob = 9 / 95.
        group5_actions = ['grasp_plate', 'walk_sink', 'place_plate']
        group5_action_prob = [6 / 9., 1/ 9., 2 / 9.]

        group6 = 'the plate is missing.'
        opp_group6 = 'the plate found.'
        group6_object = 'plate'
        group6_prob = 6 / 95.
        group6_actions = ['grasp_plate', 'walk_sink']
        group6_action_prob = [5 / 6., 1 / 6.]

        group7 = 'a person dropped and got injured.'
        opp_group7 = 'a person good.'
        group7_object = 'person'
        group7_prob = 4 / 95.
        group7_actions = ['walk', 'grasp_plate', 'walk_sink']
        group7_action_prob = [1 / 4., 1 / 4., 2 / 4.]

        group8 = 'the table is missing.'
        opp_group8 = 'the table found.'
        group8_object = 'table'
        group8_prob = 2 / 95.
        group8_actions = ['walk_table']
        group8_action_prob = [2 / 2.]

        group9 = 'the sink is too dirty.'
        opp_group9 = 'the sink clean.'
        group9_object = 'sink'
        group9_prob = 2 / 95.
        group9_actions = ['walk_sink']
        group9_action_prob = [2 / 2.]

        group10 = 'there is no water in sink.'
        opp_group10 = 'water in the sink.'
        group10_object = 'water'
        group10_prob = 1 / 95.
        group10_actions = ['walk_sink']
        group10_action_prob = [1 / 1.]

        group11 = 'the table is dirty.'
        opp_group11 = 'the table clean.'
        group11_object = 'table'
        group11_prob = 1 / 95.
        group11_actions = ['walk_table']
        group11_action_prob = [1 / 1.]

        group12 = 'the table is broken.'
        opp_group12 = 'the table good.'
        group12_object = 'table'
        group12_prob = 1 / 95.
        group12_actions = ['walk_table']
        group12_action_prob = [1 / 1.]

        group13 = 'the sink cannot be found.'
        opp_group13 = 'the sink found.'
        group13_object = 'sink'
        group13_prob = 1 / 95.
        group13_actions = ['walk_sink']
        group13_action_prob = [1 / 1.]

        group14 = 'the plate is grabbed by dog.'
        opp_group14 = 'the plate back.'
        group14_object = 'plate'
        group14_prob = 1 / 95.
        group14_actions = ['grasp_plate']
        group14_action_prob = [1 / 1.]

        group15 = 'the door of dinning room is locked.'
        opp_group15 = 'the door open'
        group15_object = 'door'
        group15_prob = 1 / 95.
        group15_actions = ['walk']
        group15_action_prob = [1 / 1.]

        group16 = 'someone has already picked up the dirty plate.'
        opp_group16 = 'someone returning the dirty plate.'
        group16_object = 'plate'
        group16_prob = 1 / 95.
        group16_actions = ['grasp_plate']
        group16_action_prob = [1 / 1.]

        group17 = 'someone has already clean the table.'
        opp_group17 = 'the table dirty.'
        group17_object = 'table'
        group17_prob = 1 / 95.
        group17_actions = ['walk_table']
        group17_action_prob = [1 / 1.]

        group18 = 'people are not finishing food.'
        opp_group18 = 'people finishing food.'
        group18_object = 'food'
        group18_prob = 1 / 95.
        group18_actions = ['walk']
        group18_action_prob = [1 / 1.]

        # ------------------------------------------
        # random select
        # ------------------------------------------
        groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13, group14, group15, group16, group17, group18]
        opp_groups = [opp_group1, opp_group2, opp_group3, opp_group4, opp_group5, opp_group6, opp_group7, opp_group8, opp_group9, opp_group10, opp_group11, opp_group12, opp_group13, opp_group14, opp_group15, opp_group16, opp_group17, opp_group18]
        group_objects = [group1_object, group2_object, group3_object, group4_object, group5_object, group6_object, group7_object, group8_object, group9_object, group10_object, group11_object, group12_object, group13_object, group14_object, group15_object, group16_object, group17_object, group18_object]
        group_probs = np.array([group1_prob, group2_prob, group3_prob, group4_prob, group5_prob, group6_prob, group7_prob, group8_prob, group9_prob, group10_prob, group11_prob, group12_prob, group13_prob, group14_prob, group15_prob, group16_prob, group17_prob, group18_prob])
        group_actions = [group1_actions, group2_actions, group3_actions, group4_actions, group5_actions,
                     group6_actions, group7_actions, group8_actions, group9_actions, group10_actions, group11_actions,
                     group12_actions, group13_actions, group14_actions, group15_actions, group16_actions,
                     group17_actions, group18_actions]
        group_action_probs = [group1_action_prob, group2_action_prob, group3_action_prob, group4_action_prob,
                          group5_action_prob,
                          group6_action_prob, group7_action_prob, group8_action_prob, group9_action_prob,
                          group10_action_prob,
                          group11_action_prob, group12_action_prob,
                          group13_action_prob, group14_action_prob, group15_action_prob, group16_action_prob,
                          group17_action_prob, group18_action_prob]
        # select group index
        group_index = np.random.choice(list(range(0, 18)), p=group_probs)

        # ------------------------------------------
        # test
        # group_index = 1
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action, group_index

    if task_id == 10:
        group1 = 'the coke is not available.'
        opp_group1 = 'the coke available'
        group1_object = 'coke'
        group1_prob = 17 / 93.
        group1_actions = ['find_coke', 'grasp_coke']
        group1_action_prob = [14 / 17., 3 / 17.]

        group2 = 'the glass is broken.'
        opp_group2 = 'the glass good.'
        group2_object = 'glass'
        group2_prob = 11 / 93.
        group2_actions = ['find_glass', 'pour_coke', 'move_glass']
        group2_action_prob = [3 / 11., 5 / 11., 3 / 11.]

        group3 = 'the coke bottle is missing.'
        opp_group3 = 'the coke bottle found.'
        group3_object = 'bottle'
        group3_prob = 11 / 93.
        group3_actions = ['find_coke']
        group3_action_prob = [11 / 11.]

        group4 = 'the glass is dirty.'
        opp_group4 = 'the glass clean.'
        group4_object = 'glass'
        group4_prob = 9 / 93.
        group4_actions = ['find_glass', 'pour_coke', 'move_glass']
        group4_action_prob = [6 / 9., 2 / 9., 1 / 9.]

        group5 = 'the glass falls down.'
        opp_group5 = 'the glass picked up.'
        group5_object = 'glass'
        group5_prob = 8 / 93.
        group5_actions = ['find_glass', 'pour_coke', 'place_glass']
        group5_action_prob = [1 / 8., 1 / 8., 6 / 8.]

        group6 = 'the coke spills.'
        opp_group6 = 'the coke good.'
        group6_object = 'coke'
        group6_prob = 8 / 93.
        group6_actions = ['find_glass', 'pour_coke']
        group6_action_prob = [2 / 8., 6 / 8.]

        group7 = 'the glass is missing.'
        opp_group7 = 'the glass found.'
        group7_object = 'glass'
        group7_prob = 7 / 93.
        group7_actions = ['find_glass']
        group7_action_prob = [7 / 7.]

        group8 = 'the coke is flat.'
        opp_group8 = 'the coke good.'
        group8_object = 'coke'
        group8_prob = 5 / 93.
        group8_actions = ['place_glass']
        group8_action_prob = [5 / 5.]

        group9 = 'the coke bottle cannot open.'
        opp_group9 = 'the coke bottle open.'
        group9_object = 'bottle'
        group9_prob = 4 / 93.
        group9_actions = ['pour_coke']
        group9_action_prob = [4 / 4.]

        group10 = 'the coke bottle is empty.'
        opp_group10 = 'the coke bottle full.'
        group10_object = 'bottle'
        group10_prob = 3 / 93.
        group10_actions = ['find_coke']
        group10_action_prob = [3 / 3.]

        group11 = 'the person has something caught in the throat and cough out the drink.'
        opp_group11 = 'the person good.'
        group11_object = 'person'
        group11_prob = 2 / 93.
        group11_actions = ['place_glass']
        group11_action_prob = [2 / 2.]

        group12 = 'the coke bottle is dropped.'
        opp_group12 = 'the coke bottle picked up.'
        group12_object = 'bottle'
        group12_prob = 2 / 93.
        group12_actions = ['pour_coke']
        group12_action_prob = [2 / 2.]

        group13 = 'the robot cannot recognize the bottle.'
        opp_group13 = 'the robot recognizeing the bottle.'
        group13_object = 'robot'
        group13_prob = 1 / 93.
        group13_actions = ['find_coke']
        group13_action_prob = [1 / 1.]

        group14 = 'the robot cannot recognize the bottle, and take beer out.'
        opp_group14 = '......'
        group14_object = 'robot'
        group14_prob = 1 / 93.
        group14_actions = ['find_coke']
        group14_action_prob = [1 / 1.]

        group15 = 'the person does not like coke.'
        opp_group15 = 'the person liking coke'
        group15_object = 'person'
        group15_prob = 1 / 93.
        group15_actions = ['place_glass']
        group15_action_prob = [1 / 1.]

        group16 = 'the coke bottle is sticky and leaking.'
        opp_group16 = 'the coke bottle clean and good.'
        group16_object = 'bottle'
        group16_prob = 1 / 93.
        group16_actions = ['find_coke']
        group16_action_prob = [1 / 1.]

        group17 = 'the coke bottle is not chill.'
        opp_group17 = 'the coke bottle chilled.'
        group17_object = 'bottle'
        group17_prob = 1 / 93.
        group17_actions = ['grasp_coke']
        group17_action_prob = [1 / 1.]

        group18 = 'the coke bottle is frozen.'
        opp_group18 = 'the coke bottle warm.'
        group18_object = 'bottle'
        group18_prob = 1 / 93.
        group18_actions = ['grasp_coke']
        group18_action_prob = [1 / 1.]

        # ------------------------------------------
        # random select
        # ------------------------------------------
        groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12,
                  group13, group14, group15, group16, group17, group18]
        opp_groups = [opp_group1, opp_group2, opp_group3, opp_group4, opp_group5, opp_group6, opp_group7, opp_group8,
                      opp_group9, opp_group10, opp_group11, opp_group12, opp_group13, opp_group14, opp_group15,
                      opp_group16,
                      opp_group17, opp_group18]
        group_objects = [group1_object, group2_object, group3_object, group4_object, group5_object, group6_object,
                         group7_object, group8_object, group9_object, group10_object, group11_object, group12_object,
                         group13_object, group14_object, group15_object, group16_object, group17_object, group18_object]
        group_probs = np.array(
            [group1_prob, group2_prob, group3_prob, group4_prob, group5_prob, group6_prob, group7_prob,
             group8_prob, group9_prob, group10_prob, group11_prob, group12_prob, group13_prob, group14_prob,
             group15_prob, group16_prob, group17_prob, group18_prob])
        group_actions = [group1_actions, group2_actions, group3_actions, group4_actions, group5_actions,
                         group6_actions, group7_actions, group8_actions, group9_actions, group10_actions,
                         group11_actions,
                         group12_actions, group13_actions, group14_actions, group15_actions, group16_actions,
                         group17_actions, group18_actions]
        group_action_probs = [group1_action_prob, group2_action_prob, group3_action_prob, group4_action_prob,
                              group5_action_prob,
                              group6_action_prob, group7_action_prob, group8_action_prob, group9_action_prob,
                              group10_action_prob,
                              group11_action_prob, group12_action_prob,
                              group13_action_prob, group14_action_prob, group15_action_prob, group16_action_prob,
                              group17_action_prob, group18_action_prob]
        # select group index
        group_index = np.random.choice(list(range(0, 18)), p=group_probs)

        # ------------------------------------------
        # test
        # group_index = 1
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action, group_index

    if task_id == 11:
        group1 = 'the chair is broken.'
        opp_group1 = 'the chair unbroken.'
        group1_object = 'chair'
        group1_prob = 23 / 93.
        group1_actions = ['find_chair', 'pull_chair']
        group1_action_prob = [12 / 23., 11 / 23.]

        group2 = 'the burger is missing.'
        opp_group2 = 'the burger found.'
        group2_object = 'burger'
        group2_prob = 15 / 93.
        group2_actions = ['find_burger', 'grasp_burger', 'find_plate']
        group2_action_prob = [10 / 15., 2 / 15., 3 / 15.]

        group3 = 'the fork is missing.'
        opp_group3 = 'the fork found.'
        group3_object = 'fork'
        group3_prob = 10 / 93.
        group3_actions = ['find_fork']
        group3_action_prob = [10 / 10.]

        group4 = 'the plate is dirty.'
        opp_group4 = 'the plate clean.'
        group4_object = 'plate'
        group4_prob = 5 / 93.
        group4_actions = ['move_plate', 'place_plate']
        group4_action_prob = [3 / 5., 2 / 5.]

        group5 = 'the plate is missing.'
        opp_group5 = 'the plate found.'
        group5_object = 'plate'
        group5_prob = 4 / 93.
        group5_actions = ['find_plate']
        group5_action_prob = [4 / 4.]

        group6 = 'the person falls when sitting down.'
        opp_group6 = 'the person standing.'
        group6_object = 'person'
        group6_prob = 4 / 93.
        group6_actions = ['pull_chair']
        group6_action_prob = [4 / 4.]

        group7 = 'the chair is occupied.'
        opp_group7 = 'the chair available.'
        group7_object = 'chair'
        group7_prob = 4 / 93.
        group7_actions = ['find_chair']
        group7_action_prob = [4 / 4.]

        group8 = 'the fork is dirty.'
        opp_group8 = 'the fork clean.'
        group8_object = 'fork'
        group8_prob = 3 / 93.
        group8_actions = ['find_fork']
        group8_action_prob = [3 / 3.]

        group9 = 'the person has to take out of the burger.'
        opp_group9 = 'the person......'
        group9_object = 'person'
        group9_prob = 2 / 93.
        group9_actions = ['place_plate']
        group9_action_prob = [2 / 2.]

        group10 = 'the burger spills.'
        opp_group10 = 'the burger good.'
        group10_object = 'burger'
        group10_prob = 2 / 93.
        group10_actions = ['place_plate']
        group10_action_prob = [2 / 2.]

        group11 = 'the burger is overcooked.'
        opp_group11 = 'the burger well.'
        group11_object = 'burger'
        group11_prob = 2 / 93.
        group11_actions = ['find_burger']
        group11_action_prob = [2 / 2.]

        group12 = 'the chair is missing.'
        opp_group12 = 'the chair found.'
        group12_object = 'chair'
        group12_prob = 2 / 93.
        group12_actions = ['find_chair']
        group12_action_prob = [2 / 2.]

        group13 = 'the chair is dirty.'
        opp_group13 = 'the chair clean.'
        group13_object = 'chair'
        group13_prob = 2 / 93.
        group13_actions = ['find_chair']
        group13_action_prob = [2 / 2.]

        group14 = 'the utensil is placed already.'
        opp_group14 = 'the utencil not placed in advance.'
        group14_object = 'utencil'
        group14_prob = 1 / 93.
        group14_actions = ['place_plate']
        group14_action_prob = [1 / 1.]

        group15 = 'the table is dirty.'
        opp_group15 = 'the table clean.'
        group15_object = 'table'
        group15_prob = 1 / 93.
        group15_actions = ['find_table']
        group15_action_prob = [1 / 1.]

        group16 = 'the spoon is missing.'
        opp_group16 = 'the spoon found.'
        group16_object = 'spoon'
        group16_prob = 1 / 93.
        group16_actions = ['place_plate']
        group16_action_prob = [1 / 1.]

        group17 = 'the plate is not available.'
        opp_group17 = 'the plate available.'
        group17_object = 'plate'
        group17_prob = 1 / 93.
        group17_actions = ['find_plate']
        group17_action_prob = [1 / 1.]

        group18 = 'the plate is broken.'
        opp_group18 = 'the plate good.'
        group18_object = 'plate'
        group18_prob = 1 / 93.
        group18_actions = ['find_plate']
        group18_action_prob = [1 / 1.]

        group19 = 'the person needs a spoon.'
        opp_group19 = 'the person not needs a spoon.'
        group19_object = 'person'
        group19_prob = 1 / 93.
        group19_actions = ['place_plate']
        group19_action_prob = [1 / 1.]

        group20 = 'the person needs a napkin.'
        opp_group20 = 'the person get a spoon.'
        group20_object = 'person'
        group20_prob = 1 / 93.
        group20_actions = ['']
        group20_action_prob = [1 / 1.]

        group21 = 'the person cannot walk.'
        opp_group21 = 'the person can walk.'
        group21_object = 'person'
        group21_prob = 1 / 93.
        group21_actions = ['']
        group21_action_prob = [1 / 1.]

        group22 = 'the fork is broken.'
        opp_group22 = 'the fork good.'
        group22_object = 'fork'
        group22_prob = 1 / 93.
        group22_actions = ['']
        group22_action_prob = [1 / 1.]

        group23 = 'the burger smells bad.'
        opp_group23 = '.'
        group23_object = 'burger'
        group23_prob = 1 / 93.
        group23_actions = ['']
        group23_action_prob = [1 / 1.]

        group24 = 'the burger is not enough.'
        opp_group24 = 'the burger enough.'
        group24_object = 'burger'
        group24_prob = 1 / 93.
        group24_actions = ['']
        group24_action_prob = [1 / 1.]

        group25 = 'the burger is expired.'
        opp_group25 = 'the burger in good condition.'
        group25_object = 'burger'
        group25_prob = 1 / 93.
        group25_actions = ['']
        group25_action_prob = [1 / 1.]

        group26 = 'the burger is dirty.'
        opp_group26 = 'the burger clean.'
        group26_object = 'burger'
        group26_prob = 1 / 93.
        group26_actions = ['']
        group26_action_prob = [1 / 1.]

        group27 = 'the chair slipped.'
        opp_group27 = 'the chair in good condition.'
        group27_object = 'chair'
        group27_prob = 1 / 93.
        group27_actions = ['']
        group27_action_prob = [1 / 1.]

        group28 = 'the chair is wet.'
        opp_group28 = 'the chair dry.'
        group28_object = 'chair'
        group28_prob = 1 / 93.
        group28_actions = ['']
        group28_action_prob = [1 / 1.]

        # ------------------------------------------
        # random select
        # ------------------------------------------
        groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12,
                  group13, group14, group15, group16, group17, group18, group19, group20, group21, group22, group23,
                  group24, group25, group26, group27, group28]
        opp_groups = [opp_group1, opp_group2, opp_group3, opp_group4, opp_group5, opp_group6, opp_group7, opp_group8,
                      opp_group9, opp_group10, opp_group11, opp_group12, opp_group13, opp_group14, opp_group15,
                      opp_group16, opp_group17, opp_group18, opp_group19, opp_group20, opp_group21, opp_group22,
                      opp_group23, opp_group24, opp_group25, opp_group26, opp_group27, opp_group28]
        group_objects = [group1_object, group2_object, group3_object, group4_object, group5_object, group6_object,
                         group7_object, group8_object, group9_object, group10_object, group11_object, group12_object,
                         group13_object, group14_object, group15_object, group16_object, group17_object, group18_object,
                         group19_object, group20_object, group21_object, group22_object, group23_object,
                         group24_object, group25_object, group26_object, group27_object, group28_object]
        group_probs = np.array(
            [group1_prob, group2_prob, group3_prob, group4_prob, group5_prob, group6_prob, group7_prob,
             group8_prob, group9_prob, group10_prob, group11_prob, group12_prob, group13_prob, group14_prob,
             group15_prob, group16_prob, group17_prob, group18_prob, group19_prob, group20_prob, group21_prob,
             group22_prob, group23_prob, group24_prob, group25_prob, group26_prob, group27_prob, group28_prob])
        group_actions = [group1_actions, group2_actions, group3_actions, group4_actions, group5_actions,
                         group6_actions, group7_actions, group8_actions, group9_actions, group10_actions,
                         group11_actions,
                         group12_actions, group13_actions, group14_actions, group15_actions, group16_actions,
                         group17_actions, group18_actions, group19_actions, group20_actions, group21_actions,
                         group22_actions, group23_actions, group24_actions, group25_actions, group26_actions,
                         group27_actions, group28_actions]
        group_action_probs = [group1_action_prob, group2_action_prob, group3_action_prob, group4_action_prob,
                              group5_action_prob,
                              group6_action_prob, group7_action_prob, group8_action_prob, group9_action_prob,
                              group10_action_prob,
                              group11_action_prob, group12_action_prob,
                              group13_action_prob, group14_action_prob, group15_action_prob, group16_action_prob,
                              group17_action_prob, group18_action_prob, group19_action_prob, group20_action_prob,
                              group21_action_prob, group22_action_prob, group23_action_prob, group24_action_prob,
                              group25_action_prob, group26_action_prob, group27_action_prob, group28_action_prob]
        # select group index
        group_index = np.random.choice(list(range(0, 28)), p=group_probs)

        # ------------------------------------------
        # test
        # group_index = 17
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action, group_index


# sample N situations
task_id = 11
sample_result = []
N = 100
for i in range(N):
    group, opp_group, group_object, group_predicate, group_action, group_index = situation_simulator(task_id)
    sample_result.append(group_index)
print('sample_result:', sample_result)
print('number:', len(sample_result))
# count situations
M = 30
for index in range(M):
    counter = 0
    for item in sample_result:
        if item == index:
            counter += 1
    print('index=%d, counter=%d' %(index, counter))





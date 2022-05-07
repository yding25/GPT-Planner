import numpy as np
from utility_llm import predicate_generator


def situation_simulator(task_id):
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

        group9 = 'a sink is not found.'
        opp_group9 = 'a sink found.'
        group9_object = 'sink'
        group9_prob = 2 / 95.
        group9_actions = ['find_sink']
        group9_action_prob = [2 / 2.]

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
        opp_group14 = 'the ground clean.'
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

        group17 = 'a cup falls down.'
        opp_group17 = 'a cup not fall down.'
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
        group_index = 0
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action

    if task_id == 6:
        group1 = 'a plate is broken.'
        opp_group1 = 'a plate not broken.'
        group1_object = 'plate'
        group1_prob = 21 / 92.
        group1_actions = ['walk', 'open_cupboard', 'find_plate', 'takout_plate', 'find_table', 'place_plate']
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
        # group_index = np.random.choice(list(range(0, 17)), p=group_probs)

        # ------------------------------------------
        # test
        group_index = 0
        # ------------------------------------------

        group = groups[group_index]
        opp_group = opp_groups[group_index]
        group_object = group_objects[group_index]
        group_action = np.random.choice(group_actions[group_index], p=group_action_probs[group_index])
        group_predicate = predicate_generator(group)
        return group, opp_group, group_object, group_predicate, group_action


# test
# task_id = 4
# group, group_predicate, group_action = situation_simulator(task_id)
# print('situation, its predicate, and step:', group, group_predicate, group_action)

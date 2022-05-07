import random


def object_simulator():
    filein = open('dataset/appliances_processed.txt')  # read appliance
    appliance_list = []
    for line in filein.readlines():
        line = line.strip()
        joint_rule = ''
        appliance_list.append(joint_rule.join(line))
    filein.close()
    # print('appliance that robot can operate:', appliance_list)

    filein = open('dataset/utensils_processed.txt')  # read appliance
    utensil_list = []
    for line in filein.readlines():
        line = line.strip()
        joint_rule = ''
        utensil_list.append(joint_rule.join(line))
    filein.close()
    # print('utensil that robot can operate:', utensil_list)

    appliance_selected = (random.sample(appliance_list, int(len(appliance_list) / 2)))
    utensil_selected = (random.sample(utensil_list, int(len(utensil_list) / 2)))

    return appliance_selected, utensil_selected
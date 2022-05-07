# -*- coding: utf-8 -*-
"""
Created on Wed July 28 15:54:15 2021

@author: YanDing
"""
import openai
import numpy as np
from nltk.corpus import stopwords

# -----------------------------------------
# read the 'available_action.json' file
filename1 = 'available_actions.json'
fidin1 = open(filename1, 'r')

# store the extracted object
object_list = []

num_object = 0
for line in fidin1.readlines():
    line = line.strip()
    dataset_action_object = line.split("\"")
    # print(items)
    for action_object in dataset_action_object:
        if len(action_object) > 3:
            # print(action_object)
            items = action_object.split(" ")
            for item in items[1:]:
                if item in list(stopwords.words('english')):
                    continue
                else:
                    if item not in object_list:
                        print(item)
                        object_list.append(item)
                        num_object += 1
                        break
print(num_object)
print(object_list)
np.save('object_list.npy', object_list)

# -----------------------------------------
fidout1 = open('object_in_dining.txt', 'w')
for object in object_list:
    fidout1.write('%s\n' % object)

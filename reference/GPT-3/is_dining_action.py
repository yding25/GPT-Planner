# -*- coding: utf-8 -*-
"""
Created on Wed July 28 15:54:15 2021

@author: YanDing
"""
import openai
import numpy as np


def isdiningaction(action):
    response = openai.Completion.create(
        engine="text-ada-001",
        prompt="predict an action is in the dining domain or not\n\naction: close address_book\ndining domain: "
               "no\n\naction: close after_shave\ndining domain: no\n\naction: cut pancake\ndining domain: "
               "yes\n\naction: drink sauce_pan\ndining domain: yes\n\nclose basket_for_clothes\ndining domain: "
               "no\n\nclose after_shave\ndining domain: no\n\naction: " + action + "\ndining domain:",
        temperature=1.0,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


# -----------------------------------------
f = open('openai_api_key.txt', "r")
key = f.read()
openai.api_key = key
f.close()

# -----------------------------------------
# read the action file
filename1 = '/home/kitrob/Desktop/GPT-Planner/LLM/available_actions.json'
fidin1 = open(filename1, 'r')

# store the extracted action
action_list = []

num_action = 0
for line in fidin1.readlines():
    line = line.strip()
    items = line.split("\"")
    for action in items:
        if len(action) > 3:
            # print(action)
            num_action += 1
            action_list.append(action)
# print(num_action)
# print(action_list)
np.save('action_list.npy', action_list)

# -----------------------------------------
fidout1 = open('action_in_dining.txt', 'w')
action_list_test = action_list[1:500]
for action in action_list_test:
    response = isdiningaction(action)
    # print(response)
    result = response['choices'][0]
    result = result['text']
    print('action and result:', (action, result))
    if 'yes' in result:
        fidout1.write('%s\n' % action)

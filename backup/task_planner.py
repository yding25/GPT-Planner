# generate a task plan
import os
import getpass

user = getpass.getuser()
def task_planner(path_domain, path_problem, name_output):
    address = '/home/' + getpass.getuser() + '/downward/fast-downward.py '
    output_filename = name_output
    command = 'python ' + address + '--alias lama-first ' + '--plan-file ' + output_filename + ' ' + path_domain + ' ' + path_problem
    # print(command)
    os.system(command)
    return '/home/' + user + '/githubBase/GPT-Planner/' + output_filename

import os
import time
import getpass

for repeat in range(2):
    # ------------------------------------------
    # single run
    # ------------------------------------------
    user = getpass.getuser()
    command = 'python /home/' + user + '/GPT-Planner/main.py'
    terminal_output = os.popen(command).readlines()
    # ------------------------------------------
    # create a file to store terminal output
    # ------------------------------------------
    task_id = 11
    fidout = open('results/result_task_' + str(task_id) + '_' + str(round(time.time())) + '.txt', 'w')
    for line in terminal_output:
        fidout.write('%s' % line)
        fidout.flush()
    fidout.close()
    time.sleep(5)
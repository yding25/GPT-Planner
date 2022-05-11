import os
import time
import getpass

for repeat in range(5):
    # ------------------------------------------
    # single run
    # ------------------------------------------
    user = getpass.getuser()
    command = 'python /home/' + user + '/githubBase/GPT-Planner/main.py'
    terminal_output = os.popen(command).readlines()

    # ------------------------------------------
    # create a file to store terminal output
    # ------------------------------------------
    task_id = 11
    situation = 17
    fidout = open('results/result_task_' + str(task_id) + '_situation_' + str(situation) + '_' + str(round(time.time()) - 500000) + '.txt', 'w')
    for line in terminal_output:
        fidout.write('%s' % line)
        fidout.flush()
    fidout.close()
    time.sleep(10)

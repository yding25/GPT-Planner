# GPT-Planner

## Environment
ubuntu (version 16.04, 18.04, and 20.04 have been tested) <br />

## Install GPT-Planner
### step 1: download GPT-Planner
* open terminal
* `cd`
*  `git clone https://github.com/yding25/GPT-Planner.git`
### step 2: install dependencies
* `pip install numpy==1.19.5`
*  `pip install openai==0.8.0`
### step 3: install FastDownward (detailed instruction at https://www.fast-downward.org/ObtainingAndRunningFastDownward)
* `cd GPT-Planner`
* `git clone https://github.com/aibasel/downward.git FastDownward`
* `sudo apt install cmake g++ git make python3`
* `cd FastDownward`
* `python build.py`
* `cd ..`
### step 4: prepare an GPT-3 API key
Here is a brief instruction to obtain a key. 
* `log in https://beta.openai.com/`
* `click the icon ``Personal'' on the top right`
* `click ``view API keys''`
* `click ``+ Create new secret key''`
* `copy the key and paste it in GPT-Planner/dataset/openai_api_key.txt`

## Run GPT-Planner
* change the value of `task_id` (line 19 in `main.py` file) to select an task
```
task_id = 4
task = {
    1: 'cleaning floor',
    4: 'drinking water',
    6: 'setting table',
    9: 'grasping plate',
    10: 'drinking soda',
    11: 'eating dinner'
    }
task_name = task[task_id]
```

* `python main.py`

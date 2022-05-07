### 
domain_1.pddl and problem_1.pddl are a basic case.
There is only one cup in the domain knowledge.

translation into natural language.
Plan: 
a robot walks from dining room to kitchen room.
a robot finds a cup in kitchen room.
a robot finds a faucet in kitchen room.
a robot turns on a faucet in kitchen room.
a robot holds a cup in kitchen room.
a robot fills a cup with water from faucet in kitchen room
a robot moves a cup from kitchen room to dining room.
a robot put a cup on a table in dining room.
a robot walk from dining room to kitchen room.
a robot turns off a faucet in kitchen room.

### 
domain_2.pddl and problem_2.pddl
There is two cup in the domain knowledge.
But there is no constraint.

###
domain_2_c.pddl and problem_2_c.pddl
There is two cup in the domain knowledge.
But there is one constraint obtained from lm.

###
domain_3.pddl and problem_3.pddl
There is one cup and one bowl in the domain knowledge.
But there is one constraint obtained from lm.
Note: there is no feasible plan

###
domain_3_e.pddl and problem_3_e.pddl
There is one cup and one bowl in the domain knowledge.
There is one constraint obtained from lm.
lm find bowl can replace cup.

###
domain_4.pddl and problem_4.pddl
use tool to clean the cup

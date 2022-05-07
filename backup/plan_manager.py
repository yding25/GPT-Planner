def plan_manager(next_step, path_plan):
    fidin = open(path_plan, 'r')
    plan = []
    for line in fidin.readlines():
        line = line.strip()
        line = line[1:-1]
        line = line.split(' ')
        plan.append(line)
    plan = plan[:-1]
    return plan[next_step]

# print(plan_manager(0))

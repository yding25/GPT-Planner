def read_plan(file_path):
    fidin = open(file_path, 'r')
    plan = []
    for line in fidin.readlines():
        line = line.strip()
        line = line[1:-1]
        line = line.split(' ')
        plan.append(line)
    plan = plan[:-1]
    return plan
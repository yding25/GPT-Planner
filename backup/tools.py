def print_file(file_path):
    fidin = open(file_path, 'r')
    print('#----------file content-----------')
    for line in fidin.readlines():
        line = line.strip()
        print(line)
    fidin.close()

def print_list(input_list):
    for item in input_list:
        print('\t', item)


def write_file(file_path, content):
    fidin = open(file_path, 'w')
    for item in content:
        fidin.write('%s' % item)
    fidin.close()

def read_plan(file_path):
    fidin = open(file_path, 'r')
    plan = []
    for line in fidin.readlines():
        line = line.strip()
        line = line[1:-1]
        line = line.split(' ')
        plan.append(line)
    plan = plan[:-1]
    fidin.close()
    return plan
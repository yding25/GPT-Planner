def print_file(file_path):
    fidin = open(file_path, 'r')
    print('#----------file content-----------')
    for line in fidin.readlines():
        line = line.strip()
        print(line)
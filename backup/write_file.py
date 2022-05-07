def write_file(file_path, content):
    fidin = open(file_path, 'w')
    for item in content:
        fidin.write('%s' % item)
    fidin.close()

def get_dirs():
    #code to run
    f = open('input.txt','r').readlines()

    dirs = {'/': {}}
    dir_trail = []

    for line in f:
        line = line[:-1] # strip all '\n'
        cmd = line.split(' ')
        if cmd[0] == '$': # check command (cd or ls)
            if cmd[1] == 'cd':
                if cmd[2] == '/':
                    dir_trail = [dirs['/']]
                elif cmd[2] == '..':
                    dir_trail.pop()
                else:
                    dir_trail.append(dir_trail[-1][cmd[2]])
            else:
                pass #dir_trail unchanged on ls
        else: #processing an ls command
            if cmd[0] == 'dir':
                dir_trail[-1][cmd[1]] = {} #create empty child of current dir
            else:
                dir_trail[-1][cmd[1]] = int(cmd[0]) #add file to current dir

    return dirs

dirs = get_dirs()

filesizes = {}

def calc_filesize(dirs, name):
    size = 0
    for dir_name, sub_dir in dirs.items():
        if type(sub_dir) == dict: #proper subdir
            fs_key = name + '/' + dir_name if name else '/'
            filesizes[fs_key] = calc_filesize(sub_dir, fs_key)
            size += filesizes[fs_key]
        else: #file
            size += sub_dir

    return size

calc_filesize(dirs, '')

# print(filesizes)
print(sum([fs for fs in filesizes.values() if fs <= 100000]))
used_space = filesizes['/']
total_space = 70000000
free_space = total_space - used_space
needed_free_space = 30000000
print(min([fs for fs in filesizes.values() if fs >= needed_free_space - free_space]))
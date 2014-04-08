import sys
from os import mkdir, listdir, path
from shutil import rmtree

def split_file(filename, to_dir):
    if path.exists(to_dir):
        rmtree(to_dir)
    mkdir(to_dir)
    f = open(filename, 'r')
    loc_name = 'Start'
    ff = open(to_dir + loc_name + '.txt', 'w')
    for line in f:
        if line[0] == '#' and line[1] == ' ':
            ff.close()
            loc_name = (line[2:-1]).decode('utf-8')
            ff = open(to_dir + loc_name + '.txt', 'w')
            ff.write(line)
        else:
            ff.write(line)
    f.close()

def merge_file(dir, filename):
    file_list = []
    f = open(filename, 'w')
    for file in listdir(dir):
        file_n = path.join(dir, file)
        ff = open(file_n, 'r')
        f.write(ff.read())
        ff.close()
    f.close()

def main():
    if len(sys.argv) != 3:
        print 'usage: split_file.py {--split | --merge} file'
        sys.exit(1)

    dist_dir = 'src/'
    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--split':
        split_file(filename, dist_dir)
    elif option == '--merge':
        merge_file(dist_dir, filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
  main()

"""
remove .git/objects files
1. find large size files
./git_find_big.sh

2. if the file does not exits, remove it using
git filter-repo --invert-paths --force --path /path/to/large/file
"""
import subprocess, sys
import os


def main():
    print('main')
    cp = subprocess.run(['./git_find_big.sh'], encoding='utf-8', stdout=subprocess.PIPE)
    files = cp.stdout
    files = files.split('\n')
    remove_files = []
    for f in files[2:-1]:
        ff = f.split()
        path = ff[-1]
        print(path)
        if ".png" in path or ".map" in path or "jpg" in path:
            if not os.path.exists(path):
                remove_files.append(path)
    print('start removing')
    print(remove_files)
    for file in remove_files:
        print('gfr', file)
        # cp = subprocess.run(['gfr', file], encoding='utf-8', stdout=subprocess.PIPE)
        # print(cp.stdout)

        cp = subprocess.run(['git', 'filter-repo', '--invert-paths', '--force', '--path', file])
        if cp.returncode != 0:
            print('ls failed.', file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
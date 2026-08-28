import os
from datetime import datetime


# prints current working dir
print(os.getcwd())


# changes dir to input
os.chdir('some/path')
print(os.getcwd())


# prints dir in cwd
print(os.listdir())


# create a dir
os.mkdir('os-test.txt')


# remove a dir
os.removedirs('os-test.txt')


# rename file or folder = old name -> new name
os.rename('os-test.txt', 'demo.txt')


# returns size, modification time
print(os.stat('demo.txt'))

# getting it readable
mod_time = os.stat('os-test.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


# traver the dir - use walk method - goes from top down
for dirpath, dirnames, filenames in  os.walk('/some/path'):
    print(dirpath)
    print(dirnames)
    print(filenames)
    
    
# get environment variables
print(os.environ.get('HOME'))
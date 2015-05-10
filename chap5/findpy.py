#Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import os
def find_py(files):
    s =0
    for dire,root,files in  os.walk(files):
        for i in files:
           if i.split('.')[1] == 'py':
              s = s+1
              yield s
cwd = os.getcwd()

files = os.listdir(cwd)

for i in find_py(cwd):
      print i,

#Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

import os,string
def countlines(path):
   s = 0 
   for dire,root,files in os.walk(path):
          for i in files:
               if i.split('.')[1] == 'py':
                    for line in open(i):
                         s = s+1
                         for i in line:
                             if i == string.ascii_letters:
                                 break
                             if i == '#' or i == '\n':
                               s = s-1  
                               break
                             break
                                    
                         yield s    
cwd =os.getcwd()
for i in countlines(cwd):
    print i

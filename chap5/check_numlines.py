#Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

import os
def checkpy(filename):
     s = 0
     for dirc,root,files in os.walk(filename):
         for i in files:
            if i.split('.')[1] == 'py':
               for lines in open(i):
                  s =s+1
                  yield s
            else:
               pass
cwd = os.getcwd()


for i in checkpy(cwd):
     print i    


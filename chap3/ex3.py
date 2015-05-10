#Write a program to count number of files for each extension in the given directory. 
import os
import sys
cwd = os.getcwd()
l = os.path.join(cwd,sys.argv[1])
def ex_count(l):
   n = os.listdir(l)
   r = []
   f ={}
   for i in n:
      r.append(i.split('.')[1])
  
   for i in r:
      f[i] = f.get(i,0)+1   

   print f
ex_count(l)

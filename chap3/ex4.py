#Write a program to list all the files in the given directory along with their length and last modification time.
import os
import time
cwd = os.getcwd()
l = os.listdir(cwd)
for i in l:
   print i,"\t",len(i),"\t" ,time.ctime(os.stat(i)[9])
  

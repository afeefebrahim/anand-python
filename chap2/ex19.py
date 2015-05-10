#Write a program that takes filename and width as aruguments and wraps the lines longer than width.
from sys import argv
script,filename,width = argv
temp = open(filename).readlines()
l = len(temp)
w = int(width)
for i in range(0,l):
   s =temp[i]
   print s[0:w] 
   print"\n"
   print s[w:] 
   
        

   

#Write a program  to print lines of a file in reverse order. 
import sys
filename = sys.argv[1]
def linecounts(filename):
   return open(filename).readlines()
x =[]
x = linecounts(sys.argv[1])
for i in x[::-1]:
  print i
   

#the grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
import sys
def grep(filename,string):
  l =len(open(filename).readlines())
  txt = open(filename).readlines()
  for i in range(0,l):
     temp = txt[i].split()
     
     for j in range(0,len(temp)):
        if temp[j] == string:
           print txt[i]
z =grep(sys.argv[1],"she")


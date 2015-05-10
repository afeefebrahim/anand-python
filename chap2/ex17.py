#The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
import sys
def head(filename):
   temp = open(filename).readlines()
   print temp[0:10]

def tail(filename):      
   temp = len(open(filename).readlines()) 
   z= open(filename).readlines()  
   print z[temp-10:temp]
print "head is for print first 10 lines"
x =head(sys.argv[1])
print "tail is for print last 10 lines"
y =tail(sys.argv[1])

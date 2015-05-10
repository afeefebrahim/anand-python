# Write a program to print each line of a file in reverse order.
import sys
def reverse_line(filename):
   line =open(filename).readlines()
   for i in line:
     rev = i[::-1]
     print rev
  
x = reverse_line(sys.argv[1])

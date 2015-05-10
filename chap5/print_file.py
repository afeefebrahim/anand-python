#Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.



import sys
def print_line(filename):
    for name in filename:
         for line in open(name):
              if len(line) >= 40:
                  yield line
filename = []
for i in sys.argv[1:]:
    filename.append(i)
for i in print_line(filename):
       print i
    

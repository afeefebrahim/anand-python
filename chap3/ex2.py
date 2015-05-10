#Write a program to list all files in the given directory.
import os
cwd =os.getcwd()
l = os.listdir(cwd)
print l

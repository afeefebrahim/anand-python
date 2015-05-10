#Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.


import zipfile
import sys
f = zipfile.ZipFile(sys.argv[1],'w')
n = sys.argv[2:]
for i in n:
   f.write(i)
for  name in f.namelist():
   print f.read(name)


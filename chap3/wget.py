#Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

import urllib,sys,os
url = urllib.urlopen(sys.argv[1])

p = sys.argv[1]
n = p.split('/')
if n[len(n)-1] == '':
   print ' index.html' 
else:
   print n[len(n)-1]

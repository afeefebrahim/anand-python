#Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.



import re
import urllib
import sys
website = urllib.urlopen(sys.argv[1])
html = website.read()
link = re.findall('"((http)s?://.*?)"',html)
for i in range(len(link)):
   print link[i]
print i

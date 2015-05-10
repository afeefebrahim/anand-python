#Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen, typically used to create blog post URL from post titl

import re,sys
import string
def make_slug(string):
    p = re.sub('\W\s','-',string)
    l =len(p)
    for i in range(l):
         if p[i] == '-' or p[(l-1)-i] == '-':
            new_str = string.strip(p[i])
    print new_str
s= make_slug('--- hello world---')

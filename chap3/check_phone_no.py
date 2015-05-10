#Write a regular expression to validate a phone number.


import re
def check_phone_no(number):
    s =""
    if len(number) ==7 or len(number) == 10:
       for i in range(len(number)): 
          n =re.search(r'\d',number[i])
          if n:
             s = s + n.group()
          else:
             print 'This not a phone number'
             break
    else:
       print "This is not a phone number"  
    if len(s) == 7 or len (number) == 10:
       print s 
n = check_phone_no ('1243sdv')

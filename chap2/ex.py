#make a sum function to work for a list of strings to concatinate.
def sum (c):
  s=''

 
  for i in c:
    s = s+i
  
  return s 

c = sum(["hello","world"] )
print c


 

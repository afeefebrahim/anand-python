#Write a function invertdict to interchange keys and values in a dictionary. 
def invertdict(list):
  d={}
  for count,word in list.items():
     d.setdefault(word,count)
  return d
print  invertdict({'x':1,'y':2,'z':3})

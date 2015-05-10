#Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.
def enumerated(listi):
   return [(i,listi[i]) for i in range(len(listi))]
print enumerated(['a','s','d','f','c'])
   

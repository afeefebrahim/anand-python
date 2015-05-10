#built-in functions min  to compute minimum  of a given list
def min (num):
  sm =num[0]
  for i in range(0,len(num)):
     if sm > num[i]:
        sm = num[i]
  return sm

print min([2,1,3,4,5])
        
  

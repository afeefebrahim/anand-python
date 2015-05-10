#Python provides a built-in function map that applies a function to each element of a list.
def map(func,list1):
   perf =func
   return [perf(item) for item in list1]
def add(num):
   r=1
   r = num**2
   return r
print map(add,[1,2,3,4,5] ) 

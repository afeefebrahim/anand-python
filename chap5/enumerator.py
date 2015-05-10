#The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.

#>> list(enumerate(["a", "b", "c"])
#[(0, "a"), (1, "b"), (2, "c")]
#>>> for i, c in enumerate(["a", "b", "c"]):
#...     print i, c
#...
#0 a
#1 b
#2 c
def my_enumerate(it):
   n =0
   s =[]
   r =[] 
   for i in it:
       s.append(i)
       r.append(n)
       n =n+1
   v = zip(r,s) 
   return v     
it = iter(['a','s','a','v','b'])
p = my_enumerate(it)
for index,value in p:
    print index,value    
  
 


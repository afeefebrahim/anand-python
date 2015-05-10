#Write a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.


import time
def profile(fun):
   def g(x):
     start_time = time.time()
     value = fun(x)
     ex_time = time.time()-start_time
     print "time taken by this funtion =%f sec" % ex_time 
   return g
def square(x):
   s=[]
   [s.append(i*i) for i in x]
   return s 
fun = profile(square)
fun([2,4,5,6,7,8,9,10,11,12,13])  

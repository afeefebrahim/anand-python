#Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.
#>>> def square(x): return x * x
#...
#>>> f = vectorize(square)
#>>> f([1, 2, 3])
#[1, 4, 9]


def vectorize(fun):
   def g(x):
      value = fun(x)
      return value 
   return g
def sqaure(x):
   s =[]
   [s.append(i*i) for i in x]
     
   return s 
def lenght(x):
   s=[]
   [s.append(len(i)) for i in x]
   return s 

fun = vectorize(sqaure)
print fun([1,2,3,4])

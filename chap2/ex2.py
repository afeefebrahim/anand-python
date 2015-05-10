#function name factorial to compute factorial of a number.
def factorial (num):
   x=1
   for i in range(1,num+1):
      x=x*i
   return x

print factorial (5)

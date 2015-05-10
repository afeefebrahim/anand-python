#Implement a function product to multiply 2 numbers recursively using + and - operators only.



def product(x,y):
   if x == 0 or y == 0:
       return 0
   return x +product(x,y-1)
   
print product(5,100) 
   


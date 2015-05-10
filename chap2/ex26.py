#Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
none ="none"
def array (raw,coloum):
   return [[none for i in range(raw)] for j in range(coloum)]
 
print array(3,2)



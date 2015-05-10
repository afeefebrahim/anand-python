#Provide an implementation for zip function using list comprehensions.


def zip1(num,stri):
  a,b = num,stri
  return [(a[i],b[i]) for i in range(len(a)) for j in range(len(b)) if i == j ]

print zip1([1,2,3,4],['a','s','d','f'])

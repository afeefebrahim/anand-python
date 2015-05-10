#Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

#>>> it = iter(range(5))
#>>> x, it1 = peep(it)
#>>> print x, list(it1)
#    0 [0, 1, 2, 3, 4]


def peep(it):
   n =[]
   for i in it:
      n.append(i)
   return n[0],n
it = iter([1,2,3,4])
x,it = peep(it)
print x,it

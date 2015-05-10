# Implement a function izip that works like itertools.izip.


def izip(x,y):
   for i in range(len(x)):
       print x[i],y[i]
izip(['a','b','c','d'],[1,2,3,4])

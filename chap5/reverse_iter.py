#Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::

class reverse_iter():
   def __init__(self,n):
       self.i = 1
       self.n = n
   def __iter__(self):
       return self
   def next(self):
      if self.i <= len(self.n):
         i = self.n[-self.i]
         self.i +=1
         return i
      else:
         raise StopIteration()

s =reverse_iter([1,2,3,4,5])
print s.next()
print s.next()
print s.next()
print s.next()
print s.next()




#built-in function sum to find sum of all elements of a list.
def sum (num):
  s=0
  for i in num:
    s=s+i
  return s

print sum([2,3,4,5])


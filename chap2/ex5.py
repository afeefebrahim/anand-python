#a function name 'reverse' to reverse a list
def reverse (num):
  rev = []
  i=0
  while i < len(num):
    rev.insert(i,num.pop())
    i=i+1
  return rev

print reverse([1,2,3,4,5])
print reverse(reverse([1,2,3,4,5]))




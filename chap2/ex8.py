#a funtionname cumulative_product to compute cumulative product of a list of numbers.
def cumulative_product(num):
  u=[]
  for i in range(0,len(num)):
    r=0
    m=1
    while r<=i:
      m=m*num[r]
      r=r+1
    u.insert(i,m)
  return u

print cumulative_product([2,3,4,5])


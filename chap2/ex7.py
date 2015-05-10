#Write a function cumulative_sum to compute cumulative sum of a list.
def cumilative_sum(num):
   
   u=[]
   for i in range(0,len(num)):
      r=0
      s=0
      while r <= i:
        s=s+num[r]
        r=r+1
      u.insert(i,s)
   return u

print (cumilative_sum([2,3,4,5]))


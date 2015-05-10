#a function dups to find all duplicates in the list.
def dups(num):
  q =[]
  for i in num:
    a= num[i]
    for i in num:
      if a == num[i+1]:
         q.append(a)
  return q
print dups([1,2,3,1,2,4])
     

# Write a function unique to find all the unique elements of a list.
def unique(num):
   out = []
   for i in num:
     if i not in num:
        out.append(i)
   return out
print unique([1,2,1,3,4,2,3])


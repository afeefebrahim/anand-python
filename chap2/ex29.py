#program to print the words in the descending order of the number of occurrences.
def frequency(listi):
   f ={}
   q ={}
   r = []
   for w in listi:
      f[w] = f.get(w,0)+1
   for word,count in f.items():
      q.setdefault(count,word)
   r = sorted(q.keys())
   return[(i,q[i]) for i in r[::-1]] 
      
import sys  
print frequency(open(sys.argv[1]).read())
  


  

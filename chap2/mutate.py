# Write a function mutate to compute all words generated by a single mutation on a given word. A mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string.
def mutate(word):

  a=[]
  z=word
  s=word
  v=word
  st =[]
  l=   ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for i in range(len(word)):
     word = s[:]
     for j in l:
       word = s[:]
       word[i]= j
       a.append(word)
  s =v[:]
  for i in range(len(s)+1):  
    for j in range(len(l)):
      s =v[:]
      s.insert(i,l[j])
      a.append(s)
  s =z[:]
  for i in range(len(s)):
    s =z[:]
    del s[i]
    a.append(s)
  s =v[:]
  for i in xrange(len(s)):
     j =i+1
     for j in xrange(len(s)):
       s =z[:]
       temp = s[i]
       s[i] = s[j]
       s[j] = temp
       a.append(s)
  st =[''.join(i) for i in a]
    
  return st
print mutate(['h','e','l','l','o'])

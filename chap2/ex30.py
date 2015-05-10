#Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. 
def anagram(listi):
   anag =[]
   temp =[[item for item in listi if sorted(item) == sorted(word)]      for word in listi] 
   
   for item in temp:
      if item not in anag:
         anag.append(item)
   return anag
print anagram (['eat', 'ate', 'done', 'tea', 'soup', 'node'])

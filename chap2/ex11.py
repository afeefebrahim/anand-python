#write a funtionname lensort to sort a list of strings based on length.
def lensort(names):
  sort =[]
  

  for i in range(0,len(names)):
 
      temp =""
      for j in range(i+1,len(names)):
          if len(names[i])>len(names[j]):
                 temp= names[j]
                 names[j] = names[i]
                 names[i] = temp
  return names
print  lensort(['fdsfjkds','sdfa','adcscd',])




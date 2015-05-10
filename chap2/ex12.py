# to check the uniquness of a given list of string
def unique(names):
  temp =[]
  for i in range(0,len(names)):
    for j in range(i+1,len(names)):
       if names[i] == names[j]:
          temp.append(names[i])
  return temp
print unique(['as','as','we','we','go'])

# Write a python function parse_csv to parse csv (comma separated values) files.
def parse_csv( pfile,a,b):
   k =[]
   for i in pfile:
     k.append([ ",".join(j) for j in i if j!=a and j!=b and j!='\n'])
   return k
y = open('a.csv').readlines()
print parse_csv(y,'#','!')

#Write a function treemap to map a function over nested list.
#treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
#[1, 4, [9, 16, [25]]]


def treemap(listi):
     
     result = []
     for i in listi:

         if isinstance(i,list):
             result.append(treemap(i))
         else:
             result.append(squr(i))
     return result 
def squr(i):
    s = i*i
    return s

print treemap([[1, 2], [3, [4, 5]], 6] )  
    

#Write a function unflatten_dict to do reverse of flatten_dict.
#unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
#{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}


def unflatten_dict(d):
   result = {}
   for k in d.keys():
      if "." in k:
         parent,child = k.split('.',1)
         if parent in result.keys():
             result[parent].update(unflatten_dict({child:d[k]}))
         else:
             result.update({parent:unflatten_dict({child:d[k]})})
   else:   
         result.update({k:d[k]})
   return result 
print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})


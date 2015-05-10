#Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatten_dict(d,result = None,pkey =" "):
         if result is None:
               result ={}
         for k,v in d.items():
             if pkey == " ":
                key = k
             else:
                key = pkey+'.'+ k     
             if isinstance(v,dict):
                 flatten_dict(v,result,pkey=key)
             else:
                 result[key] = v
         return result
          
print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4},result = None,pkey =" ")

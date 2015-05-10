#Complete the above implementation of json_encode by handling the case of dictionaries.



def json_encode(data):
    if isinstance(data,bool):
        if data:
           return "true"
        else:
           return "false"
    elif isinstance(data,(int,float)):
       return str(data)
    elif isinstance(data,str):
       return changed_str(data)
    elif isinstance(data,list): 
       return "["+",".join(json_encode(i) for i in data) +"]" 
    elif isinstance(data,dict):
       print data
       for i in data:
           r = "{"+','.join(str(i) + ":" + str(data[i])) +"}"
       return r
    else:
       raise TypeError("%s in not json serializable" % repr(data) )
def changed_str(s):
    s=s.replace('"','\\"')
    s=s.replace('\t','\\t')
    s=s.replace('\n','\\n')
    return s
print json_encode({'a':1,'s':2,'d':5})   
      

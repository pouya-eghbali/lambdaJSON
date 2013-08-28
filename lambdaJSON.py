import json

try:    long
except: exec('class long: pass')

flatten = lambda obj:          (isinstance(obj, bytes) 
                        and    (b'bytes://'+obj).decode('utf8') 
                        or     isinstance(obj, tuple) 
                        and    'tuple://'+str(obj) 
                        or     isinstance(obj, list) 
                        and    [flatten(i) for i in obj] 
                        or     isinstance(obj, dict) 
                        and    {(lambda x: isinstance(x, (bool, int, float, complex, long)) 
                        and    str(type(x))[8:-2]+'://'+str(x) 
                        or     flatten(x))(i):flatten(obj[i]) for i in obj} 
                        or     obj)

restore = lambda obj:          (isinstance(obj, str) 
                        and    (lambda x: x.startswith('bytes://') 
                        and    bytes(x[8:], encoding = 'utf8') 
                        or     x.startswith('int://') 
                        and    int(x[6:]) 
                        or     x.startswith('float://') 
                        and    float(x[8:])
                        or     x.startswith('long://') 
                        and    long(x[7:])
                        or     x.startswith('bool://') 
                        and    eval(x[7:]) 
                        or     x.startswith('complex://')
                        and    complex(x[10:])
                        or     x.startswith('tuple://') 
                        and    eval(x[8:]) or x)(obj) 
                        or     isinstance(obj, list) 
                        and    [restore(i) for i in obj] 
                        or     isinstance(obj, dict) 
                        and    {restore(i):restore(obj[i]) for i in obj} 
                        or     obj)

serialize   = lambda obj: json.dumps(flatten(obj))
deserialize = lambda obj: restore(json.loads(obj))


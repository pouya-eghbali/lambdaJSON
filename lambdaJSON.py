try: import ujson as json
except: import json
from ast import literal_eval as eval
from lambdaJSON.functions import defreezef, freezef

ntypes  = (                    (hasattr(__builtins__, 'long')
                        and    (bool, int, float, complex, long))
                        or     (bool, int, float, complex))

flatten = lambda obj:          (isinstance(obj, bytes) 
                        and    (b'bytes://'+obj).decode('utf8') 
                        or     isinstance(obj, tuple) 
                        and    'tuple://'+str(obj)
                        or     isinstance(obj, complex) 
                        and    'complex://'+str(obj)
                        or     isinstance(obj, type(lambda: None)) 
                        and    'function://'+str(freezef(obj)) 
                        or     isinstance(obj, list) 
                        and    [flatten(i) for i in obj] 
                        or     isinstance(obj, dict) 
                        and    {(lambda x: isinstance(x, ntypes) 
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
                        or     x.startswith('function://')
                        and    defreezef(eval(x[11:]))
                        or     x.startswith('tuple://') 
                        and    eval(x[8:]) or x)(obj) 
                        or     isinstance(obj, list) 
                        and    [restore(i) for i in obj] 
                        or     isinstance(obj, dict) 
                        and    {restore(i):restore(obj[i]) for i in obj} 
                        or     obj)

serialize   = lambda obj, *args, **kwargs: json.dumps(flatten(obj), *args, **kwargs)
deserialize = lambda obj, *args, **kwargs: restore(json.loads(obj, *args, **kwargs))


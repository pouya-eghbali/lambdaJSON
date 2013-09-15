try: import ujson as json; __json__ = 'ujson'
except: import simplejson as json; __json__ = 'simplejson'
try: json
except: import json; __json__ = 'json'
try: from ast import literal_eval as eval
except: pass
from lambdaJSON.functions import defreezef, freezef
from __main__ import __builtins__

__version__ = '0.2.15'
__author__  = 'Pooya Eghbali [persian.writer at gmail]'

ntypes  = (                    (hasattr(__builtins__, 'long')
                        and    (bool, int, float, complex, long))
                        or     (bool, int, float, complex))

flatten = lambda obj:          ((hasattr(__builtins__, 'bytes')
                        and     isinstance(obj, bytes))
                        and    (b'bytes://'+obj).decode('utf8') 
                        or     isinstance(obj, tuple) 
                        and    'tuple://'+str(tuple([flatten(i) for i in obj]))
                        or     isinstance(obj, BaseException)
                        and    'exception://'+str([str(i) for i in obj.__reduce__()])
                        or     isinstance(obj, set)
                        and    'set://'+str([flatten(i) for i in obj])
                        or     isinstance(obj, frozenset) 
                        and    'frozenset://'+str([flatten(i) for i in obj])
                        or     isinstance(obj, range) 
                        and    'range://'+str(obj)[5:]
                        or     (hasattr(__builtins__, 'bytearray')
                        and     isinstance(obj, bytearray))
                        and    'bytearray://'+str([i for i in obj])
                        or     (hasattr(__builtins__, 'memoryview')
                        and     isinstance(obj, memoryview))
                        and    'memoryview://'+str([i for i in obj])
                        or     isinstance(obj, complex) 
                        and    'complex://'+str(obj)
                        or     isinstance(obj, type) 
                        and    'type://'+str([obj.__name__,str(obj.__bases__),
                               flatten({f:obj.__dict__[f] for f in obj.__dict__
                        if     callable(obj.__dict__[f])})])
                        or     isinstance(obj, type(lambda: None)) 
                        and    'function://'+str(freezef(obj)) 
                        or     isinstance(obj, list) 
                        and    [flatten(i) for i in obj] 
                        or     isinstance(obj, dict) 
                        and    {(lambda x: isinstance(x, ntypes) 
                        and    str(type(x))[8:-2]+'://'+str(x) 
                        or     flatten(x))(i):flatten(obj[i]) for i in obj} 
                        or     obj)

restore = lambda obj, globs:\
                               (isinstance(obj, str) 
                        and    (lambda x: x.startswith('bytes://') 
                        and    bytes(x[8:], encoding = 'utf8') 
                        or     x.startswith('int://') 
                        and    int(x[6:]) 
                        or     x.startswith('float://') 
                        and    float(x[8:])
                        or     x.startswith('long://') 
                        and    long(x[7:])
                        or     x.startswith('set://') 
                        and    set([restore(i,globs) for i in eval(x[6:])])
                        or     x.startswith('frozenset://') 
                        and    frozenset([restore(i,globs) for i in eval(x[12:])])
                        or     x.startswith('bool://') 
                        and    eval(x[7:])
                        or     x.startswith('exception://') 
                        and    (lambda x = eval(x[12:]):
                                __builtins__.eval('%s(*%s)'%(x[0][8:-2],x[1])))()
                        or     x.startswith('range://') 
                        and    range(*eval(x[8:]))
                        or     x.startswith('bytearray://') 
                        and    bytearray(eval(x[12:]))
                        or     x.startswith('memoryview://') 
                        and    memoryview(bytearray(eval(x[13:])))
                        or     x.startswith('complex://')
                        and    complex(x[10:])
                        or     x.startswith('type://')
                        and    (lambda x = eval(x[7:]):type(x[0],tuple((globs()[i])
                        if     i in globs() else __builtins__.eval(i)
                        for    i in [(i[9:] if i.startswith('__main__.') else i)
                        for    i in [(i[8:-2] if i.endswith('>') else i[8:-3])
                        for    i in x[1][1:-1].split(', ')]]),restore(x[2],globs)))()
                        or     x.startswith('function://')
                        and    defreezef(eval(x[11:]), globs = globs)
                        or     x.startswith('tuple://') 
                        and    tuple([restore(i,globs) for i in eval(x[8:])]))(obj) 
                        or     isinstance(obj, list) 
                        and    [restore(i, globs) for i in obj] 
                        or     isinstance(obj, dict) 
                        and    {restore(i, globs):restore(obj[i], globs) for i in obj} 
                        or     obj)

serialize   = lambda obj, *args, **kwargs: json.dumps(flatten(obj), *args, **kwargs)
deserialize = lambda obj, *args, **kwargs: restore(json.loads(obj, *args,
                                           **{arg:kwargs[arg] for arg in kwargs if not arg == 'globs'}),
                                           globs = (lambda: 'globs' in kwargs and
                                           kwargs['globs'] or (lambda:{'__builtins__':__builtins__}))())

try: import ujson as json; __json__ = 'ujson'
except: pass
try: json
except:
    try: import simplejson as json; __json__ = 'simplejson'
    except: pass
try: json
except: import json; __json__ = 'json'
try: from ast import literal_eval as eval
except: pass
from lambdaJSON.functions import defreezef, freezef
from lambdaJSON import classes
from __main__ import __builtins__

__version__ = '4.2'
__author__  = 'Pooya Eghbali [persian.writer at gmail]'

ntypes  = (                    (hasattr(__builtins__, 'long')
                        and    (bool, int, float, complex, long))
                        or     (bool, int, float, complex))

class method():
    def __init__(self, name, type, freezer, defreezer):
        self.name = name
        self.type = type
        self.freezer = freezer
        self.defreezer = defreezer

class lambdaJSON():
    def __init__(self, globs = lambda: globals(), json = json):
        self.globs = globs
        self.json = json
        self.methods = [method('tuple', tuple,
                               freezer = lambda obj, self: str(tuple([self.flatten(i) for i in obj])),
                               defreezer = lambda obj, self: tuple([self.restore(i) for i in eval(obj[8:])])),

                        method('exception', BaseException,
                               freezer = lambda obj, self: str([str(i) for i in obj.__reduce__()]),
                               defreezer = lambda obj, self: (lambda x = eval(obj[12:]): __builtins__.eval('%s(*%s)'%(x[0][8:-2],x[1])))()),

                        method('set', set,
                               freezer = lambda obj, self: str([self.flatten(i) for i in obj]),
                               defreezer = lambda obj, self: set([self.restore(i) for i in eval(obj[6:])])),

                        method('frozenset', frozenset,
                               freezer = lambda obj, self: str([self.flatten(i) for i in obj]),
                               defreezer = lambda obj, self: frozenset([self.restore(i) for i in eval(obj[12:])])),

                        method('range', range,
                               freezer = lambda obj, self: str(obj)[5:],
                               defreezer = lambda obj, self: range(*eval(x[8:]))),

                        method('complex', complex,
                               freezer = lambda obj, self: str(obj),
                               defreezer = lambda obj, self: complex(obj[10:])),

                        method('type', type,
                               freezer = classes.freeze,
                               defreezer = classes.defreeze),

                        method('function', type(lambda: None),
                               freezer = lambda obj, self: str(self.freezef(obj)),
                               defreezer = lambda obj, self: self.defreezef(eval(obj[11:]))),

                        method('list', list,
                               freezer = lambda obj, self: [self.flatten(i) for i in obj],
                               defreezer = lambda obj, self: [self.restore(i) for i in obj]),

                        method('dict', dict,
                               freezer = lambda obj, self: {(self.flatten(i) if not isinstance(i, (bool, float, complex))
                                                       else str(type(i))[8:-2]+'-->'+str(i))
                                                       :self.flatten(obj[i]) for i in obj},
                               defreezer = lambda obj, self: {self.restore(i):self.restore(obj[i]) for i in obj})]

        if hasattr(__builtins__, 'bytes'):
            self.methods.append(method('bytes', bytes,
                                       freezer = lambda obj, self: obj.decode('utf8'),
                                       defreezer = lambda obj, self: bytes(obj[8:], encoding = 'utf8')))

        if hasattr(__builtins__, 'bytearray'):
            self.methods.append(method('bytearray', bytearray,
                                       freezer = lambda obj, self: str([i for i in obj]),
                                       defreezer = lambda obj, self: bytearray(eval(obj[12:]))))

        if hasattr(__builtins__, 'memoryview'):
            self.methods.append(method('memoryview', memoryview,
                                       freezer = lambda obj, self: self.flatten(obj.obj),
                                       defreezer = lambda obj, self: memoryview(self.restore(obj))))

    def flatten(self, obj):
        try:
            freeze_method = [m for m in self.methods if isinstance(obj, m.type)][0]
            freezed = freeze_method.freezer(obj, self)
            return (freeze_method.name+'-->'+freezed if isinstance(freezed, str) else freezed)
        except: return obj

    def testAndFlat(self, obj):
        try:
            freeze_method = [m for m in self.methods if isinstance(obj, m.type)][0]
            freezed = freeze_method.freezer(obj, self)
            return (freeze_method.name+'-->'+freezed if isinstance(freezed, str) else freezed)
        except:
            return json.dumps(obj)

    def restore(self, obj):
        try:
            restore_method = [m for m in self.methods if isinstance(obj, m.type)]
            if not restore_method: restore_method = [m for m in self.methods if obj.startswith(m.name+'-->')]
            if not restore_method:
                restore_method = [t for t in ntypes if obj.startswith(str(t)[8:-2]+'-->')]
                if restore_method: return eval(obj[len(str(restore_method[0]))-7:])
            return restore_method[0].defreezer(obj, self)
        except Exception as e:
            return obj

    def addMethod(self, name, type, freezer, defreezer):
         self.methods.append(method(name, type, freezer, defreezer))

    def freezef(self, obj):
        return freezef(obj)

    def defreezef(self, obj):
        return defreezef(obj, self.globs)

    def dumps(self, obj, *args, **kwargs):
        return self.json.dumps(self.flatten(obj), *args, **kwargs)

    def loads(self, obj, *args, **kwargs):
        return self.restore(self.json.loads(obj, *args, **kwargs))

    def serialize(self, obj, *args, **kwargs): return self.dumps(obj, *args, **kwargs)
    def deserialize(self, obj, *args, **kwargs): return self.loads(obj, *args, **kwargs)

instance = lambdaJSON()

dumps = serialize   = instance.dumps
loads = deserialize = instance.loads

Usage
=====
Serialize python standard types (function, tuple, class, memoryview, set, frozenset, exceptions, complex, range, bytes, bytearray, dict with number keys, byte keys or tuple keys, and etc) with json.
lambdaJSON lets you serialize python standard library objects with json.

Typical usage
_____________
I'll show you some basic usage of the lambdaJSON lib. for more advanced examples please visit the examples section.

Serialize Complex dict
----------------------

You can serialize any dicts with lambdaJSON supported keys (and also hashable). this includes dictionaries with byte keys, tuple keys and etc::

    #!/usr/bin/env python
    
    >>> import lambdaJSON
    >>> myComplexData = {True: (3-5j), (3+5j): b'json', (1, 2, 3): {b'lambda': [1, 2, 3, (3, 4, 5)]}}
    >>> mySerializedData = lambdaJSON.serialize(myComplexData)
    >>> myComplexData  == lambdaJSON.deserialize(mySerializedData)
    True
    
    >>> 
	
Passing values to json functions
--------------------------------

To pass args and kwargs to the encoder/decoder simply pass them to the serialize/deserialize function, example for json::

    >>> mySerializedData = lambdaJSON.serialize(myComplexData, sort_keys = True)
    >>> myComplexData  == lambdaJSON.deserialize(mySerializedData, object_hook = my_hook)

It can be done for ujson too.

Serializing python functions
----------------------------

You can also serialize python functions::

    >>> import lambdaJSON
    >>> def f(): print('lambdaJSON Rocks!')
    
    >>> mySerializedFunction = lambdaJSON.serialize(f)
    >>> myNewFunction  = lambdaJSON.deserialize(mySerializedFunction)
    >>> myNewFunction()
    'lambdaJSON Rocks!'
    >>>

You should pass a function that returns list of globals to while you are creating a lambdaJSON instance, if not (lambda: globals()) will be used::

    >>> from lambdaJSON import lambdaJSON
	>>> lj = lambdaJSON(globs = (lambda: globals()))
    >>> y = 10
    >>> def f(x): return x*y
    
    >>> mySerializedFunction = lj.dumps(f)
    >>> myNewFunction  = lj.loads(mySerializedFunction)
    >>> myNewFunction(5)
    50
    >>> y = 3
    >>> myNewFunction(5)
    15
    >>>

If no globs passed to function, the globs will be just the __builtins__ module. Note that passing globals will pass the lambdaJSONs local globals and it will not work, if you want to include all the globals from where the deserialization function is called, just use globs = (lambda: globals()), else implement your own function. You can do some nice hacks too::

    >>> z = 10
    >>> def g():
            global z
            z += 1
            return {'z':z}
    
    >>> def f(x,y): return x*y+z
    
	>>> from lambdaJSON import lambdaJSON
	>>> lj = lambdaJSON(globs = g)
    >>> mySerializedFunction = lj.dumps(f)
    >>> myNewFunction  = lj.loads(mySerializedFunction)
    >>> myNewFunction(2,3)
    17
    >>> myNewFunction(2,3)
    18
    >>>

Serializing builtin exceptions
------------------------------	

You can serialize Builtin Exceptions like this::

    >>> a = lambdaJSON.serialize(OSError('FILE NOT FOUND'))
    >>> b = lambdaJSON.deserialize(a)
    >>> raise b
    Traceback (most recent call last):
      File "<pyshell#3>", line 1, in <module>
        raise b
    OSError: FILE NOT FOUND
    >>>
	
Serializing python classes
--------------------------

introduced in version 0.2.15, you can now serialize basic classes and types. The support is basic, but I'm planning to develop the class serialization support in the next subversion. to deserialize a class, you must pass the globals function too, if you do not pass the globals, only __builtins__ will be passed to the class functions. this is an example to do it::

    >>> class test(object):
            def __init__(self):
                self.var = 'lambdaJSON'
    
    >>> serializedClass = lambdaJSON.serialize(test)
    >>> newClass = lambdaJSON.deserialize(serializedClass)
    >>> newClass().var
    'lambdaJSON'
    >>> 
	
Find version
____________

To check version, simply use lambdaJSON.__version__, or if you want to know which json lib is in use, try lambdaJSON.__json__

Json lib in use
_______________

LambdaJSON first tries to import ujson, if it fails it will import simplejson, and if that fails too, the json lib will be imported. you can check which json lib is in use with lambdaJSON.__json__ variable. 

Currently Supported Types
_________________________

This types are covered in this version:

1. Functions
2. Bytes and Bytearrays
3. Classes (basic support)
4. Builtin Exceptions
5. Tuples
6. Complex
7. Range
8. Set and Frozenset
9. Memoryview
10. Dicts (With Number, Tuple, String, Bool and Byte keys)
11. other json supported types
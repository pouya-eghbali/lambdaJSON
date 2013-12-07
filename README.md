lambdaJSON
===========
[![PyPi version](https://pypip.in/v/lambdaJSON/badge.png)](https://pypi.python.org/pypi/lambdaJSON)
[![PyPi downloads](https://pypip.in/d/lambdaJSON/badge.png)](https://pypi.python.org/pypi/lambdaJSON)

Serialize python standard types (function, tuple, class, memoryview, set, frozenset, exceptions, complex, range, bytes, bytearray, dict with number keys, byte keys or tuple keys, and etc) with json.
lambdaJSON lets you serialize python standard library objects with json.


V0.3.0 Changes
==============
Code is more clean, i used class and function definitions instead of lambda to improve readability.
now, there is a lambdaJSON class, the freezer and defreezer class, you can have as many custom lambdaJSON instances you may need.
Method identifier changed. previously i used "type://" identifier, this was unclean, after serialization it turned into "type:\\/\\/" which is ugly, now i have used "type::" identifier.

I have added a method class, you can use it to implement custom freeze and defreeze methods for you complex/custom data types.

you can no more pass globals to the loads function, you must create a lambdaJSON instance while passing the globals function to it.
See the examples for more info.

I've redesigned lambdaJSON, i don't know which parts still needs some work, mail me or post an issue if you've found one, I'd be glad to solve it.

Examples
========

** From v0.2.19 you can use dumps, loads instead of serialize, deserialize. **

Typical usage::

    #!/usr/bin/env python
    
    >>> import lambdaJSON
    >>> myComplexData = {True: (3-5j), (3+5j): b'json', (1, 2, 3): {b'lambda': [1, 2, 3, (3, 4, 5)]}}
    >>> mySerializedData = lambdaJSON.serialize(myComplexData)
    >>> myComplexData  == lambdaJSON.deserialize(mySerializedData)
    True
    
    >>> 

To pass args and kwargs to the encoder/decoder simply pass them to the serialize/deserialize function, example for json::

    >>> mySerializedData = lambdaJSON.serialize(myComplexData, sort_keys = True)
    >>> myComplexData  == lambdaJSON.deserialize(mySerializedData, object_hook = my_hook)

It can be done for ujson too. You can also serialize python functions::

    >>> import lambdaJSON
    >>> def f(): print('lambdaJSON Rocks!')
    
    >>> mySerializedFunction = lambdaJSON.serialize(f)
    >>> myNewFunction  = lambdaJSON.deserialize(mySerializedFunction)
    >>> myNewFunction()
    'lambdaJSON Rocks!'
    >>>

You can no more pass globals to deserialize/dumps methods, so the following code will not work::

    >>> import lambdaJSON
    >>> y = 10
    >>> def f(x): return x*y
    
    >>> mySerializedFunction = lambdaJSON.serialize(f)
    >>> myNewFunction  = lambdaJSON.deserialize(mySerializedFunction, globs = (lambda: globals()))
    >>> myNewFunction(5)
    50
    >>> y = 3
    >>> myNewFunction(5)
    15
    >>>
	
instead, you can do this::

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

If no globs passed to class instance, the globs will be just the __builtins__ module. Note that passing globals will pass the lambdaJSONs local globals and it will not work, if you want to include all the globals from where the deserialization function is called, just use globs = (lambda: globals()), else implement your own function. You can do some nice hacks too::

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

You can serialize Builtin Exceptions like this::

    >>> a = lambdaJSON.serialize(OSError('FILE NOT FOUND'))
    >>> b = lambdaJSON.deserialize(a)
    >>> raise b
    Traceback (most recent call last):
      File "<pyshell#3>", line 1, in <module>
        raise b
    OSError: FILE NOT FOUND
    >>>

introduced in version 0.2.15, you can now serialize basic classes and types. The support is basic, but I'm planning to develop the class serialization support in the next subversion. to deserialize a class, you must pass the globals function too, if you do not pass the globals, only __builtins__ will be passed to the class functions. this is an example to do it::

    >>> class test(object):
            def __init__(self):
                self.var = 'lambdaJSON'
    
    >>> serializedClass = lambdaJSON.serialize(test)
    >>> newClass = lambdaJSON.deserialize(serializedClass)
    >>> newClass().var
    'lambdaJSON'
    >>> 

To check version, simply use lambdaJSON.__version__, or if you want to know which json lib is in use, try lambdaJSON.__json__

Implement your own method
=========================
It is so easy to implement your own method to be used with lambdaJSON, you can use lambdaJSON.addMethod function::

    >>> from lambdaJSON import lambdaJSON
    >>> lj = lambdaJSON()	#No globals passed, using globs = (lambda: globals())
    >>> lj.addMethod(name, type, freezer, defreezer)
	
name must be of type str, and be unique, do not use names of the builtin types like tuple, str, complex, etc...
type is the type you want to add a method for. it must be a type.
freezer and defreezer are functions, freezer must return str, defreezer must receive the str and turn it back to the initial object.
both functions should have obj keyword::

    >>> def myFreezer(obj, lj): #lj is the lambdaJSON instance calling this function
            #do something and return a string.

    >>> def myDefreezer(obj, lj):
            #get the string and defreeze it.
			
Explore source code for more info.


The json lib
============

LambdaJSON first tries to import ujson, if it fails it will import simplejson, and if that fails too, the json lib will be imported. you can check which json lib is in use with lambdaJSON.__json__ variable.

Currently Supported Types
=========================

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

Changes from previous
=====================

Better support for class serialization.

Download
========

Download package from here: https://pypi.python.org/pypi/lambdaJSON

Project Info
============

Github project page: https://github.com/pooya-eghbali/lambdaJSON
PyPi: https://pypi.python.org/pypi/lambdaJSON
Mail me at: persian.writer [at] Gmail.com


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/pooya-eghbali/lambdajson/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
===========
lambdaJSON
===========
Serialize python standard types (tuple, complex, bytes, dict with number keys, byte keys or tuple 

keys, and etc) with json.
lambdaJSON lets you serialize python standard library objects
with json.
Typical usage::

    #!/usr/bin/env python

    >>> import lambdaJSON
    >>> myComplexData = {True: (3-5j), (3+5j): b'json', (1, 2, 3): {b'lambda': [1, 2, 3, (3, 4, 5)]}}
    >>> mySerializedData = lambdaJSON.serialize(myComplexData)
    >>> myComplexData  == lambdaJSON.deserialize(mySerializedData)
    True

    >>> 

To pass args and kwargs to the encoder/decoder simply pass them to the serialize/deserialize function, 

example for json::

    >>> mySerializedData = lambdaJSON.serialize(myComplexData, sort_keys = True)
    >>> myComplexData  == lambdaJSON.deserialize(mySerializedData, object_hook = my_hook)

It can be done for ujson too. You can also serialize python functions::

    >>> import lambdaJSON
    >>> def f(x): return x*x
    
    >>> mySerializedFunction = lambdaJSON.serialize(f)
    >>> myNewFunction  = lambdaJSON.deserialize(mySerializedFunction)
    >>> myNewFunction(10)
    100
    >>>

Currently Supported Types
=========================

This types are covered in this version:

1. Functions
2. Bytes
3. Tuples
4. Complex
5. Dicts (With Number, Tuple, String, Bool and Byte keys)
6. other json supported types

Changes from previous
=====================

Added ability to serialize functions.

Download
========

Download package from here: https://pypi.python.org/pypi/lambdaJSON

Project Info
============

Github project page: https://github.com/pooya-eghbali/lambdaJSON
PyPi: https://pypi.python.org/pypi/lambdaJSON
Mail me at: persian.writer [at] Gmail.com


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/pooya-eghbali/lambdajson/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


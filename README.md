===========
lambdaJSON
===========
Serialize python standard types (tuple, bytes, dict with number keys, byte keys or tuple keys, and etc) with json.
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

Currently Supported Types
=========================

This types are covered in this version:

1. Bytes
2. Tuples
3. Complex
4. Dicts (With Number, Tuple, String, Bool and Byte keys)
5. other json supported types

Changes from previous
=====================

Support for py2 long with no hacks!

Download
========

Download package from here: https://pypi.python.org/pypi/lambdaJSON

Project Info
============

Github project page: https://github.com/pooya-eghbali/lambdaJSON
PyPi: https://pypi.python.org/pypi/lambdaJSON
Mail me at: persian.writer [at] Gmail.com


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/pooya-eghbali/lambdajson/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


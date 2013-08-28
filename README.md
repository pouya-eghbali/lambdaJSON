===========
lambdaJSON
===========
Serialize python standard types (tuple, bytes, dict with number keys, byte keys or tuple keys, and etc) with json.
lambdaJSON lets you serialize python standard library objects
with <json>.
Typical usage::

    #!/usr/bin/env python

    >>> import lambdaJSON
    >>> myComplexData = {(3+5j): b'json', (1, 2, 3): {b'lambda': [1, 2, 3, (3, 4, 5)]}}
    >>> mySerializedData = lambdaJSON.serialize(myComplexData)
    >>> myComplexData  == lambdaJSON.deserialize(mySerializedData )
    True

    >>> 

Currently Supported Types
=========================

This types are covered in this version:

1. Bytes
2. Tuples
3. Dicts (With Number, Tuple, String and Byte keys)
4. other json supported types

Changes
=======

Added support for python 2 long type.

Project Info
============

Github project page: https://github.com/pooya-eghbali/lambdaJSON
Mail me at: persian.writer [at] Gmail.com

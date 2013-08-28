===========
lambdaJSON
===========

lambdaJSON lets you serialize python standard library objects
with <json>.
Typical usage::

    #!/usr/bin/env python

    import lambdaJSON

    mySerialisedObject = lambdaJSON.serialize({(1,2,3):{b'lambda':[b'json',1,3]}, 45: 'test'})
	
	myDeserialisedObject = lambdaJSON.deserialize(mySerialisedObject)

Currently Supported Types
=========================

This types are covered in this version:

1. Bytes
2. Tuples
3. Dicts (With Number, Tuple, String and Byte keys)
4. other json supported types

PyPi project page: https://pypi.python.org/pypi/lambdaJSON

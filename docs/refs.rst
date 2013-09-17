Quick Reference
===============

This section will provide a brief explaination to all parts and functions included in lambdaJSON lib.

__init__.py
___________

Everything inside __init__.py!

__author__
----------

if used, this value returns name of the author of the lambdaJSON lib, 'Pooya Eghbali'.

__version__
-----------

if used, this value returns the version of the lambdaJSON lib, eg: 2.0.16.

__json__
--------

if used, this value returns the name of the json lib in use, eg: 'ujson'. You can use this to find the json lib if you want to pass for example ujson specific arguments to the deserialization function.

__builtins__
------------

this is imported from __main__. the __builtins__ included in the top level module.

eval
----

actually this is the same as ast.literal_eval, used instead of builtins.eval to avoid security issues.

flatten
-------

lambdaJSON uses this function to flatten objects and convert them to a format that json understands. if you just want to flattend an object, use this function.

restore
-------

this is the reverse if the flatten function. restores object from the flattened one.

freezef
-------

this function is used to flatten function objects. (imported from functions.py)

defreezef
---------

reverse function for freezef. (imported from functions.py)

functions
---------

this is same as functions.py.

ntypes
------

a list of available numerical types and bool. this is different in versions of python (there is no long type in py3k)

json
----

returns the json lib in use.

serialize
---------

this is the main serialization function.

deserialize
-----------

and the main deserialize function!

functions.py
____________

freezef
-------

this function is used to flatten function objects.

defreezef
---------

reverse function for freezef.
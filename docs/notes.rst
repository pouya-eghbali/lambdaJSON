Notes
=====

Here are some notes and some warnings.

Serializing class and functions
_______________________________

1. Keep in mind, deserialized functions and classes are not equal to the original ones.
2. Deserialized class and functions are not serializable!
3. if you want to serialize a class, define class vars inside __init__. just class functions are included in serialization.

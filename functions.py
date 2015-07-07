import marshal
from types import FunctionType

def freezef(function):
    if hasattr(function, '__code__'):
        code = function.__code__
    else:
        code = function.func_code

    defaults = function.__defaults__ or tuple()

    return marshal.dumps({'code': code, 'defaults': defaults})

def defreezef(function, globals):
    function = marshal.loads(function)
    code     = function['code']
    defaults = function['defaults']

    return FunctionType(code, globals(), 'func', defaults)

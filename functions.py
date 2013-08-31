try:
    freezef = lambda function:     {'co_argcount': function.__code__.co_argcount,
                                   'co_kwonlyargcount': function.__code__.co_kwonlyargcount,
                                   'co_nlocals': function.__code__.co_nlocals,
                                   'co_stacksize': function.__code__.co_stacksize,
                                   'co_flags': function.__code__.co_flags,
                                   'co_code': function.__code__.co_code,
                                   'co_consts': function.__code__.co_consts,
                                   'co_names': function.__code__.co_names,
                                   'co_varnames': function.__code__.co_varnames,
                                   'co_filename': function.__code__.co_filename,
                                   'co_name': function.__code__.co_name,
                                   'co_firstlineno': function.__code__.co_firstlineno,
                                   'co_lnotab': function.__code__.co_lnotab}

    defreezef = lambda co_dict:    type(lambda: None)(
                                   type((lambda: None).__code__)(
                                   co_dict['co_argcount'],
                                   co_dict['co_kwonlyargcount'],
                                   co_dict['co_nlocals'],
                                   co_dict['co_stacksize'],
                                   co_dict['co_flags'],
                                   co_dict['co_code'],
                                   co_dict['co_consts'],
                                   co_dict['co_names'],
                                   co_dict['co_varnames'],
                                   co_dict['co_filename'],
                                   co_dict['co_name'],
                                   co_dict['co_firstlineno'],
                                   co_dict['co_lnotab']),
                                   {'__builtins__':__builtins__},'')
except:
    freezef = lambda function:     {'co_argcount': function.func_code.co_argcount,
                                   'co_nlocals': function.func_code.co_nlocals,
                                   'co_stacksize': function.func_code.co_stacksize,
                                   'co_flags': function.func_code.co_flags,
                                   'co_code': function.func_code.co_code,
                                   'co_consts': function.func_code.co_consts,
                                   'co_names': function.func_code.co_names,
                                   'co_varnames': function.func_code.co_varnames,
                                   'co_filename': function.func_code.co_filename,
                                   'co_name': function.func_code.co_name,
                                   'co_firstlineno': function.func_code.co_firstlineno,
                                   'co_lnotab': function.func_code.co_lnotab}

    defreezef = lambda co_dict:    type(lambda: None)(
                                   type((lambda: None).func_code)(
                                   co_dict['co_argcount'],
                                   co_dict['co_nlocals'],
                                   co_dict['co_stacksize'],
                                   co_dict['co_flags'],
                                   co_dict['co_code'],
                                   co_dict['co_consts'],
                                   co_dict['co_names'],
                                   co_dict['co_varnames'],
                                   co_dict['co_filename'],
                                   co_dict['co_name'],
                                   co_dict['co_firstlineno'],
                                   co_dict['co_lnotab']),
                                   {'__builtins__':__builtins__},'')

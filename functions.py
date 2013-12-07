freezef = lambda function:         (lambda code = (hasattr(function, '__code__')
                                   and function.__code__ or function.func_code):
                                   {'co_argcount': code.co_argcount,
                                   'co_kwonlyargcount': (
                                   hasattr(code,'co_kwonlyargcount')
                                   and code.co_kwonlyargcount),
                                   'co_nlocals': code.co_nlocals,
                                   'co_stacksize': code.co_stacksize,
                                   'co_flags': code.co_flags,
                                   'co_code': code.co_code,
                                   'co_consts': code.co_consts,
                                   'co_names': code.co_names,
                                   'co_varnames': code.co_varnames,
                                   'co_filename': code.co_filename,
                                   'co_name': code.co_name,
                                   'co_firstlineno': code.co_firstlineno,
                                   'co_lnotab': code.co_lnotab,
                                   'defaults':function.__defaults__ or tuple()})()

defreezef = lambda co_dict, globs:\
                                   eval("""(lambda lambdaJSON_globs = globs,
                                   co_dict = co_dict: (lambda %s:
                                   (type(lambda: None)(
                                   type((lambda: None).__code__)(
                                   co_dict['co_argcount'],%s
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
                                   lambdaJSON_globs(),'')(%s))))()"""%
                                   (','.join(['%s'%a+('=%s'%co_dict['defaults']
                                   [co_dict['co_varnames'][:co_dict['co_argcount']].index(a)
                                   -len(co_dict['co_varnames'][:co_dict['co_argcount']])]
                                   if len(co_dict['defaults']) >= abs(co_dict['co_varnames']
                                   [:co_dict['co_argcount']].index(a)-len(co_dict['co_varnames']
                                   [:co_dict['co_argcount']]))  else '')
                                   for a in co_dict['co_varnames'][:co_dict['co_argcount']]]),
                                   (co_dict['co_kwonlyargcount'] is False and ' '
                                   or "co_dict['co_kwonlyargcount'],"),
                                   ','.join(['%s'%a for a
                                   in co_dict['co_varnames'][:co_dict['co_argcount']]])))

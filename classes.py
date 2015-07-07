from lambdaJSON.functions import *

def freeze(obj, lj):
    
    name  = obj.__name__
    bases = obj.__bases__
    
    cdict = {}

    for key in obj.__dict__:
        try: cdict[key] = lj.testAndFlat(obj.__dict__[key])
        except: pass

    if cdict['__doc__'] == 'null': cdict.pop('__doc__')

    bases = [str(b).split()[1][1:-2] for b in bases]
    
    return str([name, bases, cdict])

def defreeze(obj, lj):

    info  = eval(obj[8:-1])

    name  = info[0]
    bases = info[1]
    cdict = info[2]

    cdict = {key:lj.restore(cdict[key]) for key in cdict}
    globs = lj.globs()

    for i in range(len(bases)):
        base = bases[i].split('.')
        while not base[0] in globs:
            base.pop(0)
            if not base: break

        if base:
            bases[i] = '.'.join(base)
        else:
            bases[i] = ''

    bases = [b for b in bases if b]

    Class = eval('type("{name}", {bases}, cdict)'.format(
             name = name, bases = str(tuple(bases)).replace("'",'')),
             globs, locals())

    return Class

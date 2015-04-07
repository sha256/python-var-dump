__author__ = "Shamim Hasnath"
__copyright__ = "Copyright 2013, Shamim Hasnath"
__license__ = "BSD License"
__version__ = "1.0.1"


TAB_SIZE = 4
NoneType = type(None)



def display(o, space, num, key, typ):
    st = ""
    l = []
    if key:
        if typ is dict:
            st += " " * space + "['%s'] => "
        else:
            st += " " * space + "%s => "
        l.append(key)
    elif space > 0:
        st += " " * space + "[%d] => "
        l.append(num)
    else:  # at the very start
        st += "#%d "
        l.append(num)

    if type(o) in (tuple, list, dict, int, str, float, bool, NoneType, bytes):
        st += "%s(%s) "
        l.append(type(o).__name__)

        if type(o) in (int, float, bool, NoneType):
            l.append(o)
        else:
            l.append(len(o))

        if type(o) in (str, bytes):
            st += '"%s"'
            l.append(o)

    elif type(o).__name__ == 'datetime':
        st += "%s(%s)"
        l.append(type(o).__name__)
        l.append(o.__str__())

    elif isinstance(o, object):
        st += "object(%s) (%d)"
        l.append(o.__class__.__name__)
        l.append(len(getattr(o, '__dict__', {})))

    print(st % tuple(l))


def dump(o, space, num, key, typ):

    if type(o) in (str, int, float, bool, NoneType, bytes):
        display(o, space, num, key, typ)

    elif isinstance(o, object):
        display(o, space, num, key, typ)
        num = 0
        if type(o) in (tuple, list, dict):
            typ = type(o)  # type of the container of str, int, long, float etc
        elif isinstance(o, object):
            o = getattr(o, '__dict__', {})
            typ = object
        for i in o:
            space += TAB_SIZE
            if type(o) is dict:
                dump(o[i], space, num, i, typ)
            else:
                dump(i, space, num, '', typ)
            num += 1
            space -= TAB_SIZE


def var_dump(*obs):
    """
      shows structured information of a object, list, tuple etc
    """
    i = 0
    for x in obs:
        dump(x, 0, i, '', object)
        i += 1

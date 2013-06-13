from __future__ import print_function
from types import NoneType

__author__ = "Shamim Hasnath"
__copyright__ = "Copyright 2013, Shamim Hasnath"
__license__ = "BSD License"
__version__ = "1.0"


TAB_SIZE = 4


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

    if type(o) in (tuple, list, dict, int, str, float, long, bool, NoneType):
        st += "%s(%s) "
        l.append(type(o).__name__)

        if type(o) in (int, float, long, bool, NoneType):
            l.append(o)
        else:
            l.append(len(o))

        if type(o) is str:
            st += '"%s"'
            l.append(o)

    elif isinstance(o, object):
        st += "object(%s) (%d)"
        l.append(o.__class__.__name__)
        l.append(len(o.__dict__))

    print(st % tuple(l))


def dump(o, space, num, key, typ):

    if type(o) in (str, int, float, long, bool, NoneType):
        display(o, space, num, key, typ)

    elif isinstance(o, object):
        display(o, space, num, key, typ)
        num = 0
        if type(o) in (tuple, list, dict, bool):
            typ = type(o)  # type of the container of str, int, long, float etc
        elif isinstance(o, object):
            o = o.__dict__
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
      shows
    """
    i = 0
    for x in obs:
        dump(x, 0, i, '', object)
        i += 1
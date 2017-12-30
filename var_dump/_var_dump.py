from __future__ import print_function
import sys

try:
    from enum import Enum
except ImportError:
    Enum = type(str)

try:
    from types import NoneType
except ImportError:
    NoneType = type(None)

if sys.version_info > (3,):
    long = int
    unicode = str

__author__ = "Shamim Hasnath"
__copyright__ = "Copyright 2013, Shamim Hasnath"
__license__ = "BSD License"
__version__ = "1.2.0"

TAB_SIZE = 4


def display(o, space, num, key, typ, proret):
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

    if type(o) in (tuple, list, dict, int, str, float, long, bool, NoneType, unicode):
        st += "%s(%s) "
        l.append(type(o).__name__)

        if type(o) in (int, float, long, bool, NoneType):
            l.append(o)
        else:
            l.append(len(o))

        if type(o) in (str, unicode):
            st += '"%s"'
            l.append(o)

    elif isinstance(o, Enum):
        st += "Enum(%s)"
        l.append(str(o))

    elif isinstance(o, object):
        st += "object(%s) (%s)"
        l.append(o.__class__.__name__)
        try:
            l.append(len(o.__dict__))
        except AttributeError:
            l.append(str(o))

    if proret:
        print(st % tuple(l))

    return st % tuple(l)


def dump(o, space, num, key, typ, proret):
    r = ''
    if type(o) in (str, int, float, long, bool, NoneType, unicode, Enum):
        r += display(o, space, num, key, typ, proret)

    elif isinstance(o, Enum):
        r += display(o, space, num, key, typ, proret)

    elif isinstance(o, object):
        r += display(o, space, num, key, typ, proret)
        num = 0
        if type(o) in (tuple, list, dict):
            typ = type(o)  # type of the container of str, int, long, float etc
        elif isinstance(o, object):
            try:
                o = o.__dict__
            except AttributeError:
                return r
            typ = object
        for i in o:
            space += TAB_SIZE
            if type(o) is dict:
                r += dump(o[i], space, num, i, typ, proret)
            else:
                r += dump(i, space, num, '', typ, proret)
            num += 1
            space -= TAB_SIZE
    return r


def var_dump(*obs):
    """
        shows structured information of a object, list, tuple etc
    """
    i = 0
    for x in obs:
        dump(x, 0, i, '', object, True)
        i += 1


def var_export(*obs):
    """
        returns output as as string
    """
    r = ''
    i = 0
    for x in obs:
        r += dump(x, 0, i, '', object, False)
        i += 1
    return r

import unittest

from enum import Enum
from var_dump import var_export


class Foo:
    def __init__(self):
        self.x = 5
        self.y = 'abc'
        self.z = True


class Bar:
    def __init__(self):
        self.value = False
        self.foo = Foo()


class Color(Enum):
    RED = 1
    GREEN = 2


class ObjectWithoutDict:
    """
    https://stackoverflow.com/questions/25221270/how-to-create-class-object-without-dict
    """
    __slots__ = ()


class ObjectWithCircularReference:
    def __init__(self):
        self.r = self


class DeepCircularReferenceParent:
    def __init__(self):
        self.child = DeepCircularReferenceChild(self)


class DeepCircularReferenceChild:
    def __init__(self, parent: DeepCircularReferenceParent):
        self.parent = parent


class ParentObjectThatIsEqualToOthers:
    def __init__(self):
        self.foo = Foo()

    def __eq__(self, other):
        return True


class VarExportTestCase(unittest.TestCase):
    def test_var_export(self):
        data = [
            # todo: why is there a space at the end?
            [None, '#0 NoneType(None) '],

            # booleans
            [True,  '#0 bool(True) '],
            [False, '#0 bool(False) '],

            # strings
            ['',    '#0 str(0) ""'],
            ['a',   '#0 str(1) "a"'],
            ['abc', '#0 str(3) "abc"'],

            # numbers
            [0,     '#0 int(0) '],
            [12,    '#0 int(12) '],
            [-13,   '#0 int(-13) '],
            [21.37, '#0 float(21.37) '],

            # enums
            [Color.RED, '#0 Enum(Color.RED)'],
            [Color(2),  '#0 Enum(Color.GREEN)'],

            # dicts
            [
                {'foo': 12, 'bar': False},
                "#0 dict(2) "
                "    ['foo'] => int(12) "
                "    ['bar'] => bool(False) ",
            ],

            # objects
            [Foo(), '#0 object(Foo) (3)'
                    '    x => int(5) '
                    '    y => str(3) "abc"'
                    '    z => bool(True) '],

            # nested objects
            [Bar(), '#0 object(Bar) (2)'
                    '    value => bool(False) '
                    '    foo => object(Foo) (3)'
                    '        x => int(5) '
                    '        y => str(3) "abc"'
                    '        z => bool(True) '],
        ]

        for given, expected in data:
            with self.subTest([given, expected]):
                self.assertEqual(
                    var_export(given),
                    expected
                )

    def test_var_export_multiple_values_at_once(self):
        self.assertEqual(
            var_export('foo', 55, Bar(), False),
            '#0 str(3) "foo"'
            '#1 int(55) '
            '#2 object(Bar) (2)'
            '    value => bool(False) '
            '    foo => object(Foo) (3)'
            '        x => int(5) '
            '        y => str(3) "abc"'
            '        z => bool(True) '
            '#3 bool(False) '
        )

    def test_var_export_object_without_dict(self):
        self.assertRegex(
            var_export(ObjectWithoutDict()),
            '#0 object\(ObjectWithoutDict\) '
            '\(<tests.var_export_test.ObjectWithoutDict object at 0x(\w+)>\)'
        )

    def test_var_export_circular_reference(self):
        self.assertEqual(
            var_export(ObjectWithCircularReference()),
            '#0 object(ObjectWithCircularReference) (1)'
            '    r => object(ObjectWithCircularReference) (1) …circular reference…'
        )

    def test_var_export_compares_parents_by_reference_not_value(self):
        self.assertEqual(
            var_export(ParentObjectThatIsEqualToOthers()),
            '#0 object(ParentObjectThatIsEqualToOthers) (1)'
            '    foo => object(Foo) (3)'
            '        x => int(5) '
            '        y => str(3) "abc"'
            '        z => bool(True) '
        )

    def test_var_export_deep_circular_reference(self):
        self.assertEqual(
            var_export(DeepCircularReferenceParent()),
            '#0 object(DeepCircularReferenceParent) (1)'
            '    child => object(DeepCircularReferenceChild) (1)'
            '        parent => object(DeepCircularReferenceParent) (1) …circular reference…'
        )


if __name__ == '__main__':
    unittest.main()

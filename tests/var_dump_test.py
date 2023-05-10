import unittest

from var_dump import var_dump
from unittest.mock import MagicMock, call, patch


class VarDumpTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_var_dump(self, print_mock: MagicMock):
        var_dump('abc')

        print_mock.assert_called_with('#0 str(3) "abc"')
        self.assertEqual(1, print_mock.call_count)

    @patch('builtins.print')
    def test_var_dump_multiple_values_at_once(self, print_mock: MagicMock):
        var_dump('foo', 55, False)

        print_mock.assert_has_calls([
            call('#0 str(3) "foo"'),
            call('#1 int(55) '),
            call('#2 bool(False) '),
        ])
        self.assertEqual(3, print_mock.call_count)


if __name__ == '__main__':
    unittest.main()

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('../converter'))

from csv_to_json_converter import *

class TestConverter(unittest.TestCase):
    """
    This class implements the unit tests for class Converter
    """

    def test_format_1(self):
        dummy_object = Converter("dummy")  # dummy object for testing

        input = ['James Murphy',
                 'yellow',
                 '83880',
                 '018 154 6474']

        output = {'color': 'yellow',
                  'lastname': 'Murphy',
                  'phonenumber': '018-154-6474',
                  'zipcode': '83880',
                  'firstname': 'James'}

        self.assertEqual(dummy_object._normalize_format_1(input), output)


    def test_format_2(self):
        dummy_object = Converter("dummy")  # dummy object for testing

        input = ['Booker T.',
                 'Washington',
                 '87360',
                 '373 781 7380',
                 'yellow']

        output = {'color': 'yellow',
                  'lastname': 'Washington',
                  'phonenumber': '373-781-7380',
                  'zipcode': '87360',
                  'firstname': 'Booker T.'}

        self.assertEqual(dummy_object._normalize_format_2(input), output)

    def test_format_3(self):
        dummy_object = Converter("dummy")  # dummy object for testing

        input = ['Chandler',
                 'Kerri',
                 '(623)-668-9293',
                 'pink',
                 '12313']

        output = {'color':
                  'pink',
                  'lastname': 'Chandler',
                  'phonenumber': '623-668-9293',
                  'zipcode': '12313',
                  'firstname': 'Kerri'}

        self.assertEqual(dummy_object._normalize_format_3(input), output)

    def test_normalize_color_valid(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_color('red'), 'red')

    def test_normalize_color_invalid(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_color('joy'), '')

    def test_normalize_color_empty(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_color(''), '')

    def test_normalize_color_whitespace(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_color(' '), '')

    def test_normalize_zipcode_valid(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_zipcode('14850'), '14850')

    def test_normalize_zipcode_long(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_zipcode('14850112'), '')

    def test_normalize_zipcode_short(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_zipcode('148'), '')

    def test_normalize_zipcode_alnum(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_zipcode('148abc'), '')

    def test_normalize_zipcode_alpha(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_zipcode('abc'), '')

    def test_normalize_zipcode_empty(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_zipcode(''), '')

    def test_normalize_zipcode_whitespace(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_zipcode('  '), '')

    def test_normalize_phonenumber_valid(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('607-279-8551'), '607-279-8551')

    def test_normalize_phonenumber_spaces(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('607 279 8551'), '607-279-8551')


    def test_normalize_phonenumber_parens(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('(607) 279 8551'), '607-279-8551')

    def test_normalize_phonenumber_parens_dashes(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('(607)-279-8551'), '607-279-8551')

    def test_normalize_phonenumber_long(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('(607)-279-85515566'), '')

    def test_normalize_phonenumber_short(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('(607)-279-85'), '')

    def test_normalize_phonenumber_alnum(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('(607)-279-85abc'), '')

    def test_normalize_phonenumber_empty(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber(''), '')

    def test_normalize_phonenumber_whitespaces(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_phonenumber('  '), '')

    def test_normalize_lastname_valid(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_lastname('John'), 'John')

    def test_normalize_lastname_lowercase(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_lastname('john'), 'John')

    def test_normalize_lastname_uppercase(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_lastname('JOHN'), 'John')

    def test_normalize_lastname_alnum(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_lastname('abc123'), '')

    def test_normalize_lastname_num(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_lastname('123'), '')

    def test_normalize_lastname_empty(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_lastname(''), '')

    def test_normalize_lastname_whitespace(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_lastname('  '), '')

    def test_normalize_firstname_lowercase(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname('john'), 'John')

    def test_normalize_firstname_uppercase(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname('JOHN'), 'John')

    def test_normalize_firstname_dot(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname('Booker T.'), 'Booker T.')

    def test_normalize_firstname_dot_small(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname('booker t.'), 'Booker T.')

    def test_normalize_firstname_alnum(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname('abc123'), '')

    def test_normalize_firstname_num(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname('123'), '')

    def test_normalize_firstname_empty(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname(''), '')

    def test_normalize_firstname_whitespace(self):
        dummy_object = Converter("dummy")  # dummy object for testing
        self.assertEqual(dummy_object._normalize_firstname('  '), '')


# When called from command line interface,
# following code will be executed.
if __name__ == '__main__':
    unittest.main()
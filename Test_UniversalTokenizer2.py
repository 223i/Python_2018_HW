"""This module contains a set of tests for 'UniversalTokenizer2.py' module"""


import unittest
from UniversalTokenizer2 import Token, UniversalTokenizer


class UniversalTokenizerTest(unittest.TestCase):
    """ The basic class that inherits unittest.TestCase. It contains
    the main tests for module "UniversalTokenizer2.py" """

    def test_type_of_symbol_digit(self):
        """check whether the returned value is digit."""
        a = UniversalTokenizer().type_define('4')
        self.assertEqual(a, 'Digit')

    def test_type_of_symbol_alpha(self):
        """check whether the returned value is alphabetical symbol."""
        a = UniversalTokenizer().type_define('a')
        self.assertEqual(a, 'Alpha')

    def test_type_of_symbol_space(self):
        """check whether the returned value is whitespace."""
        a = UniversalTokenizer().type_define(' ')
        self.assertEqual(a, 'Space')

    def test_type_of_symbol_punctuation(self):
        """check whether the returned value is punctuation."""
        a = UniversalTokenizer().type_define('!')
        self.assertEqual(a, 'Punctuation')

    def test_type_of_symbol_othertype(self):
        """check whether the returned value is other type."""
        a = UniversalTokenizer().type_define('+')
        self.assertEqual(a, 'Other type')

    def test_tokenize_wrong_type_of_input_fail(self):
        """check the return value if an input is not a string"""
        with self.assertRaises(TypeError) as error:
            UniversalTokenizer().tokenize([])

    def test_tokenize_empty_string_input(self):
        """check the return value if an input is an empty string"""
        a = UniversalTokenizer().tokenize('')
        self.assertEqual(a, [])

    def test_tokenize_one_alphabetical_symbol_input(self):
        """check the returned token if an input is alphabetical symbol."""
        actual_result = UniversalTokenizer().tokenize('word')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.type_of_token, 'Alpha')
        self.assertEqual(instance_of_actual_result.string_representation,
                         'word')
        self.assertEqual(instance_of_actual_result.position, 0)

    def test_tokenize_space_input(self):
        """check the returned token if an input is a whitespace"""
        actual_result = UniversalTokenizer().tokenize(' ')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.type_of_token,
                         'Space')
        self.assertEqual(instance_of_actual_result.string_representation,
                         ' ')
        self.assertEqual(instance_of_actual_result.position, 0)

    def test_tokenize_digit_input(self):
        """check the returned token if an input is one digit"""
        actual_result = UniversalTokenizer().tokenize('1')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.type_of_token, 'Digit')
        self.assertEqual(instance_of_actual_result.string_representation,
                         '1')
        self.assertEqual(instance_of_actual_result.position, 0)

    def test_tokenize_punctuation_input(self):
        """check the returned token if an input is punctuation symbol."""
        actual_result = UniversalTokenizer().tokenize('!')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.type_of_token,
                         'Punctuation')
        self.assertEqual(instance_of_actual_result.string_representation,
                         '!')
        self.assertEqual(instance_of_actual_result.position, 0)


if __name__ == '__main__':
    unittest.main()

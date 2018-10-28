"""This module contains a set of tests for 'UniversalTokenizer2.py' module"""

import unittest
from UniversalTokenizer2 import  UniversalTokenizer


class UniversalTokenizerTest(unittest.TestCase):
    """ The basic class that inherits unittest.TestCase. It contains
    the main tests for module "UniversalTokenizer2.py" """

    def test_tokenize_wrong_type_of_input_fail(self):
        """check the return value if an input is not a string"""
        with self.assertRaises(TypeError) as error:
            UniversalTokenizer().tokenize([])

    def test_tokenize_empty_string_input(self):
        """check the return value if an input is an empty string"""
        a = UniversalTokenizer().tokenize("")
        self.assertEqual(a, [])

    def test_tokenize_one_alphabetical_symbol_input(self):
        """check the returned value if an input is one alphabetical symbol."""
        actual_result = UniversalTokenizer().tokenize("a")
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 0)
        self.assertEqual(instance_of_actual_result.string_representation, 'a')

    def test_tokenize_space_input(self):
        """check the return value if an input is a whitespace"""
        actual_result = UniversalTokenizer().tokenize(" ")
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 0)
        self.assertEqual(instance_of_actual_result.string_representation, " ")

    def test_tokenize_digit_input(self):
        """check the returned value if an input is one digit"""
        actual_result = UniversalTokenizer().tokenize("4")
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 0)
        self.assertEqual(instance_of_actual_result.string_representation, '4')

    def test_tokenize_punctuation_input(self):
        """check the returned value if an input is punctuation symbol."""
        actual_result = UniversalTokenizer().tokenize("!")
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 0)
        self.assertEqual(instance_of_actual_result.string_representation, "!")

    def test_tokenizer_space_after_punctuation(self):
        """check the returned value if the input has whitespace
         after punctuation."""
        actual_result = UniversalTokenizer().tokenize('token. Token')
        values_for_comparison = [0, 'token',5, '.', 6, ' ', 7, 'Token']
        p = 0  #counter for list
        for i in actual_result:
            self.assertEqual(i.position, values_for_comparison[p])
            p += 1
            self.assertEqual(i.string_representation,
                             values_for_comparison[p])
            p += 1


if __name__ == '__main__':
    unittest.main()

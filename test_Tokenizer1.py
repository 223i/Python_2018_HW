"""This module contains a set of tests for 'Tokenizer1.py' module"""

import unittest
from Tokenizer1 import Token, Tokenizer


class TokenizerTest(unittest.TestCase):
    """ The basic class that inherits unittest.TestCase. It contains
    the main tests for module "Tokenizer1.py" """

    def test_tokenize_wrong_type_of_input_fail(self):
        """check the return value if an input is not a string"""
        with self.assertRaises(TypeError) as error:
            Tokenizer().tokenize([])

    def test_tokenize_empty_string_input(self):
        """check the return value if an input is an empty string"""
        a = Tokenizer().tokenize("")
        self.assertEqual(a, [])

    def test_tokenize_one_alphabetical_symbol_input(self):
        """check the returned value if an input is one alphabetical symbol."""
        actual_result = Tokenizer().tokenize("a")
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 0)
        self.assertEqual(instance_of_actual_result.string_representation, 'a')

    def test_tokenize_one_not_alphabetical_symbol_input(self):
        """check the returned value if an input is not alphabetical symbol."""
        actual_result = Tokenizer().tokenize("!")
        self.assertEqual(actual_result, [])

    def test_tokenize_not_alphabetical_symbols_at_the_end_input(self):
        """check the returned value if an input contains non-alphabetic
         symbols at the end."""
        actual_result = Tokenizer().tokenize('Token._?')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 0)
        self.assertEqual(instance_of_actual_result.string_representation,
                         'Token')

    def test_tokenize_alphabetical_symbol_at_the_end_input(self):
        """check the returned value if the end of input
         is alphabetical symbol."""
        actual_result = Tokenizer().tokenize('Token')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 0)
        self.assertEqual(instance_of_actual_result.string_representation,
                         'Token')

    def test_tokenizer_not_alphabetical_symbols_at_the_beginning(self):
        """check the returned value if an input contains
         non-alphabetic symbols at the beginning."""
        actual_result = Tokenizer().tokenize('--token')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 2)
        self.assertEqual(instance_of_actual_result.string_representation,
                         'token')

    def test_tokenizer_other_symbols_at_the_beginning_and_the_end(self):
        """check the returned value if an input contains
         non-alphabetic symbols at the beginning and at the end."""
        actual_result = Tokenizer().tokenize('--token_!')
        instance_of_actual_result = actual_result[0]
        self.assertEqual(instance_of_actual_result.position, 2)
        self.assertEqual(instance_of_actual_result.string_representation,
                         'token')

    def test_tokenizer_space_after_punctuation(self):
        """check the returned value if the input has space
         after punctuation."""
        actual_result = Tokenizer().tokenize('token. Token')
        values_for_comparison = [0, 'token', 7, 'Token']  #expected result
        p = 0  #counter for list
        for i in actual_result:
            self.assertEqual(i.position, values_for_comparison[p])
            p += 1
            self.assertEqual(i.string_representation,
                             values_for_comparison[p])
            p += 1


if __name__ == '__main__':
    unittest.main()



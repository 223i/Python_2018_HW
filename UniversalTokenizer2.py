"""This module contains two classes for text-tokenisation"""

import unicodedata


class Token:
    """ Form new data-type "token" with 3 parameters - type_of_token,
    string_representation and position. """

    def __init__(self, type_of_token, string_representation, position):
        """ Inits Token with 3 parameters:
        :param type_of_token: type of token
        :param string_representation: sequence named token.
        :param position: position of first symbol in token.
        """
        self.type_of_token = type_of_token
        self.string_representation = string_representation
        self.position = position


class UniversalTokenizer:
    """ This class provides a method for text-tokenization.
        For the text submitted the class return the result of tokenization
        as a list of tokens.

        For instance: The string "I am Groot!" will be tokenized by
        the following manner:
        [Alpha I 0
        Space    1
        Alpha am 2
        Space    4
        Alpha Groot 5
        Punctuation ! 10]

        """



    def type_define (self, input):
        """ Read the string, extract the sequences and return their types.

        :param string: input line, the appropriate type - string
        :return: list of tokens

        """
        if input.isdigit():
            return 'Digit'
        if input.isalpha():
            return 'Alpha'
        if input.isspace():
            return 'Space'
        if unicodedata.category(input) == 'Po':
            return 'Punctuation'
        else:
            return 'Other type'


    def tokenize(self, input):
        """ Read the string, extract the different types of sequences and
         their starting positions and return them in a list of tokens.

        :param input: input line, the appropriate type - string
        :return: list of tokens

        """

        if not isinstance(input, str):
            raise TypeError('Invalid type of input')

        tokens = []  # list for tokens
        """Check whether the input is an empty string"""

        if len(input) == 0:
            return tokens

        for idSymbol, symbol in enumerate(input):
            """ The next conditions check when the type of next
            symbol changes and create new token with his characteristics"""

            type = UniversalTokenizer().type_define(symbol)
            if idSymbol == 0:
                start_token = idSymbol
                previous_type = type

            elif type != previous_type:
                tokens.append(Token(UniversalTokenizer().type_define
                                    (input[idSymbol - 1]),
                                    start_token, input[start_token:idSymbol]))
                start_token = idSymbol
                previous_type = type
                
        """ This condition checks the last symbol and writes down 
        last token and his position"""

        if UniversalTokenizer().type_define(input[idSymbol]) == type:
            tokens.append(Token(UniversalTokenizer().type_define
                                (input[idSymbol]), start_token,
                                input[start_token:idSymbol+1]))
        return tokens


if __name__ == '__main__':
    text = 'word'
    lst = UniversalTokenizer().tokenize(text)
    for token in lst:
        print(token.type_of_token, ':', token.position,
              ':', token.string_representation)

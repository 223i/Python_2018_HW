"""This module contains two classes for text-tokenisation"""

class Token:
    """ Form new data-type "token" with 2 parameters - string_representation
     and position. """

    def __init__(self, string_representation, position):
        """ Inits Token with 2 parameters:
        :param string_representation: alphabetical sequence named token.
        :param position: position of first alphabetical symbol in token.

        """
        self.string_representation = string_representation
        self.position = position


class Tokenizer:
    """ This class provides a method for text-tokenization.
    For the text submitted the class return the result of tokenization
    as a list of tokens.

    For instance: The string "I am Groot" will be tokenized by
    the following manner:
    [0 I
    2 am
    5 Groot]

    """

    def tokenize(self, string):
        """ Read the string, extract the alphabetical sequences and their
         starting positions and return them in a list of tokens.

        :param string: input line, the appropriate type - string
        :return: list of tokens

        """

        if not isinstance(string, str):
            raise TypeError('Invalid type of input')

        tokens = []  #  list for tokens
        # Check whether the input is an empty string
        if len(string) == 0:
            return tokens
        for idSymbol, symbol in enumerate(string):
             
            # The next 3 conditions check those cases, when the first symbols
            # in the string are nonalphabetical, when symbol is the beginning 
            # of the alphabetical sequence or the first word in the line
            # and when, and when symbol is the end of alphabetical sequence
            if not symbol.isalpha() and (idSymbol == 0
                                         or not string[idSymbol-1].isalpha()):
                continue

            elif symbol.isalpha() and (idSymbol == 0
                                       or not string[idSymbol-1].isalpha()):
                start = idSymbol

            elif not symbol.isalpha() and string[idSymbol-1].isalpha():
                tokens.append(Token(string[start:idSymbol], start))

        # This condition checks the last symbol. If this symbol is a alpha,
        # method writes down last token and his position
        if string[-1].isalpha():
            tokens.append(Token(string[start:len(string)], start))
        return tokens


if __name__ == '__main__':
    text = input()
    lst = Tokenizer().tokenize(text)
    for token in lst:
        print(token.position, ': ', token.string_representation)

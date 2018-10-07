class Token:
    """ Form new data-type "token" with 2 parameters - string_representation and position. """

    def __init__(self, string_representation, position):
        """ Inits Token with 2 parameters:
        :param string_representation: alphabetical sequence named token.
        :param position: position of first alphabetical symbol in token.

        """
        self.string_representation = string_representation
        self.position = position


class Tokenizer:
    """Tokenize the text."""

    def tokenize(self, string):
        """ Read the string, extract the alphabetical sequences and their starting positions
         and return them in a list of tokens.
        :param string: input line, the appropriate type - string
        :return: list of tokens

        """
        if string == '':
            raise IndexError('String index out of range')
        if not isinstance(string, str):
            raise TypeError('Invalid type of input')
        tokens = []  #list for tokens
        for idSymbol, symbol in enumerate(string):
            if not symbol.isalpha() and (idSymbol == 0 or not string[idSymbol-1].isalpha()):  #the first symbols
                                                                # in the string are nonalphabetical
                continue
            elif symbol.isalpha() and (idSymbol == 0 or not string[idSymbol-1].isalpha()):  #the begining of the
                                                                # alphabetical sequence or the first word in the line
                start = idSymbol   #note the begining of token
            elif not symbol.isalpha() and string[idSymbol-1].isalpha():   #the end of alphabetical sequence
                tokens.append(Token(string[start:idSymbol], start))
        if string[-1].isalpha():
            tokens.append(Token(string[start:len(string)], start))
        return tokens


if __name__ == '__main__':
    text = input()
    lst = Tokenizer().tokenize(text)

    for token in lst:
        print(token.position, ': ', token.string_representation)

    #text = open('C:/Users/123/untitled/text.txt', 'r', encoding='utf-8')
    #text.close()
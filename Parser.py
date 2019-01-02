"This module parses test and returns possible syntax tree-options"""

class Token:
    """ Form new data-type "token" with 2 parameters - string_representation
        and position. """

    def __init__(self, string_representation, position):
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

        tokens = []  # list for tokens

        # Check whether the input is an empty string
        if len(string) == 0:
            return tokens
        for idSymbol, symbol in enumerate(string):
            # The next 3 conditions check those cases, when the first symbols
            # in the string are nonalphabetical, when symbol is the beginning
            # of the alphabetical sequence or the first word in the line
            # and when, and when symbol is the end of alphabetical sequence

            if not symbol.isalpha() and (idSymbol == 0
                                         or not string[idSymbol - 1].isalpha()):
                continue

            elif symbol.isalpha() and (idSymbol == 0
                                       or not string[idSymbol - 1].isalpha()):
                start = idSymbol

            elif not symbol.isalpha() and string[idSymbol - 1].isalpha():
                tokens.append(Token(string[start:idSymbol], start))

        # This condition checks the last symbol. If this symbol is a alpha,
        # method writes down last token and his position
        if string[-1].isalpha():
            tokens.append(Token(string[start:len(string)], start))
        return tokens


class Constituent:
    """ Form new data-type "Constituent" with 4 parameters - tag,
    string_representation, start, end, structures. """

    def __init__(self, tag, start, end, structures):
        self.tag = tag
        self.start = start
        self.end = end
        self.structures = structures


grammar = {('NP', 'VP'): ['S'], ('Nnom'): ['NP'], ('Nacc'): ['NP'],
           ('Nnom', 'Ngen'): ['NP'], ('V', 'NP'): ['VP']}
grammar_dictionary = {'мама': 'Nnom', 'мыла': 'Vpast',
                      'мыла': 'Ngen', 'раму': 'Nacc'}


class TokenWithTag:
    """ Reorganizes data-type "token" bz means adding a parameter - tag """

    def __init__(self, string_representation, position, tag):
        self.string_representation = string_representation
        self.position = position
        self.tag = tag


class Morphoanalyzer:  # tokenize and add POS-tags
    """ This class provides a method for morphological analysis.

       For the text submitted the class return the result of morphological
        analysis as a list of tokens. """

    def dumm_morphoanalyzer(self, input):
        tokens = Tokenizer().tokenize(input)
        tokens_with_tags = []
        for i in tokens:
            if i.string_representation in grammar_dictionary:
                tag = grammar_dictionary.get(i.string_representation)
                string = i.string_representation
                start = i.position
                tokens_with_tags.append(TokenWithTag(string, start, tag))
        return tokens_with_tags


""""
#check the result of morphoanalysis
if __name__ == '__main__':
    lst = Morphoanalyzer().dumm_morphoanalyzer("мама мыла раму")
    for token in lst:
        print(token.position, ': ', token.string_representation, ': ', token.tag)
"""


class Parser:

    def parse(self, string):
        # получаем список с токенами у которых известна
        # начальная позиция, сам токен,и его частеречная принадлежность.
        # Токены указаны в словаре в той же последовательности, в какой идут в тексте
        tokens_for_work = Morphoanalyzer().dumm_morphoanalyzer(string)

        #by_end = {}
        id_x = 0
        constituents = []
        for token in tokens_for_work:
            if tokens_for_work[0] == token: #проверяем первый ли токен
                if token.tag in (grammar or grammar_dictionary):
                    Constituent.start = token.position
                    Constituent.end = token.position + len(token.string_representation)
                    Constituent.tag = token.tag
                    Constituent.structures = []
                    Constituent.structures.append(Constituent.tag)  # тег запивается в атрибут конституента
                    id_x = 0                                 #Заоминаем предыд.конституент в списке
                    constituents.append((Constituent.tag, string[Constituent.start:Constituent.end]))

            else:
                if (constituents[id_x].tag, token.tag) in grammar:  # если предыдущий тег конституента и тег токена есть в грамматике
                    Constituent.tag = grammar[(constituents[id_x].tag, token.tag)]  # достаем из грамматики тэг конституента
                    Constituent.start = constituents[id_x].start
                    Constituent.end = token.position + len(token.string_representation)
                    Constituent.structures.append(Constituent.tag)  # тег запивается в атрибут конституента
                    constituents.append(Constituent.tag, string[Constituent.start:Constituent.end])
                    id_x += 1  # Запоминаем конец конституента

        return constituents


if __name__ == '__main__':
    text = 'Мама мыла раму'
    lst = Parser().parse(text)
    for constituent in lst:
        print(constituent)

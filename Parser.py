"This module parses text and returns possible syntax tree-options"""

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
           ('Nnom', 'Ngen'): ['NP'], ('Vpast', 'NP'): ['VP']}
grammar_dictionary = {'мама': 'Nnom', 'мыла': 'Vpast', 'раму': 'Nacc'}


class TokenWithTag:
    """ Reorganizes data-type "token" it means adding a parameter - tag """

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


"""
#check the result of morphoanalysis
if __name__ == '__main__':
    lst = Morphoanalyzer().dumm_morphoanalyzer("мама мыла раму")
    for token in lst:
        print(token.position, ': ', token.string_representation, ': ', token.tag)
"""


class Parser:

    def __init__(self):
        self.right_border_constituent = {}
        self.identity_constituent = {}

    def add(self, constituent):
        identity = (constituent.start, constituent.end, constituent.tag)
        if identity not in self.identity_constituent.keys():
            self.right_border_constituent[constituent.end] = constituent
            self.identity_constituent[(constituent.start, constituent.end, constituent.tag)] = constituent
            return constituent
        else:
            old_constituent = self.identity_constituent[identity]
            old_constituent[identity] = structures.extend(constituent.structures)

    def bind(self, c):
        end_of_previous = self.right_border_constituent[c.start-1]
        for end_of_previous in self.right_border_constituent:
            n = self.right_border_constituent.get(end_of_previous)
            if (n.tag, c.tag) in grammar:
                for i in grammar[(n.tag, c.tag)]:
                    t = Constituent(i, n.start, c.end, [(n.tag, c.tag)])
                    self.put(t)

    def put(self, constituent):
        result = self.add(constituent)
        if result != None and constituent.start != 0:
            self.bind(constituent)

    def parse(self, string):
        # получаем список с токенами у которых известна
        # начальная позиция, сам токен,и его частеречная принадлежность.
        # Токены указаны в словаре в той же последовательности, в какой идут в тексте
        tokens_for_work = Morphoanalyzer().dumm_morphoanalyzer(string)

        for token in tokens_for_work:
            token_start = token.position
            token_end = token.position + len(token.string_representation)
            tag = token.tag
            structures = ()
            c = Constituent(tag, token_start, token_end, structures)
            self.put(c)


if __name__ == '__main__':
    text = 'мама мыла раму'
    lst = Parser().parse(text)

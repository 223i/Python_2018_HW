"This module parses text and returns possible syntax tree-options"""

from Tokenizer1 import Token, Tokenizer


class Constituent:
    """ Form new data-type "Constituent" with 4 parameters - tag,
    string_representation, start, end, structures. """

    def __init__(self, tag, start, end, structures):
        """ Inits Conctituent with 4 parameters:
        :param tag: tag of constituent
        :param start: the beginning of constituent.
        :param end: the end of constituent.
        :param structures: structures for this token
        """
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
        """ Inits Conctituent with 4 parameters:
        :param string_representation: sequence named token.
        :param position: the beginning of token.
        :param tag: the tag of token.
        """
        self.string_representation = string_representation
        self.position = position
        self.tag = tag


class Morphoanalyzer:
    """ This class provides a method for morphological analysis.
       For the text submitted the class return the result of morphological
        analysis as a list of tokens. """

    def dumm_morphoanalyzer(self, input):
        """ Tokenizes the string. For each token reorganizes it's structure
        :param string: input line, the appropriate type - string
        :return: list of tokens with tags
        """
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
        print(token.position, ': ', token.string_representation, ': ',
         token.tag)
"""


class Parser:
    """ This class provides a methods for text-parsing.
        For the text submitted the class returns the result of parsing
        as a set of constituents. """

    def __init__(self):
        """ Inits 2 dictionaries: right_border_constituent and
         identity_constituent
        """
        self.right_border_constituent = {}
        self.identity_constituent = {}

    def add(self, constituent):
        """ For the constituent submitted the method checks whether parameters
         of constituent are in the dictionary 'identity_constituent'. For
         those cases, when it is, structures of constituent are updated.
         Otherwise, constituent is added in both dictionaries and is returned.
        :param constituent: submitted constituent
        :return: constituent, that is added in dictionaries
        """

        identity = (constituent.start, constituent.end, constituent.tag)
        if identity not in self.identity_constituent:
            if constituent.end not in self.right_border_constituent:
                self.right_border_constituent[constituent.end] = [constituent]
                self.identity_constituent[(constituent.start, constituent.end,
                                           constituent.tag)] = constituent
            else:
                self.right_border_constituent[constituent.end].append(constituent)
                self.identity_constituent[(constituent.start, constituent.end,
                                           constituent.tag)] = constituent
        else:
            old_constituent = self.identity_constituent[identity]
            old_constituent[identity] = structures.extend(constituent.structures)

   def bind(self, c):
        """For the constituent submitted the method checks whether previous
         constituent and constituent submitted are in grammar. For each
         case, when they are, method builds new constituent and submit
         it to "put()" function.
        :param c: submitted constituent
        """

        end_of_previous = self.right_border_constituent[c.start - 1]
        constituents_t = []
        for n in end_of_previous:
            if (n.tag, c.tag) in grammar:
                for i in grammar[(n.tag, c.tag)]:
                    t = Constituent(i, n.start, c.end, [(n, c)])
                    constituents_t.append(t)
                    self.put(t)
                    return constituents_t
                    


    def put(self, constituent):
        """This method becomes constituent and calls the method 'add()' for it.
        If returned value is not None, it calls the method 'bind()' for
         constituent.
        :param constituent:submitted constituent
        """
        result = self.add(constituent)
        if result != None and constituent.start != 0:
            for_return = self.bind(constituent)
            return  result, for_return

    def parse(self, string):
        """This method becomes string, provides morphoanalysis for it. Method creates
        constituent for each morphoanalyzed and calls  "put()" function for them.
        :param string: input string
        """

        tokens_for_work = Morphoanalyzer().dumm_morphoanalyzer(string)
        constituents = []
        for token in tokens_for_work:
            token_start = token.position
            token_end = token.position + len(token.string_representation)
            tag = token.tag
            structures = ()
            c = Constituent(tag, token_start, token_end, structures)
            a = self.put(c)
            constituents.extend(a)
        return constituents


if __name__ == '__main__':
    text = 'мама мыла раму'
lst = Parser().parse(text)


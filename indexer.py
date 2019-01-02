"""This module contains one class in order to index text"""

from UniversalTokenizer2 import Token, UniversalTokenizer
import shelve


class Indexer:
    """Contain the function for text indexation and the
    function for closing database."""

    def shelve_db(self, text):
        """ This function gets list of tokens and  creates database o
        nly with alphabetical tokens and digits

        :param text: text, which should be tokenized and placed into db
        :return: d_b - database
        """

        with shelve.open("database",  flag='n', protocol=None,
                         writeback=False) as d_b:
            tokens = UniversalTokenizer().tokenize(text)
            counter = 0
            for token in tokens:
                    if token.type_of_token == 'Alpha' \
                            or token.type_of_token == 'Digit':
                        d_b[str(counter)] = token.position
                        counter += 1
            print(dict(d_b))  #check whether database is fulfilled
        return d_b

    def shelve_db_close(self, d_b):
        """ This function helps to close created database

        :param d_b: the existing opened database
        :return: the closed database
        """

        d_b.close()
        return d_b


if __name__ == '__main__':
    db = Indexer().shelve_db("This  is test example 1 ")
    db = Indexer().shelve_db_close(db)




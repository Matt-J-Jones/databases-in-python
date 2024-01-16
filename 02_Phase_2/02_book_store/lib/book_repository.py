from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

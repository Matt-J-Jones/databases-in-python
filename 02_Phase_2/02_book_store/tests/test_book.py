from lib.book import Book

def test_book_constructs():
    book = Book(1, "Test Title", "Test Author")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author"

def test_books_format_nicely():
    book = Book(1, "Test Title", "Test Author")
    assert str(book) == "1 - Test Title - Test Author"

def test_books_are_equal():
    book_1 = Book(1, "Test Title", "Test Author")
    book_2 = Book(1, "Test Title", "Test Author")
    assert book_1 == book_2

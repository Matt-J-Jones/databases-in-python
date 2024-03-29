from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/music_library.sql")

# Retrieve all artists
book_repository = BookRepository(connection)
books = book_repository.all()

# List them out
for book in books:
    print(book)

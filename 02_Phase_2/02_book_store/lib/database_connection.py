import os
import psycopg2
# from psycopg2 import connect
from psycopg2.extras import DictCursor
from . import passwords

# This class helps us interact with the database.
# It wraps the underlying psycopg library that we are using.

# If the below seems too complex right now, that's OK.
# That's why we have provided it!
class DatabaseConnection:
    DATABASE_NAME = "book_store"  # <-- CHANGE THIS!
    DB_USER = passwords.username() # <-- CHANGE THIS!
    DB_PASSWORD = passwords.password()  # <-- CHANGE THIS!

    def __init__(self):
        self.connection = None

    # This method connects to PostgreSQL using the psycopg library.
    # We connect to localhost and select the database name given in argument.
    def connect(self):
        try:
            db_url = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@localhost/{self.DATABASE_NAME}"
            self.connection = psycopg2.connect(db_url, cursor_factory=DictCursor)
        except psycopg2.OperationalError as e:
            raise Exception(f"Couldn't connect to the database {self.DATABASE_NAME}! {e}")

    # This method seeds the database with the given SQL file.
    # We use it to set up our database ready for our tests or application.
    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    # This method executes an SQL query on the database.
    # It allows you to set some parameters too. You'll learn about this later.
    def execute(self, query, params=None):
        self._check_connection()
        with self.connection.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = [dict(row) for row in cursor.fetchall()]
            else:
                result = None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = (
        "DatabaseConnection.exec_params: Cannot run a SQL query as "
        "the connection to the database was never opened. Did you "
        "make sure to call first the method DatabaseConnection.connect` "
        "in your app.py file (or in your tests)?"
    )

    # This private method checks that we're connected to the database.
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)


# Usage example:
# db = DatabaseConnection()
# db.connect()
# db.seed("your_sql_file.sql")
# result = db.execute("SELECT * FROM your_table;")
# print(result)
# Get-Content ../seeds/database_connection | psql -h 127.0.0.1 test_table

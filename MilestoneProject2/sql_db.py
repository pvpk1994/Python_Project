import sqlite3
import context_manager

# Cursor Usage:All operations in SQLite are made by cursors
# and not by the connection object itself

# That is so that we can have one single connection.but potentially multiple cursors
# either reading data and at most one writing data

# Commit()
# Save the result of the query to the disk
# Keep bunch of data in memory until we commit


def create_db_book_table():
    # establish a connection first to the db
    with context_manager.DatabaseConnect() as connection:
        cursor = context_manager.cursor_establish(connection)
    # Create a table with 3 fields name, author (of type text) and read
    # of type integer
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key ,author text,read integer)')


def insert_db_book_table(namer,authors):
    with context_manager.DatabaseConnect() as connection:
        cursor = context_manager.cursor_establish(connection)
    # Now insert all the fields into created table

        cursor.execute("INSERT INTO books VALUES(?,?,0)",(namer, authors))


def get_all_books():
    with context_manager.DatabaseConnect() as connection:
        cursor = context_manager.cursor_establish(connection)
        cursor.execute('SELECT * FROM books')

    # NOTE: there is no need to commit in this case since we are merely reading with SELECT and not
    # writing anything to the file.
    # so without commit and we close, it closes without saving, there fore we do the following taking the
    # help of cursor feature and fetch all the entries into books list in this case
        books = cursor.fetchall()
    # convert the above obtained list into dict
        books_1 = [{'name': row[0],
                'author': row[1],
                'read': row[2]} for row in books]

    # now return the dictionaries created
    return books_1

# uses database sql operations to update the books


def mark_book_as_read(name):
    with context_manager.DatabaseConnect() as connection:
        cursor = context_manager.cursor_establish(connection)
        cursor.execute('UPDATE books set read=1 WHERE name=?', (name,))


# Use database sql operations to delete an entry (an entire row)


def del_book(name):
    with context_manager.DatabaseConnect() as connection:
        cursor = context_manager.cursor_establish(connection)
        cursor.execute('DELETE FROM books WHERE name=?',(name,))


create_db_book_table()
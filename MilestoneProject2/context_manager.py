import sqlite3

'''
Context Manager file: Essentially helps us in removing duplication and helps
in issuing the same commands avoiding same set of statements being repeated in the
file....
'''


class DatabaseConnect:
    def __init__(self):
        self.connection = None
        self.host = 'data.db'

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


connect_cursor = DatabaseConnect().connection


def cursor_establish(connect):
    cursor = connect.cursor()
    return cursor

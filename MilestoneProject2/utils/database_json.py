import json
'''
Concerned with storing and retreiving files from a JSON file
'''

books_file = "books.json"


def create_book_table():
    with open(books_file, "w") as file:

        json.dump([], file)  # copy an empty list into file to remove further JSON decode errors.


def get_all_books():
    with open(books_file, 'r') as file:
        # gives an error since, books_file at the beginning is books.json which is empty
        return json.load(file)  # a list


# implicitly called function
def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)  # copy books into file


def add_new_book(name, author):
    books = get_all_books()
    books.append({'name': name,
                  'author': author,
                  'read': False})
    _save_all_books(books)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


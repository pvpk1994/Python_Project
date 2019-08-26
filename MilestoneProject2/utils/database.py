'''
Concerned with storing and extracting books from a CSV File
Format of CSV file : name, author, read \n
'''

books_file = 'books.txt'


# Add a new book to the database

def create_book():
    with open(books_file, 'w'):
        pass


def add_new_book(name, author):
    with open('books.txt', 'a') as file:
        file.write(f'{name},{author},0\n')


def list_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    return[
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
     ]


def mark_book_as_read(name):
    books = list_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)  # implicitly called


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")

'''
# Not very efficient way to accomplish deletion of a book
def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)
'''

# To create a new list and not add the entry we want to delete


def best_delete_book(name):
    books = list_all_books()
    books = [book for book in books if book['name']!= name]
    _save_all_books(books)



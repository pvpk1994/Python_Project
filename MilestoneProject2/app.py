from utils import database
from utils import database_json
import sql_db
USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book 
- 'q' to quit


Your Choice: """


def prompt_add_book():
    name = input("Enter the name of the book:")
    author = input("Enter the author of the book:")
    sql_db.insert_db_book_table(name,author)


def list_books():
    books = sql_db.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book that you just finished reading: ')
    sql_db.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')
    sql_db.del_book(name)


def menu():
    database_json.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Invalid Option, Please enter a valid option")

        user_input = input(USER_CHOICE)


if __name__ == '__main__':
    menu()

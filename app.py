'''
- Enter 'a' to add a movie, '1' to see movies, 'f' to find a movie and 'q' to quit.

- Add movies
- See movies
- Find movies
- Quit the program

Tasks:
[x] : Show the user the main interface and get their inputs
[x]: Allow users to add movies
[x]: Show all their movies
[x]: Find a movie
[x]: stop running the program when users type 'q'
'''

# maintaining list of tuples for movies
'''
Movie Parameter : (name, director and year)

User has to be given the option of adding movies to the database
'''
movies = []  # Empty list.. later filled out by the users


def add_movies():
    name = input("Enter the name of the movie:")
    director = input("Enter the name of the director:")
    year = input("Enter the year of release:")
    movies.append({
        'name': name,
        'Director': director,
        'year': year
    })


def view_movie(movie_list):
    for t in movie_list:
        print(f'Movie Details: {t["name"]}')


def find_movie():
    find_by = input("What property of the movie are you looking for ?")  # name / dir / year?
    looking_for = input("What are you looking for ?")  # attribute name ?
    found_movies = find_by_attr(movies, looking_for, lambda x: x[find_by])
    view_movie(found_movies)


def find_by_attr(items, expected, finder):
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see movies, 'f' to find a movie and 'q' to quit :") # 1st time request
    while user_input != 'q':
        if user_input == 'a':
            add_movies()
        elif user_input == 'l':
            view_movie(movies)
        elif user_input == 'f':
            find_movie()
        user_input = input("Enter 'a' to add a movie, 'l' to see movies, 'f' to find a movie and 'q' to quit :")
    if user_input is 'q':
        print(f'The program is exiting ...')
        exit()


menu()
# add_movies()









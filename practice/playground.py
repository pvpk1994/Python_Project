# Creating a dictionary
my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 89, 100, 23]
}

print(f'Sum:{sum(my_student["grades"])}')


def avg_grade():
    totals = 0
    for grade in my_student['grades']:
        totals += grade
    avg = totals/len(my_student['grades'])
    print(f'Avg grade is: {avg}')
    return avg


avg_grade()

#  classes and objects


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    #  functions inside class are referred to as property

    def average(self):
        return sum(self.grades)/len(self.grades)

    def print_info(self):
        print('<<{}>> '.format(self.name))

    #  @ property changes method into a property. It is to be used when there
    #  are no args passed to the function other than self.
    @property
    def maximum(self):
        return f'The Max of grades: {max(self.grades)}'


student_one = Student('Rolf Smith', [70, 89, 10, 23])
print(f'Func Avg {student_one.average()}')

#  To know type of student_one , we can do the following
print(f'Type: {student_one.__class__}')
student_one.print_info()
print(student_one.maximum)

#  creating own objects


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    # used in indexing the list
    def __getitem__(self, item):
        return self.cars[item]

    # for class to return strings of some description
    def __repr__(self):
        return f'Garage with {Garage.__len__(self)} cars'


Ford = Garage()
Ford.cars.append('Fusion')  # add items to the list of cars[]
Ford.cars.append('Jetta')
Ford.cars.append('HayBrazer')
print(f'{Ford.cars}')
print(f'{len(Ford)}')  # define inline __len__ to determine the length of class

# challenge: to print indices of the class
print(f'{Ford[2]}')

# Now after setting up __len__ and __getitem__ we can iterate through the class
for car in Ford:
    print(f'Car:{car}')
print(f'{Ford}')


# ------- Magic Methods Exercise : Udemy ------
# ------------------ Magic Methods in Python ------------
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self, item):
        return self.players[item]

    def __repr__(self):
        return f'Club {self.name}: ["{self.players[0]}","{self.players[1]}"]'

    def __str__(self):
        return f'Club {self.name} with {Club.__len__(self)} players'


club = Club('Arsenal')
print(f'{club.name}')
club.players.append('Rolf')
club.players.append('Anne')
print(f'Number of club members: {len(club)}')
print(f'Club Member: {club[0]}')
print(club)


# ----- Inheritance in python ---
class Movie:
    def __init__(self, lang, year, name):
        self.lang = lang
        self.year = year
        self.name = name

    def __str__(self):
        return f'{self.name} is an {self.lang} movie and was released in {self.year}'


# Movie_type is a subclass that describes whether its holly/bolly/tolly/mollywood movie
class MovieType(Movie):
    def __init__(self, lang, year, name, genre):
        super().__init__(lang, year, name)
        self.genre = genre


# inits
movie1 = MovieType('English', '2018', 'Quiet Place', 'Horror')
print(movie1)


# ------ @classmethod and @staticmethod demonstrations --------
# staticmethod is used when self is not used in the functions inside class.
class FloatingPoint:
    def __init__(self, number):
        self.number = number

    @staticmethod  # as we see, there is no need to pass self as an arg to this function
    def sum_float(val1, val2):
        return FloatingPoint(val1+val2)

    def __repr__(self):
        return f'<Fixed Float>: {self.number:.2f}'

    # with staticmethod, we cannot access sum_float function present in parent class
    # thru child class object.
    @classmethod
    def sum_float1(cls, val1, val2):
        return cls(val1+val2)


new_number = FloatingPoint(13.555)
print(new_number)


class SubFloat(FloatingPoint):
    def __init__(self, number):
        super().__init__(number)
        self.symbol = "$"

    def __repr__(self):
        return f'<US Dollar: {self.symbol} {self.number:.2f}>'


money = SubFloat.sum_float1(74.567, 67.890)
print(money)


class Gaadi:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class University:
    def __init__(self):
        self.uni = []

    def __len__(self):
        return len(self.uni)

    # def add_uni(self, university):
    # raise NotImplementedError("This function is still under development")

    def add_uni(self, car_t):
        if not isinstance(car_t, Gaadi):
            raise TypeError(f'Tried to add a `{car_t.__class__.__name__}` to the parking lot at'
                            f' University, only cars allowed')
        # raise NotImplementedError("Functionality yet to be added")
        self.uni.append(car_t)


univ = University()
# univ.add_uni('University of Houston')
# print(len(univ))
car = Gaadi('Ford', 'Fiesta')
try:
    univ.add_uni('Fiesta')

except TypeError:
    print('Your car is not in the University')

# finally always runs no matter what
finally:
    print(f'Length of univ: {len(univ)}')


# ----- Udemy Exercise Problem ---
def count_positive_integers(m):
    if m < 0:
        raise ValueError("No Negative integers allowed!!")
    for num in range(0, m+1):
        print(num)


count_positive_integers(3)
# ---------------------------------


def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
        # return 0

    # else part of the code is reached only when no error occurs
    finally:
        n_square = n ** 2
        return n_square


print(f'Answer: {power_of_two()}')


# ------- Try, Except, Finally Exercise -- Udemy..
def interact():
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer:'))     # turn the user input into an integer
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print out the message '{user_input} is {even/odd}.'

        except ValueError:
            print(f'Please input integers only.')
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit


interact()


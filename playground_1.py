print("Pavan")
a = 1
b = 2
c = 3
my_sum = a + b
print(my_sum)
math_op = 1 + 3 * 4 // 2 - 2
print(math_op)
# ----- strings ----
string1 = "hello, world"
print(string1)
single = 'pavan kumar paluri'
print(single)

name = 'pavan'
greet = 'Hello, ' + name
print(greet)

# >=3.6 convention for string concatenation (fstring)

another_greet = f'Hello, {name}'
print(another_greet)

# old way - only use the below when working with python --version <= 3.5
final_greet = 'How are you, {}'
format_greet = final_greet.format(name)
print(format_greet)

# Stdin/stdout in python
name1 = input('Enter your name: ')
greet1 = f'hello, {name1}'
print(greet1)

# Ask #age of the customer and answer back it in number of months,..
age1 = input('Enter your age ')
age_month = int(age1) * 12
greet2 = f'You have lived for {age_month} months'
print(greet2)

# input: Number of years.
# output: Number of seconds lived based on number of years.
age_sec = age_month * 30 * 24 * 60 * 60
greet3 = f'Hey bro, you have lived for fucking {age_sec} seconds until now '
print(greet3)

print("Lived for " + str(age_month) + " months")

#------ Booleans in Python ------
truthy = True
falsy = False
age = 20
is_over_age = age >= 18
print(is_over_age)
is_twenty = age == 21
print(is_twenty)

# numerical boolean comparisons in python
ny_number = 5
num1 = int(input("Enter a number "))
print(num1 == ny_number)
print(num1 != ny_number)

yes = True and True
no = True and False
age >= 18 and age < 65

absolute = not False
print(absolute)

x = 6
cmpq = False or x
print("Answer: " + str(cmpq))

# --------- Data Structures (Lists, tuples) -----------

# 1. Lists init
my_list = ['Hello', 'Pavan Kumar', 'Paluri']
# 2. Tuples init
my_tuple = ('Hello', 'Pavan Kumar', 'Paluri')
# 3. Set init
my_set = {'Hello', 'Pavan Kumar', 'Paluri'}

print(my_list)
print(my_tuple)
print(my_set)  # Why is set jumbling the order of statements (sets unordered)

my_tup1 = ('hello')  #note: This is not treated as a tuple.
my_tup2 = ('hello', )  #note: this is treated as a tuple.
print("Not tuple:" + str(my_tup1))
print("A tuple:" + str(my_tup2))

# printing particular items of list/tuples/sets
print(my_list[0])  #list's 1st item
print(my_tuple[0])  #for a tuple
# however, we cannot do the same for sets, since it is an unordered set

# few list operations
# Append to a list
my_list.append('2019')
print(my_list)

# Tuple doesnt support append
# however this can be acheived using '+'
my_tuple += ('2020', )
print(my_tuple)

# set doesnt support append as well
# we have object add for it
my_set.add('ed')
print(my_set)
# Set doesnt show up duplicates, so if we do my_set.add('hello') will not show up hello as there is a hello already in the set my_set

#----------------------- Set Operations -----------------------
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 3, 5, 7, 9}

# elementary operations on sets
set_intersection = set_1.intersection(set_2)
print(set_intersection)

set_union = set_1.union(set_2)
print(set_union)

set_diff = set_1.difference(set_2)
print(set_diff)

#-------- Exercise: Nearby friends solution ---------
nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

# Add the name to the empty set

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
name = input("Enter the name of the user: ")
user_friends.add(name)
friends_nearby = user_friends.intersection(nearby_people)
print(friends_nearby)
#-----------------------------------------------------

#------------ Dictionaries in python ---------------
# Key-value pairs
my_frnds1 = {'Pavan': 7, 'Anna': 12, 'Surabhi': 6}

# union/intersection/subtract operations cannot be done in Dictionaries
my_frnds = {
    # single key: (last_seen) and value is 6
    'Pavan': {
        'last_seen': 6
    },
    'Anna': {
        'surname': 'Smith'
    },
    'Surabhi': 6
}

# dictionary inside a list
players = [{
    'name': 'Rolf',
    'numbers': (12, 34, 5, 67, 89)
}, {
    'name': 'Jhon',
    'numbers': (1, 3, 5, 7, 9)
}]

# retreive an element of dictionary inside a list
player_1 = players[1]
# to access key/val of that dictionary
print(player_1['name'])
print(player_1['numbers'])

# sum_ups
print(sum(player_1['numbers']))
print(my_frnds['Pavan']['last_seen'])

# ----------- Length of a list ----------

grades = [23, 45, 67, 88]  #list
total = sum(grades)
print(total)
length = len(grades)
print(length)
# sum and len work for lists and tuples as well.
# len also works for dictionary and sets

# -------------- Functions and loops ------------
programmer = True

if programmer is True:
    print("You are amazing!!")

else:
    print("You need to buck up!")
if programmer:
    print("You are amazing bro!")

# -------------------- While loops ----------------------
i = 0
while i < 10:
    print(f"Repeated {i} times")
    i += 1
temp = 12
while temp < 19:
    print("heating...")
    temp += 1

# ---------------- For Loops and Functions -------------
primes = [2, 3, 5, 7, 11, 13]  #lists

for i in primes:
    print(f'{i} is a prime number')

kids_ages = (3, 7, 23)  #tuples
for age in kids_ages:
    print(f'I have {age} year old kid')

# --- range function ---
for i in range(5):
    print(f'Range gives {i}')

#iterate over Dictionaries
# name parameter is the key in each field.
for name in my_frnds1:
    print(f'I saw {name} {my_frnds1[name]} days ago')

# easier way to access entries in dictionary:
for name, values in my_frnds1.items():
    print(f'I saw {name} {values} days ago')

print(my_frnds1.items())  #prints tuples
# prints this: dict_items([('Pavan', 7), ('Anna', 12), ('Surabhi', 6)])

# now use this array of tuples in a for loop as below:
# Tuple Destructuring
for t in ([('Pavan', 7), ('Anna', 12), ('Surabhi', 6)]):
    n, v = t  # assign n and v (key,val) to t
    print(f'n value:{n}, v value:{v}')

# Searching for a key-val in a dictionary.
if ('Surabhi', 6) in my_frnds1.items():
    print("I know Surabhi")

# --- loop keywords (break & continue) ----
# continue skips the statements following in that iteration and starts with next iteration.
cars = ['ok', 'ok', 'Faulty', 'ok', 'ok']

for car_status in cars:
    if car_status is 'ok':
        print('Car is in a good condition')
    elif car_status is 'Faulty':
        print('Car is faulty, production line abort')
        break

for num in range(2, 10):
    if num % 2 is 0:
        print(f'Found an even number, {num}')
        continue
    print(f'found a {num}')

# prime number checker:
# else condition can be used in for loops: When in a nested for loop and the inner for loop condition is not satisfied for all inner for loop values, python gets into else and prints out the else.
for i in range(2, 10):
    for j in range(2, i):
        if i % j is 0:
            print(f'{i} is not a prime number')
            break
    else:
        print(f'{i} is a prime number')

# Tips:
# for repeating a loop n times, simply do this:
for i in range(3):
    print(i)  # prints 0,1,2

kids = (3, 7, 2)
for kid in kids:
    print(f'{kid} year old!')

# ----- List Slicing -----
friends = ['rolf', 'jose', 'anna', 'pavan']
print(friends[2:4])
print(friends[-1])  # displays last index

print(friends[-3:-1])

# Print last 3
print(friends[-3:])

# Prints all the list entries
print(friends[0:])

# ------- List Comprehension ------
my_list = list(range(10))  #creates a list of 10 numbers starting from 0 to 9

# Method1: to print doubled numbers in a list
# ------------------------------------
numbers = range(10)
# init an empty list
double_numbers = []
for num in numbers:
    double_numbers.append(num * 2)

print(double_numbers)

# Method2: Init and assignment on the go!
# -------------------------------------
num = range(5)
dob_num = [n * 2 for n in numbers]
print(dob_num)

phrases = [f'I am {age} years old' for age in dob_num]
print(phrases)

# To turn Uppercase text into a lowercase
list_names = ['Jhon', 'Pavan', 'Anna']
list_lower = [name.lower() for name in list_names]

print(list_lower)

# List comprehension with conditional
evens = [n for n in num if n % 2 is 0]
print(evens)

friends = ['rolf', 'anna', 'pavan']
guests = ['Jose', 'Rolf', 'PavaN', 'Mich']

guests_lower = [names.lower() for names in guests]
present_frnds = [
    names.lower() for names in friends if names.lower() in guests_lower
]

print(present_frnds)

## ---- SET AND DICTIONARY COMPREHENSION ---
# sets
friends = {'rolf', 'anna', 'pavan'}
guests = {'Jose', 'Rolf', 'PavaN', 'Mich'}

guests_low = {name.lower() for name in guests if name.lower() in friends}
print(f'Friends at the party:')
print(f'{guests_low}')
guests_capsoff = {name.lower() for name in guests}
# Efficient way to do:
print(f'New Guest List: {guests_capsoff & friends}')

# ----- Example 2 for set intersection and union operations ----
set1 = {'A', 'B', 'C', 'D'}
set2 = {'a', 'b', 'c'}
# convert set1 to lowercase
set1 = {name.lower() for name in set1}
set_common = set1 & set2
set_union = set1 | set2
print(f'Set intersection: {set_common}')
print(f'Set Union: {set_union}')

# ---
# ----- DICTIONARY comprehension ------
# Construction of a dictionary from given lists : Treat one list as a key and the other as value
namer = ['Rolf', 'Pavan', 'Pooja']
last_seen = [10, 15, 8]
last_seen_frnds = dict(zip(namer, last_seen))
print(last_seen_frnds)
gui = [name.upper() for name in namer]
print(gui)

# --- Tuple to dictionary conversion ---
uh_students = [('Jennifer', 83), ('Mitch', 11), ('Katherine', 95)]
student_dict = {name: score for name, score in uh_students}
print(f'Dictionary of UH students: {student_dict}')

# To print the corresponding value given a key.
given_key = 'jennifer'
print(f'Given_Key in Capitalized format')
print(f'{given_key.capitalize()}')
for name, score in student_dict.items():
    if name == given_key.capitalize():
        print(f'{score}')

# Important Note: Difference B/N 'is' and '==' operators.
# Helpful Link: https://www.geeksforgeeks.org/difference-operator-python/
# Understanding: we can use 'is' keyword only when the comparison is made between objects at the same memory address.

easy_dict = dict(
    uh_students)  # easy way to build a dictionary from list of tuples
print(easy_dict)

# Try exploring unzip as well.. zip(*zip(...))


# ----------------- Functions -------------
def greet():
    name = input('Enter your name')
    print(f'Hello {name}!')


greet()  # calling the function

# ------ Lambda Function --------
# Anonymous function


def add(x, y):
    return x + y


# Shortcut to do it.. using Lambda func
lambda x, y: x + y

# To invoke this lambda
# ()- call the function
(lambda x, y: x + y)(10, 5)

# First Class Function:
# Here a function can be an argument to another function


def who(user, identify_fn):
    return identify_fn(user)


def identify_fn(some_data):
    return some_data['name']


# Small Dict
user_base = {'name': 'Pavan'}

print(f'Name is {identify_fn(user_base)}')

# Now we use First Class Fn to print the entire Dictionary
els = who(user_base, identify_fn)
print(f'Entire: {els}')

# Here as an alternative, we use Lambda function to reduce the complexity
els = who(user_base, lambda x: x['name'])
print(els)


#-- classes and objects --
class Movie:
    def __init__(self, movie_name, movie_director):
        self.movie_namer = movie_name
        self.movie_directors = movie_director


my_movie = Movie('The Matrix', 'Wachowski')
print(f'Movie name: {my_movie.movie_namer}')

import json

# setup of a file
file = open('friends_json.txt', 'r') # can also implement this with "with" keyword
# open automatically closes the file without specially invoking close() function

file_contents = json.load(file)  # reads file and turns it into dictionary

# teardown
file.close()

print(f'{file_contents["friends"][0]}')  # prints details of object 0

# list of dictionaries
cars = [
    {'make': 'Ford',
     'model': 'Focus'
     },
    {
        'make': 'Ford',
        'model': 'Fiesta'
    }
 ]


# using json.dump to write to a JSON file
filer = open('cars_json.txt', 'w')
json.dump(cars, filer)
filer.close()

# Convert a Json string into a list
my_json_str = '[{"make": "Alfa Romeo", "model": "Buggatti"}]'

convert_list = json.loads(my_json_str)  # converts JSON string into dictionary
print(convert_list[0]['make'])

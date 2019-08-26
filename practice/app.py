#  Extraction of CSV files in Python
#  Example file: Extraction of state Ids and various other parameters
import csv
import json
continent_list = []
country_list = []
file = open('/Users/pavankumarpaluri/Downloads/sales.csv', 'r')
print(f'Name of the file: {file.name}')

lines = file.readlines()
print(f'CONTENT:{lines}')

file.close()

#  Take off the header from the csv file extracted
# using slicing (Get from index 1 ignoring index 0)
lines = [x.strip() for x in lines[1:]]
print(f'CONTENT:{lines}')

for line in lines:
    single_element = line.split(',')
    # extracting continent and country out of each list
    country_list.append(single_element[1])
    print(f'Single Cell:{single_element[0].split(",")}')
    continent_list.append(single_element[0])

for i in range(len(continent_list)):
    print(f'{country_list[i].capitalize()} is in {continent_list[i].title()}')


#  writing back to a csv file

sample_CSV = ','.join(['Australia', 'New Zealand', 'Pavan', 'University of Auckland'])
print(sample_CSV)


#  ---- CSV modules --------

movies = [
    {"name": "Matrix", "director": "James Cameroon"},
    {"name": "Pokemon", "director": "Sophia"},
    {"name": "Spider Man", "director": "Christopher Nolan"}
]

# Writing into a CSV file
'''
This naive implementation of writing to CSV file does not recognize
name and director as headers
'''


def naive_write_to_file(movie):
    with open("movies.csv", "w") as fo:
        writer = csv.writer(fo)
        fo.write("name, director\n")
        writer.writerows([elem.values() for elem in movie])


'''
This implementation considers headers as well
'''


def expert_write_to_file(movie):
    with open("expert_movies.csv", "w") as expert:
        field_names=['name', 'director']
        writer = csv.DictWriter(expert, fieldnames=field_names, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(movie)


expert_write_to_file(movies)
"""
Expert reading from CSV files Implementation
"""


def expert_read_from_file():
    with open("expert_movies.csv", "r") as f:
        field_names = ['name', 'director']
        reader = csv.DictReader(f)
        for liner in reader:
            print(f'name:{liner["name"]} \t Director:{liner["director"]}')
           # json.loads(liner)  # converts dictionary into JSON



expert_read_from_file()

# Reading from a CSV file


def read_from_file():
    with open("movies.csv","r") as fo:
        reader = csv.reader(fo)
        fo.readlines()
        reader.readrows([elem.values() for elem in movies])

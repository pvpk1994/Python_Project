import csv
import json
from collections import OrderedDict
# step 1
# extract csv file into list of dictionaries

list_of_dict = []

key_list = ["club", "country", "city"]

def csv_to_list():
    with open('csv_file.txt', 'r') as f:
        field_names = ["club", "city", "country"]
        for row in csv.DictReader(f, fieldnames = field_names):

            print(dict(row))  # converts into dictionary
            new_dict = OrderedDict((k, dict(row)[k]) for k in key_list)
            list_of_dict.append(new_dict)
        #print(list_of_dict)

        f.close()
        filer = open('json_file.txt', 'w')
        json.dump(list_of_dict, filer) # transferring list of dict to json
        filer.close()


csv_to_list()


#  Ask the user for a list of 3 frnds
#  For each frnd, code tells the user whether they are nearby
#  For each nearby frnd, save their name to 'nearby_frnds.txt'

# hint: readlines()

fry = []
final_list = []
counter = 0
'''
 let this function return list of all nearby frnds
 obtained from the text file
'''


def file_reader(filename):
    fo = open(filename, "r+")
    print("File Name is: ", fo.name)
    line = fo.readlines()
    print(f"Reading Line:{line}")
    print(f'Printing... {len(line)}')
    # close the file after usage
    fo.close()
    # strip whitespaces after each name in the line list
    for i in line:
        i.split()
        print('Str:{}'.format(i.split()))
        fry.append(i.split())
    print(f'List:{fry}')
    print(f'Final List: {remove_nest(fry)}')
    return remove_nest(fry)


def remove_nest(lists):
    for sublist in lists:
        for item in sublist:
            final_list.append(item)
    return final_list


def find_frnds():
    global counter

    fo = open('nearby_frnds.txt', 'a')
    while counter < 3:
        frnd = input('Enter the name of your friend:')
        if frnd in file_reader('people.txt'):
            print(f'{frnd} is nearby')
            fo.write(f"{frnd}\n")
        else:
            print(f'{frnd} is far away')
        counter += 1
    fo.close()


find_frnds()

'''
friends = file_reader("people.txt")
print(f'Friends:{friends}')

if "Priyal" in friends:
    print("Element Exists")
else:
    print("False")
'''







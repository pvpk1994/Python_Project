'''
Hacker Rank: Nested List using only Dictionaries inside Lists...
Author: Pavan Kumar Paluri
'''

'''
Input Format
The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
Constraints
2 <= N <= 5
There will always be one or more students having the second lowest grade.
Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
'''
list_students = []
list_second = []


def second_lowest_grade(list_input: list):

    list_input_new = sorted(list_input, key=lambda k: k['grade'])
    # Always remove the min item from the sorted list..
    print(list_input_new)
    # Using filer to filter out all same min elements...
    list_new = remove_same_occr_from_list(list_input_new, list_input_new[0]['grade'])
    list_new_new = remove_neg_cases(list_new)
    # print(list_new_new)
    # If there is only one element in the list..
    if len(list_new_new) == 1:
        return list_second.append(list_new_new[0]['name'])
    for i in range(1, len(list_new_new)):
        if list_new_new[0]['grade'] == list_new_new[i]['grade']:
            # if second lowest grade is same as any other student, output both the names..
            list_second.append(list_new_new[0]['name'])
            list_second.append(list_new_new[i]['name'])
        else:
            list_second.append(list_new_new[0]['name'])
        return list_second


def remove_same_occr_from_list(list_remv, val):
    return [list_remv[value] for value in range(0, len(list_remv)) if list_remv[value]['grade'] != val]

# Cover cases where grades could be negative...


def remove_neg_cases(list_neg_remv: list):
    return[list_neg_remv[val] for val in range(0, len(list_neg_remv))
           if list_neg_remv[val]['grade'] > 0]


if __name__ == '__main__':
    no_students = int(input('Enter the number of students..'))
    for _ in range(no_students):
        name = input('Enter student name:')
        grade = float(input('Enter his/her grade:'))
        list_students.append({'name': name, 'grade': grade})
    second_lowest_grade(list_students)
    list_second_new = sorted(list_second, key=lambda k: k.upper())
    for grader in list_second_new:
        print(f'{grader}')


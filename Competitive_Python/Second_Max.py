import math
'''
Find Second Largest Number - List of Integers
Author: Pavan Kumar Paluri
Source:: GeeksForGeeks
'''


def second_max(list_elem: list) -> int:
    # First for obtaining max in the list
    # Second is for obtaining second largest..
    counter = 0
    first, second = -math.inf, -math.inf
    for num in list_elem:
        counter += 1
        if num > second:
            if num >= first:
                first, second = num, first
            else:
                second = num
    return second if counter >= 2 else None


if __name__ == '__main__':
    list_elements = []
    num_test_cases = int(input())
    for case in range(num_test_cases):
        len_array = int(input())
        # No duplicates in the list entries...
        list_elements.append(list(map(int, input().rstrip().split())))
    # print(list_elements)
    for list_array in list_elements:
        print(f'Second Max is: {second_max(list_array)}')

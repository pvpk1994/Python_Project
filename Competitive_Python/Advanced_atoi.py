import math
'''
Advanced atoi() function implementation
Author:: Pavan Kumar Paluri
Source:: LeetCode (Med)
'''
INT_MIN = pow(-2, 31)
INT_MAX = pow(2, 31) - 1


def atoi(str_inp: str) -> int:
    '''
    python strings are immutable, so any modification to a given string
    generates a new string
    :param str_inp:
    :return:
    '''
    global INT_MAX, INT_MIN
    var_new = 1
    # strip function removes leading and trailing whitespaces
    str_new = str_inp.strip()
    if len(str_new) == 0:
        return 0
    # get rid of all duplicate whitespaces and newline chars.
    new_str = " ".join(str_new.split())
    new_str = new_str.replace('.', ' ')
    # To check if new_str starts with digit or not.
    # Only has to consider first occurrence of a digit
    # new_str = [s for s in new_str.split() if s.isdigit()]
    if new_str[0].isdigit() is True or new_str[0] == '+' or new_str[0] is '-':
        if new_str[0] is '-':
            new_str = new_str.strip(new_str[0])
            var_new = -1
        elif new_str[0] is '+':
            new_str = new_str.strip(new_str[0])
        # print("Yes it starts with digit / sign")
    else:
        return 0
    # int_only_str = ''.join(filter(lambda func: func.isdigit(), new_str))
    int_only_str = [s for s in new_str.split() if s.isdigit()]

    if len(int_only_str) == 0:
        return 0
    print(int_only_str)

    int_only = var_new * int(int_only_str[0])

    # print(int_only)
    if int_only < INT_MIN:
        return INT_MIN
    elif int_only > INT_MAX:
        return INT_MAX
    return int_only


if __name__ == '__main__':
    str_input = input('Enter the string')
    print(atoi(str_input))

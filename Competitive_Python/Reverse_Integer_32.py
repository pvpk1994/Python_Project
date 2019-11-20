'''
Reverse Integer - 32 bit Unsigned
Author: Pavan Kumar Paluri
Source: leetcode - Easy
Note:: The number has to lie only in the range [-2^31, 2^31-1]
'''

if __name__ == '__main__':
    number = int(input('Enter the number to be reversed:'))
    '''
    Check for 32 bit overflow with this logic...
    '''
    if number <= 0:
        number_str = str(abs(number))
    else:
        number_str = str(number)
    '''
    Just iterate through the list of string and use 
    list comprehension to slice it...
    '''
    list_slicing = [num for num in number_str]
    list_slicing.reverse()
    str_rev = ''.join(list_slicing)
    list_rev_int = list(map(int, list_slicing))
    # print(list_slicing)
    if number <= 0:
        final = int(str_rev)
        if not(final >> 31) is False:
            print(0)  # return 0
        final = -final
        print(final)
    else:
        if not(int(str_rev) >> 31) is False:
            print(0)  # return 0
        print(int(str_rev))


'''
Hacker Rank: List Comprehension
Author: Pavan Kumar Paluri
'''

'''
Description: given 3 integers, find out the ordered pairs (i,j, k) such
that i+j+k != n by using concept of list comprehensions...
'''

list_array = []

'''
This function only works fine if 2 inputs and 1 output is provided..
'''


def get_ordered_pair(var1, var2, var3, result):
    new_list = [[i, j, k] for i in range(0, var1+1) for j in range(0, var2+1)
                for k in range(0, var3+1)
                if i+j+k != result]
    return new_list


if __name__ == '__main__':
    x = int(input('Enter x:'))
    y = int(input('Enter y:'))
    z = int(input('Enter z:'))
    n = int(input('Enter value of n:'))
    print(f'{get_ordered_pair(x, y, z, n)}')

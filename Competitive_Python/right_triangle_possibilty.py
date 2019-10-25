import math
'''
Right Angle Triangle Possible ??
Author: Pavan Kumar Paluri
'''

'''
Given 4 vertices, find if its possible to construct a Right Angle Triangle
'''


def distance(num1, num2):
    sum_new = pow(num1[0] - num2[0], 2) + pow(num1[1] - num2[1], 2)
    dist = math.sqrt(sum_new)
    return dist


def find_sq(list_square: list):
    '''
    :param list_square:
    :return: Bool : true or False
    '''
    list_dist = []
    for val in range(len(list_square)):
        if val+1 <= len(list_square)-1:
            list_dist.append(distance(list_square[0], list_square[val+1]))
    print(list_dist)
    for val in range(len(list_dist)):
        for val_sub in range(len(list_dist)):
            if list_dist[val_sub] == math.sqrt(2)*list_dist[val]:
                return True
    return False


if __name__ == '__main__':
    list_sq = []
    list_sq.append([20, 10])
    list_sq.append([10, 20])
    list_sq.append([20, 20])
    list_sq.append([10, 10])
    print(find_sq(list_sq))
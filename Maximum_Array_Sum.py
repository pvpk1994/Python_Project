'''
Maximum Array Sum Problem
Source: Hacker Rank
Author: Pavan Kumar Paluri
'''
import math


def max_array_sum(array_elem: list) -> int:
    # init array
    max_elem_array = [-10001]*len(array_elem)
    max_elem_array[0] = array_elem[0]
    max_elem_array[1] = max(array_elem[0], array_elem[1])
    for index in range(2, len(array_elem)):
        # Constraint Check!
        if array_elem[index] > 10000 or array_elem[index] < -10000:
            print("Constraints not followed")
        max_elem_array[index] = max(array_elem[index], max_elem_array[index-1],
                                    array_elem[index] + max_elem_array[index - 2])
    return max(max_elem_array)


'''
    def max_elem(index):
        if max_elem_array[index] != -math.inf:
            return max_elem_array[index]
        else:
            
            return max_elem_array[index]
'''

if __name__ == '__main__':
    n = int(input())
    list_elem = list(map(int, input().strip().split()))
    # print(list_elem)
    print("max sum is: " + str(max_array_sum(list_elem)))

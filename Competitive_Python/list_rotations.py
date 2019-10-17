'''
Arrays List Rotations
Author: Pavan Kumar Paluri
Question: Hacker Rank
'''


# Complete the rotLeft function below.
def rot_left(a, d):
    # a is the list of integers in the list
    # d is the number of times left_rotate operation has to be performed
    for val in range(d):
        # always pop the first element and ...
        new_val = a.pop(0)
        # print(new_val)
        a.append(new_val)

    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    num_rot = int(nd[1])

    list_int = list(map(int, input().rstrip().split()))

    print(rot_left(list_int, num_rot))

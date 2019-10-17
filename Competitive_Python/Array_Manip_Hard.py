'''
Array Manipulation _Hard problem
Author: Pavan Kumar Paluri
Working Code: Time Complexity has to be brought down...
'''


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries, m):
    list_add = []
    # Load init array with n num of 0's.
    for val in range(1, n+1):
        list_add.append(0)
    for i in range(m):
        left_index = queries[i][0]
        right_index = queries[i][1]
        summand = queries[i][2]
        for val in range(left_index-1, right_index):
            list_add[val] += summand
    # print(list_add)
    return max(list_add)


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    print(arrayManipulation(n, queries, m))


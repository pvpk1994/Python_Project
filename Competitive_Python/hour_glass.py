'''
Hour glasses Max sum Problem
Author: Pavan Kumar Paluri
Source: HackerRank
'''

'''
Description:
Given a 6*6 matrix with int values and we need to find all 
possible hour glasses and then sum all the elements of such 
possible hour glasses and then return the maximum of such sums
'''


def hour_glass(arr: list) -> int:

    entries_sum = []
    x = 0
    for i in range(4):
        count = 0
        limit = 3
        j = 0
        sum_var, sum_var1 = [], []
        while count <= 9:
            # print(f'{count}')
            if j == 2 or j == 3 or j == 4:
                j = j-1
                if j == 1:
                    limit = 4
                elif j == 2:
                    limit = 5
                elif j == 3:
                    limit = 6
                for j in range(j, limit):
                    # print(f'j val: {j}')
                    if count == 0 or count == 3 or count == 6 or count == 9:
                        sum_var.append(arr[i+1][j+1])  # will get the middle element of the hour glass
                    count += 1
                    sum_var.append(arr[i][j])
                    sum_var.append(arr[i+2][j])
            else:
                for j in range(limit):

                    if count == 0 or count == 3 or count == 6:
                        sum_var.append(arr[i+1][j+1])  # will get the middle element of the hour glass
                    count += 1
                    sum_var.append(arr[i][j])
                    sum_var.append(arr[i+2][j])
            # print(sum_var)
            entries_sum.append(sum(sum_var))
            sum_var.clear()
            # print(sum_var)
        # break

    # print(max(entries_sum))
    return max(entries_sum)


if __name__ == '__main__':
    list_arr = []
    for _ in range(6):
        list_arr.append(list(map(int, input().rstrip().split())))
    result = hour_glass(list_arr)
    print(result)

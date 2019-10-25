'''
Leet Code
Two Sum Problem: Easy type
Author: Pavan Kumar Paluri
'''

list_num = [2, 5, 1, 7, 3]


# Return the indices of the list entities that add up to given sum
# Runtime: 6800ms
def sum_two(list_sum: list, target_num: int):
    list_index = []
    for i in range(len(list_sum)):
        for j in range(i):
            if list_sum[i] + list_sum[j] == target_num:
                list_index.append(j)
                list_index.append(i)
    return list_index


# Advanced approach...
# Runtime: 300ms
def sum_adv(list_sum: list, target: int):
    list_new_adv = []
    counter = 0
    for val in range(len(list_sum)):
        list_new_adv.append(target-list_sum[val])
        if list_new_adv[val] == list_sum[val] and counter == 0:
            counter += 1
            continue
        if list_sum[val] in list_new_adv:
            return [list_new_adv.index(list_sum[val]), val]


if __name__ == '__main__':
    target_sum = 9
    print(sum_adv(list_num, target_sum))
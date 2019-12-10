
'''
To find the length of a longest substring (non-repeating)
Author: Pavan Kumar Paluri
Source: LeetCode (Medium) - Accepted Version!!
'''


def split_string(str_i:   str) -> list:
    return list(str_i)


def find_longest_substring(str_inp: str) -> int:
    len_str = []
    i_ = 0
    if len(str_inp) == 0:
        return 0
    list_str = split_string(str_inp)
    unordered_set = []
    for i in range(len(list_str)):
        if list_str[i] in unordered_set:
            len_str.append(len(unordered_set))
            j = 0
            index_num = unordered_set.index(list_str[i])
            # print(f'index_num is {index_num}')
            while j <= index_num:
                unordered_set.pop(0)
                j += 1
            # unordered_set.clear()
        unordered_set.append(list_str[i])
    len_str.append(len(unordered_set))
    return max(len_str)


if __name__ == '__main__':
    given_str = input()
    print(find_longest_substring(given_str))
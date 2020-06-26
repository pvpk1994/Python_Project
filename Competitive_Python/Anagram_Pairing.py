import collections
from collections import Counter

# Anagrams Pairing
# Author: Pavan Kumar Paluri


def make_anagram(str_a: str, str_b: str):
    # get len of strs (a,b)
    len_a = len(str_a)
    len_b = len(str_b)
    total_len = len_a + len_b

    # Cast Counter to a dict
    dict_str_a = dict(Counter(str_a))

    # strip b into char list
    b_list = list(str_b.strip())
    counter = 0
    for char in b_list:
        if char in dict_str_a and dict_str_a[char] > 0:
            counter += 2
            dict_str_a[char] -= 1
    return total_len - counter


if __name__ == '__main__':
    a = input()
    b = input()
    print(make_anagram(a, b))
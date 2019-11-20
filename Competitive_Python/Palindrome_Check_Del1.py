import re
'''
Palindrome Check with atmost one deletion
Source:: LeetCode
Author: Pavan Kumar Paluri
'''

'''
Time limit exceeded but workable version..
Time Complexity: O(N^2) since we are iterating through the same list twice.
'''


def reversal(str_input: str) -> str:
    # Perform a reversal of str on given str
    str_new = ''.join(reversed(str_input))
    return str_new


def palindrome_check(str_unrev: str, str_rev: str) -> bool:
    if str_rev == str_unrev:
        return True


def palindrome_check_del1(str_input: str) -> bool:
    # Get str len
    str_store = str_input
    str_len = len(str_input)
    if str_len > 50000:
        return False
    # If case
    temp_res = palindrome_check(str_input, reversal(str_input))
    if temp_res is True:
        return True
    counter_occ = 0
    # Else case
    for i in range(str_len):
        str_input_n = str_store
        # Keep replacing one word at a time with ''
        # new str excludes ith letter in the string
        new_str = str_input_n[:i] + str_input_n[i+1:]
        print(new_str)
        result = palindrome_check(new_str, reversal(new_str))
        if result is True:
            return True
    return False

'''
This function validPalindrome() runs in O(N) time complexity 
'''


def validPalindrome(s: str) -> bool:
    n = len(s)
    for i in range(n // 2 + 1):
        if s[i] != s[~i]:
            print(f's[i+1 : n-i] is {s[i+1: n-i]}')
            print(f's[i+1: n-i] reverse is {s[i+1 : n-i][::-1]}')
            print(f's[i : ~i] is {s[i : ~i]}')
            print(f's[i : ~i] reverse is {s[i: ~i][::-1]}')
            return s[i + 1:n - i] == s[i + 1:n - i][::-1] or s[i:~i] == s[i:~i][::-1]
    return True


if __name__ == '__main__':
    str_inp = input('Enter the string: ')
    print(palindrome_check_del1(str_inp))
    print(validPalindrome(str_inp))

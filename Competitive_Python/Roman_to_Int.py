'''
Roman to Integer Conversion
Author: Pavan Kumar Paluri
Source: Leet Code - Easy
'''


def roman_to_int(str_in: str) -> int:
    '''
    store vals in dictionary
    '''
    int_num = 0
    dict_store = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    # iterate through a string without having to slice it.
    # Up until last character
    i = 0
    while i < len(str_in)-1:
        if dict_store[str_in[i]] >= dict_store[str_in[i+1]]:
            int_num += dict_store[str_in[i]]

        elif dict_store[str_in[i]] < dict_store[str_in[i+1]]:
            int_num += dict_store[str_in[i+1]] - dict_store[str_in[i]]
            i += 1
        i += 1
    if i == len(str_in)-1:
        int_num += dict_store[str_in[len(str_in)-1]]
    return int_num


if __name__ == '__main__':
    str_input = input()
    print(roman_to_int(str_input))

list_reverse = [0, 5, 4, 4, 0]


def concat(list_num: list) -> int:

    final_res = 0
    for numb in range(len(list_num)):
        final_res += list_num[numb] * (10 ** (len(list_num)-1 - numb))
    return final_res

# Using enumerate function


def concat_enum(list_n: list) -> int:
    final_r = 0
    for index, num in enumerate(list_n):
        final_r += num * pow(10, (len(list_n)-1 - index))
    return final_r


print(concat(list_reverse))
print(concat_enum(list_reverse))

from collections import deque
# Common Child Python
# Author: Pavan Kumar Paluri


def common_child(s1: str, s2: str) -> int:

    counter = 0
    # Parse the strings into list of chars
    list_s1 = deque(list(s1.strip()))
    list_s2 = list(s2.strip())

    for char in list_s2:
        # if char in list_s1 increment the counter
        # and delete the list_s1 until that char part
        # print(list_s1)
        if char in list_s1:
            counter += 1
            for _ in range(0, list_s1.index(char) + 1):
                list_s1.popleft()
        else:
            continue
    return counter


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(common_child(str1, str2))
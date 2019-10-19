'''
Digit Scoring
Author: Pavan Kumar Paluri
'''

score = 0


def get_score(number: int):
    global score
    counter = 1
    counter_tuple = 1
    counter_2 = 0
    counter_rem = 0
    # given number is in int,
    # Split it into digits to calculate scoring
    # Convert int into string
    list_number = list(str(number))
    # list_number is in string
    list_new_num = list(map(int, list_number))
    print(list_new_num)

    # Condition 1: Given number is multiple of 3, add 4 to the score
    if number % 3 == 0:
        score += 4
    for val in range(len(list_new_num)):
        if list_new_num[val] % 2 == 0:
            score += 3
        if list_new_num[val] == 7:
            score += 5
        if val+1 <= len(list_new_num)-1:
            if list_new_num[val] == list_new_num[val+1] == 2 and counter_2 < 1:
                score += 6
                counter_2 += 1

            if list_new_num[val] == 2 and counter_2 > 1:
                score += 6
            if list_new_num[val] - list_new_num[val+1] == 1:
                # counter = 1
                counter += 1
                counter_tuple += 1
                # counter = 0

            elif list_new_num[val] - list_new_num[val+1] != 1 and counter >= 2:
                score += pow(counter, 2)
                counter = 1
                counter_rem += 1

                # now if we reach the end of list.. compute the following
        else:
            if val == len(list_new_num)-1 and counter_rem > 1:
                rem_elements = val - counter_tuple-1
                score += rem_elements
    if counter > 1:
        score += pow(counter, 2)
    return score


if __name__ == '__main__':
    # given a number
    num = int(input('Enter the number:'))
    print(f'Score is:{get_score(num)}')


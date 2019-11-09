'''
Santa - Elves and various type of Recursion
Type: Easy
Author: Pavan Kumar Paluri
Source: Self-Developed
'''

'''
Description: Santa has to deliver gifts to given list of houses,
however, since Santa is an old man, he cannot deliver gifts to each house which rules out the 
possibility of iteration. So Santa has to appoint elves to deliver gifts to each and every house in the list.
This can therefore be achieved by recursion.
'''
list_houses = ['Kenny', 'Charles', ' Anna', 'Jessica', 'Monica', 'Rachel', 'Joey', 'Ross', 'Chandler']


def gift_delivery(list_house: list) -> None:
    '''
    If this is the last house, appoint an elf to deliver it...
    :param list_house:
    :return:
    '''
    if len(list_house) == 1:
        house = list_house[0]
        print(f'The gift is delivered to {house}')
    elif len(list_house) > 0:
        '''
        Santa appoints an elf which appoints elf and so on...
        '''
        mid = len(list_house) // 2
        first_set = list_house[:mid]
        second_set = list_house[mid:]
        gift_delivery(first_set)
        gift_delivery(second_set)


'''
Threaded recursion,
passing the updated current state to each recursive call as arguments
'''


def sum_n(current_number: int, cum_sum: int) -> int:
    if current_number == 3:
        return cum_sum
    else:
        current_number += 1
        return sum_n(current_number, cum_sum + current_number-1)

'''
Recursive List element addition to the head of a given list
'''


def add_to_head(element: int, list_given: list) -> list:
    return [element] + list_given


if __name__ == '__main__':
    gift_delivery(list_houses)
    print(sum_n(1, 0))
    list_new = []
    # Recursive additions to the same list -> to head
    list_new = add_to_head(1, add_to_head(2, add_to_head(3, add_to_head(4, add_to_head(5, list_new)))))
    print(list_new)

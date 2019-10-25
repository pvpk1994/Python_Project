from collections import Counter
from itertools import *


def get_nth_index(lst, item, n):
    c = count()
    return next(i for i, j in enumerate(lst) if j == 's' and next(c) == n-1)


def check_log_history(events_list: list) -> int:
    new_event_list = []
    counter = 0
    events_list_acquire = []
    events_list_release = []
    '''
    for val in events_list:
        counter += 1
        res, val1 = val.split(' ')
        new_event_list.append([res, int(val1)])

        if new_event_list[val.index(val)][0].__eq__('ACQUIRE'):
            events_list_acquire.append(new_event_list[val.index(val)])
        else:
            events_list_release.append(new_event_list[val.index(val)])
    '''
    for val in range(len(events_list)):
        lock_name, value = events_list[val].split(' ')
        new_event_list.append([str(lock_name), int(value)])
        if new_event_list[val][0].__eq__('ACQUIRE'):
            events_list_acquire.append(new_event_list[val][1])
        else:
            '''
            if Acquire is followed by a release, 
            '''
            events_list_release.append(new_event_list[val][1])
            events_list_release.reverse()
    list_common = [entry for entry in events_list_release if entry in events_list_acquire]
    list_no_release = [entry for entry in events_list_release if entry not in events_list_acquire]
    list_no_acquire = [entry for entry in events_list_acquire if entry not in events_list_release]
    new_dict = dict(Counter(list_no_release))
    new_dict_acq = dict(Counter(list_no_acquire))
    for key, val in new_dict_acq.items():
        if val > 1:
            print(f'Trying to re-acquire lock {key}....')
            '''
            If trying to acquire an already held lock...,
            return the event number in such cases
            '''
            return get_nth_index(new_event_list, key, )
        else:
            break
    for key, val in new_dict.items():
        if val > 1:
            print(f'Trying to re-release lock {key}.....')
            return len(events_list) + 1
        else:
            break
    # print(dict(Counter(list_no_acquire)))
    print(str(new_event_list))
    print(events_list_acquire)
    print(events_list_release)
    print(list_common)
    print(list_no_release)
    print(list_no_acquire)


if __name__ == '__main__':
    event_count = int(input().strip())
    events = []
    for _ in range(event_count):
        events_item = input()
        events.append(events_item)

    print(check_log_history(events))
    # print(events)

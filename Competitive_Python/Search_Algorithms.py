import math
'''
Various Search Algorithms
Author: Pavan Kumar Paluri
'''


# Linear Search
# Time Complexity: O(n) (since in worst case the element wanting to be searched could be at the very end...)
def linear_search(list_search: list, val: int) -> int:
    if list_search is None:
        raise AssertionError('List is Empty.. cannot be searched')
    for num in list_search:
        if num == val:
            return list_search.index(num)
    return -1


# binary Search
# Time Complexity: O(logn) since the list is sub-divided into left and right subarrays with mid as pivot..
def binary_search(list_search: list, start: int, end: int, index: int) -> int:
    if list_search is None:
        raise AssertionError('List is Empty... Cannot be Searched')
    if end >= start:
        mid = int(start + (end - start)/2)
        if list_search[mid] == index:
            return mid
        # If index is greater than mid element, explore thr right subarray
        elif list_search[mid] < index:
            return binary_search(list_search, mid+1, end, index)
        # Else, the only option left is to explore the left subarray
        else:
            return binary_search(list_search, start, mid-1, index)
    # If end is less than start, return invalid
    else:
        return -1


# Jump Search
# Time Complexity: O(n^1/2) - since each interval is between consecutive sqrt(n)'s
# Performs better than linear search but not than Binary search
def jump_search(list_jumper: list, n: int, index: int) -> int:
    # Compute step
    step = math.sqrt(n)
    prev = 0
    while list_jumper[int(min(step, n)-1)] < index:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    # Perform Iterative Search...
    while list_jumper[int(prev)] < index:
        prev += 1

        # If we reach the end of next step...
        if int(prev) == int(min(step, n)):
            return -1

    # Out of this, we check for index == list_jumper[prev]
    if list_jumper[int(prev)] == index:
        return int(prev)

    return -1


# Interpolation Search
# Time Complexity: O(log log n) if uniformly distributed, else O(n)
def interpolation_search(list_probe: list, index: int) -> int:
    # Firstly, set low and high
    low = 0
    high = len(list_probe) - 1
    while low <= high and index <= list_probe[high] and index >= list_probe[low]:
        if low == high:
            if list_probe[low] == index:
                return low
            return -1
        # Begin Probe_position calc...
        # probe_pos = low + int((index - list_probe[low] * (high - low)/ list_probe[high] - list_probe[low]))
        probe_pos = low + int(((float(high - low) /
                         (list_probe[high] - list_probe[low])) * (index - list_probe[low])))
        if list_probe[probe_pos] == index:
            return probe_pos
        if list_probe[probe_pos] < index:
            # Explore only the positions after current probe_pos until end
            low = probe_pos+1
        elif list_probe[probe_pos] > index:
            high = probe_pos - 1
    return -1


# Exponential Search
# Time Complexity: O(log n) since it does a binary search within the final interval
#  after narrowing down on the range of execution...
def exponential_search(list_exp: list, index: int):
    if list_exp[0] == index:
        return 0
    i = 1
    while i < len(list_exp) and list_exp[i] <= index:
        i = i*2
    # after exiting the while loop, we are sure the value will somewhere be b/n i/2 and min(i,n)..
    return binary_search(list_exp, i/2, min(i, len(list_exp)), index)


if __name__ == '__main__':
    key = 21
    # List need not be sorted for linear search
    list_linear = [10, 30, 80, 50, 70, 21]
    # List has to be sorted for Binary Search
    list_binary = sorted(list_linear, key=lambda k: k)
    # list_binary = [2, 3, 4, 10, 40]
    print(list_binary)
    print(f'Linear Search: Element is at index: {linear_search(list_linear, key)}')
    print(f'Binary Search: Element is at index: {binary_search(list_binary, 0, len(list_binary)-1, key)}')
    print(f'Jump Search: Element is at index: {jump_search(list_binary, len(list_binary), key)}')
    print(f'Interpolation Search: Element is at index: {interpolation_search(list_binary, key)}')
    print(f'Exponential Search: Element is at index: {exponential_search(list_binary, key)}')

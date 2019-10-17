'''
Minimum Swaps
Author: Pavan Kumar Paluri
Source: Hacker Rank
'''

'''
Description: Given an unsorted array of integers (without any duplicates)
, obtain the sorted array with minimum number of swaps
'''


# Function returns the minimum
# number of swaps required to sort the array
def min_swaps(arr):
    n = len(arr)

    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    # arrpos = [*enumerate(arr)]
    arrpos = list(enumerate(arr))
    print(arrpos)
    # Sort the array by array element i.e., arrpos[1]
    arrpos.sort(key=lambda it: it[1])
    print(f'arrpos Sorted: {arrpos}')
    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}
    print(vis)
    # Initialize result
    ans = 0
    for i in range(n):

        # already swapped or
        # already present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            print(vis[i])
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:  # is False
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
        # return answer
    return ans


# Driver Code
arr = [2, 3, 4, 1, 5]
print(min_swaps(arr))


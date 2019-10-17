from collections import Counter
'''
Pairing Socks Challenge:
Author: Pavan Kumar Paluri
'''

'''
Description: 
sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock

Output Format
Return the total number of matching pairs of socks that John can sell.
'''


def sock_merchant(number: int, ar: list):
    list_pairs = sorted(ar, key=lambda k: k)
    # After sorting, we now try to get pairs of integers in the list...
    '''
    list_new_pairs = [[list_pairs[i], list_pairs[j]] for i in range(0,number)
                      for j in range(i) if list_pairs[i] == list_pairs[j]]
    '''
    list_frequency = dict(Counter(list_pairs))
    counter = 0
    for val in list_frequency.values():
        counter += int(val/2)
    return counter


# main
if __name__ == '__main__':
    # Write into the file using OS packages...
    f = open("Output_file.txt", "a")
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    if len(ar) < n:
        raise AssertionError('Please enter all the numbers')
    print(sock_merchant(n, ar))
    f.write(str(ar))
    f.close()


'''
Given n servers with its backup file.
Output the number of ways in which we can make sure that
none of the servers have their own backup at all times
Author: Pavan Kumar Paluri
'''

'''
Count(number) = number-1(Count(number-1) + Count(number-2))
Naive solution is to use Brute-force Recursion 
as given by count_derange() function in this code

Issue: Issue with this code is that it slows down drastically as the size of number
keeps growing making it inefficient. Therefore it is advisable to have 
'''


class Solution:
    def __init__(self, s_num):
        self.s_num = s_num

    def count_derange(self, snum):
        # if set only has 1 element, no derangements possible
        if snum == 1:
            return 0
        if snum == 2:
            return 1
        else:
            return (snum-1)*(self.count_derange(snum-1) + self.count_derange(snum-2))

    def recursive_brute_force(self):
        return self.count_derange(self.s_num)


if __name__ == '__main__':
    for i in range(1, 64):
        n = Solution(i).recursive_brute_force()
        print(f'Total possible derangments for {i} -> {n}')
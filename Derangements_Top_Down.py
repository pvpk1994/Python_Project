'''
Solving the derangement's problem with Dynamic Programming
using Top-Down / Memoization technique
Author: Pavan Kumar Paluri
'''


class Solution:
    def __init__(self, number):
        self.num = number
        self.mem_store = [-1]*(self.num+1)

    def self_compute_top_down(self, num_er):
        # if the array index of num_er is not -1, then retrieve the index
        if self.mem_store[num_er] != -1:
            return self.mem_store[num_er]
        if num_er == 1:
            return 0
        if num_er == 2:
            return 1
        result = (num_er-1)*(self.self_compute_top_down(num_er-1) + self.self_compute_top_down(num_er-2))
        # store the result in the memotized array
        self.mem_store[num_er] = result
        return result

    # use recurrence relation to compute but rather than computing
    # already computed values, the best way is to store it in an memotized
    # array and retrieve them when needed
    def self_compute(self):
        return self.self_compute_top_down(self.num)


if __name__ == '__main__':
    for i in range(1, 64):
        print(f'result of {i} -> {Solution(i).self_compute()}')
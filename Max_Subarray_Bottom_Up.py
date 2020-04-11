'''
Max Subarray Bottom Up solution
Author: Pavan Kumar Paluri
DP- using Bottom Up solution
'''


class max_subarray_bottom_up:
    def __init__(self, list_elem: list):
        self.list_elem = list_elem
        # Pre-compute everything for usage straightaway
        self.list_mem = [-1]*(len(self.list_elem))
        for index in range(0, len(self.list_elem)):
            if index == 0:
                self.list_mem[index] = self.list_elem[index]

            if self.list_mem[index] == -1:
                self.list_mem[index] = max(self.list_elem[index], self.list_elem[index] +
                                      self.list_mem[index-1])

    def max_sub(self):
        # for index in range(0, len(self.list_mem)):
        return max(max(self.list_mem), 0)


if __name__ == '__main__':
    list_elem = [2, 3, -5]
    # list_elem = [5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]
    # list_elem_s = [1]*900
    for _ in range(10):
        print(f'The max result is: {max_subarray_bottom_up(list_elem).max_sub()}')
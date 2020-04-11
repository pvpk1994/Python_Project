'''
Maximum Subarray Memory Optimized Problem
Author: Pavan Kumar Paluri
Topic: DP- Memory Optimization on Bottom-Up
'''


class max_sub_mem_opt:
    def __init__(self, list_elem: list):
        self.list_elem = list_elem
        self.var1, self.var2 = -1, -1
        for elem in range(0, len(self.list_elem)):
            if elem == 0:
                self.var1 = self.list_elem[elem]
            else:
                self.var2 = max(self.list_elem[elem], self.list_elem[elem] + self.var1)
                if self.var2 > self.var1:
                    self.var1 = self.var2

    def ret_max(self):
        return self.var2


if __name__ == '__main__':
    list_elems = [2, 3, -5]
    print(f'Max result is {max_sub_mem_opt(list_elems).ret_max()}')






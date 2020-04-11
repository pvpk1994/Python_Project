'''
Optimized Max Subarray problem
Author : Pavan Kumar Paluri
Topic: Dynamic Programming - Memory Optimized Bottom Up Solution
'''


class max_sub_array_bottom_up_mem_opt:
    def __init__(self, list_el: list):
        self.list_el = list_el
        self.var1, self.var2 = 0, 0
        for index in range(0, len(self.list_el)):
            if index == 0:
                self.var1 = self.list_el[index]
            else:
                self.var1 = max(self.list_el[index], self.list_el[index] + self.var1)
            self.var2 = max(self.var1, self.var2)

    def get_max(self):
        return self.var2


if __name__ == '__main__':
    # list_int = [2, 3, -5]
    list_int = [5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]
    print(f'Max subarray result is: {max_sub_array_bottom_up_mem_opt(list_int).get_max()}')



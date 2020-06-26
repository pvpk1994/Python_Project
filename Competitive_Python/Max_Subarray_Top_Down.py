'''
Max Subarray problem
Author: Pavan Kumar Paluri
Using DP-Top Down Memoization Technique
'''


class max_sub:
    def __init__(self, list_int: list):
        self.list_int = list_int
        self.list_store = [-1]*(len(self.list_int))

    def at_element(self, index):
        if index == 0:
            self.list_store[index] = self.list_int[index]
            return self.list_int[index]
        if self.list_store[index] != -1:
            return self.list_store[index]
        else:
            self.list_store[index] = max(self.list_int[index], self.list_int[index] + self.at_element(index - 1))
            return self.list_store[index]

    def max_subelem(self):
        for index in range(len(self.list_int)-1, -1, -1):
            if index > 0:
                self.at_element(index)
        return max(max(self.list_store), 0)


if __name__ == '__main__':
    list_elements = [2, -3, -5]
    # list_elements = [5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]
    # larger list
    #list_elements = [1]*900
    #for _ in range(10):
    print(f'Max sum is {max_sub(list_elements).max_subelem()}')


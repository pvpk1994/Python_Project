'''
Maximum Subarray Problem using Brute-Force Approach
Author: Pavan Kumar Paluri
Method: Brute Force using Recursion
'''


class max_array:
    def __init__(self, list_int: list):
        self.list_int = list_int

    def at_element(self, index):
        # stopping condition
        if index == 0:
            return self.list_int[index]
        return max(self.list_int[index], self.list_int[index] + self.at_element(index-1))

    def max_subarray(self):
        max_elem_list = [0, ]
        for index in range(len(self.list_int)-1, -1, -1):
            if index > 0:
                max_elem_list.append(self.at_element(index))
        return max(max_elem_list)


if __name__ == '__main__':
    # list_sample = [2, 3, 5, -3]
    # list_sample = [5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3]
    list_sample = [5, -4, 8]
    # larger list
    # list_sample = [1]*900
    # for i in range(10):
    print(f'Max subarray result is {max_array(list_sample).max_subarray()}')




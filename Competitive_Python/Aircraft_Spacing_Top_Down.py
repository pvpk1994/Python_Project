'''
Aircraft spacing problem
Top-Down Recursive using Dynamic Programming
Author: Pavan Kumar Paluri
'''


class Aircraft_Space:
    def __init__(self, aircraft_list: list):
        self.aircraft_list = aircraft_list
        self.aircraft_storage = [-1]*(len(self.aircraft_list))

    def spacing(self, iter):
        if iter >= len(self.aircraft_list):
            return 0
        # If mem array has a different val than -1, simply return it
        if self.aircraft_storage[iter] != -1:
            return self.aircraft_storage[iter]
        spacing_first = self.aircraft_list[iter] + self.spacing(iter + 2)
        not_spacing_first = self.spacing(iter + 1)
        self.aircraft_storage[iter] = max(spacing_first, not_spacing_first)
        # return max(spacing_first, not_spacing_first)
        return self.aircraft_storage[iter]


if __name__ == '__main__':
    # space_list = [155, 55, 2, 96, 67, 203, 3]
    space_list = [1]*1000
    '''
    space_list = [155, 55, 2, 96, 67, 203, 3, 66, 32, 65, 29, 8, 299
                  , 323, 77, 3, 28, 128, 19, 523, 372, 2, 3, 66, 124, 38, 34
                  , 12, 88, 23, 74, 65, 87, 434, 14, 7, 49, 38, 27, 641, 61, 58
                  , 14, 57, 71, 11, 82, 178, 93, 191, 4]
    '''
    print(Aircraft_Space(space_list).spacing(0))

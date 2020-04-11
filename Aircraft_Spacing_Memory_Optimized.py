'''
Aircraft Spacing Problem with Memory Optimization
Author: Pavan Kumar Paluri
Topic: Dynamic Programming
'''


class Aircraft_Memory_Optimize:
    def __init__(self, plane_list: list):
        self.plane_list = plane_list
        self.i, i_plus_1, i_plus_2 = -1, -1, -1
        for plane in range(len(self.plane_list) - 1, -1, -1):
            self.i = self.plane_list[plane]
            first_select = self.i + (i_plus_2 if plane+2 < len(self.plane_list) else 0)
            not_first_select = i_plus_1 if plane + 1 < len(self.plane_list) else 0
            max_plus = max(first_select, not_first_select)
            self.i = max_plus
            i_plus_2 = i_plus_1
            i_plus_1 = self.i

    def plane_sequence(self):
        return self.i


if __name__ == '__main__':
    # space_list = [155, 55, 2, 96, 67, 203, 3]
    # space_list = [1, 5, 3, 1, 2]

    space_list = [155, 55, 2, 96, 67, 203, 3, 66, 32, 65, 29, 8, 299
                  , 323, 77, 3, 28, 128, 19, 523, 372, 2, 3, 66, 124, 38, 34
                  , 12, 88, 23, 74, 65, 87, 434, 14, 7, 49, 38, 27, 641, 61, 58
                  , 14, 57, 71, 11, 82, 178, 93, 191, 4]
    print(Aircraft_Memory_Optimize(space_list).plane_sequence())
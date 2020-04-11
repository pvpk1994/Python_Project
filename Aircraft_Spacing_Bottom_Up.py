'''
Aircraft Spacing Problem
Bottom Up Approach
Author: Pavan Kumar Paluri
'''


class Aircraft_Bottom_Up:
    def __init__(self, plane_list: list):
        self.plane_list = plane_list
        # Pre-compute at the very beginning and store it in a mem array
        self.plane_mem = [-1] * len(plane_list)
        for plane in range(len(plane_list)-1, -1, -1):
            first_select = self.plane_list[plane] + (self.plane_mem[plane + 2] if plane+2 < len(plane_list) else 0)
            not_first_select = (self.plane_mem[plane + 1] if plane+1 < len(plane_list) else 0)
            self.plane_mem[plane] = max(first_select, not_first_select)

    def plane_sort(self):
        return self.plane_mem[0]


if __name__ == '__main__':
    # space_list = [155, 55, 2, 96, 67, 203, 3]
    # space_list = [1, 5, 3, 1, 2]

    space_list = [155, 55, 2, 96, 67, 203, 3, 66, 32, 65, 29, 8, 299
                  , 323, 77, 3, 28, 128, 19, 523, 372, 2, 3, 66, 124, 38, 34
                  , 12, 88, 23, 74, 65, 87, 434, 14, 7, 49, 38, 27, 641, 61, 58
                  , 14, 57, 71, 11, 82, 178, 93, 191, 4]

    print(Aircraft_Bottom_Up(space_list).plane_sort())
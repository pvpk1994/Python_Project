'''
Aircraft spacing problem.
Using Brute Force Recursive solution - ineffecient yet workable version
'''


class aircraft:
    def __init__(self, plane_list: list):
        self.plane_list = plane_list

    def craft_spacing(self, plane_i):
        # Stopping condition
        if plane_i >= len(self.plane_list):
            return 0
        first_select = self.plane_list[plane_i] + self.craft_spacing(plane_i + 2)
        not_first_select = self.craft_spacing(plane_i + 1)
        print(f'random')
        # return max(first_select, not_first_select)


if __name__ == 'main':
    aircraft_list = [155, 55, 2, 96, 67, 203, 3]
    air = aircraft(aircraft_list)
    print(f'{air.craft_spacing(3849)}')

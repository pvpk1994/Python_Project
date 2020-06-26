'''
Full Bus Tour Dynamic Programming
Author: Pavan Kumar Paluri
'''


class full_bus_top_down:
    def __init__(self, grp_list, full_cap):
        self.grp_list = grp_list
        self.full_cap = full_cap
        # Init a 2D array to keep track of changing length and changing full_cap param
        self.list_entr = [[]] * (len(self.grp_list) + 1)
        # Now fill the inner cols with number of caps
        for i in range(0, len(self.grp_list)+1):
            self.list_entr[i] = [None]*(self.full_cap + 1)

    def fill_table(self, len_grp, c):
        # Stopping Conditions
        if c == 0:
            return True
        if len_grp == 0:
            return False
        if self.list_entr[len_grp][c] is not None:
            return self.list_entr[len_grp][c]
        c_rem = c - self.grp_list[len_grp - 1]
        self.list_entr[len_grp][c] = (self.fill_table(len_grp - 1, c)) or (c_rem >= 0
                                                                           and self.fill_table(len_grp-1, c_rem))
        return self.list_entr[len_grp][c]

    def print_tab_result(self):
        return self.fill_table(len(self.grp_list), self.full_cap)


if __name__ == '__main__':
    list_entries = [4, 5, 1, 8]
    bus = full_bus_top_down(list_entries, 11)
    print(bus.print_tab_result())



'''
Full Bus Tour Problem
Author: Pavan Kumar Paluri
'''


class full_bus_tour:
    def __init__(self, group_sizes, full_cap):
        self.group_sizes = group_sizes
        self.full_cap = full_cap
        # Use shallow copy concept to bring down the size of enumeration list

        for elem in self.group_sizes[:]:
            if elem > self.full_cap:
                self.group_sizes.pop(self.group_sizes.index(elem))

        self.result = 0

    def result_judge(self, len_grp, cap):
        # Stopping conditions
        if cap == 0:
            return True
        if len_grp == 0:
            return False
        cap_remain_val = cap - self.group_sizes[len_grp - 1]
        return self.result_judge(len_grp - 1, cap) or (cap_remain_val >= 0
                                                       and self.result_judge(len_grp - 1, cap_remain_val))

    def final_res(self):
        return self.result_judge(len(self.group_sizes), self.full_cap)


if __name__ == '__main__':
    grp = [4, 4, 5, 12, 6, 1, 8]
    # grp = [1, 1, 1]
    bus_fit = full_bus_tour(grp, 3)
    print(bus_fit.final_res())
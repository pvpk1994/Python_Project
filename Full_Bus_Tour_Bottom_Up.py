'''
Full Bus Tour Bottom Up Approach
Author: Pavan Kumar Paluri
Dynamic Programming
'''


class full_bus_tour_bottom_up:
    def __init__(self, list_grp: list, max_cap: int):
        self.list_grp = list_grp
        self.max_cap = max_cap
        # Create a 2D array
        self.two_d_arr = [[]] * (len(self.list_grp) + 1)
        for a in range(0, len(self.list_grp)+1):
            self.two_d_arr[a] = [None] * (self.max_cap + 1)
            for b in range(0, self.max_cap+1):
                # Stopping condition
                if b == 0:
                    self.two_d_arr[a][b] = True
                elif a == 0:
                    self.two_d_arr[a][b] = False
                else:
                    cap_rem = b - self.list_grp[a - 1]
                    self.two_d_arr[a][b] = (self.two_d_arr[a-1][b]) or (cap_rem >= 0
                                                                        and self.two_d_arr[a-1][cap_rem])

    def print_val(self):
        return self.two_d_arr[len(self.list_grp)][self.max_cap]


if __name__ == '__main__':
    grp = [4, 5, 1, 8]
    bus = full_bus_tour_bottom_up(grp, 11)
    print(bus.print_val())
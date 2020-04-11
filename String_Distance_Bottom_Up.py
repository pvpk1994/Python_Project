'''
Calculate String Distance Problem
Author: Pavan Kumar Paluri
Bottom Up Solution using DP
'''


class str_dist_top_down:
    def __init__(self, str_a, str_b):
        self.str_a = str_a
        self.str_b = str_b
        # Create a -1 filled 2D array to store all the computed values
        self.dist_arr = [[]]*(len(str_a)+1)
        # now iterate through the outer len to fill up inner columns
        for a in range(0, len(str_a) + 1):
            self.dist_arr[a] = [-1]*(len(str_b) + 1)
            # Access each cell
            for b in range(0, len(str_b) + 1):
                if a == 0:
                    self.dist_arr[a][b] = b
                elif b == 0:
                    self.dist_arr[a][b] = a
                else:
                    # Replace metric
                    if self.str_a[a - 1] == self.str_b[b - 1]:
                        replace_cost = 0
                    else:
                        replace_cost = 1
                    insert_cost = 1 + self.dist_arr[a][b-1]
                    delete_cost = 1 + self.dist_arr[a-1][b]
                    replace_cost = replace_cost + self.dist_arr[a - 1][b - 1]
                    self.dist_arr[a][b] = min(replace_cost, delete_cost, insert_cost)

    def calculate_final_dist(self):
        # The final cell has the result, so just return that
        return self.dist_arr[len(self.str_a)][len(self.str_b)]


if __name__ == '__main__':
    test_str = str_dist_top_down("TodayIsSaturday", "TomorrowIsSunday")
    print(test_str.calculate_final_dist())







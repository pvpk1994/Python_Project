'''
Calculate String Distance Problem
Author: Pavan Kumar Paluri
Top Down Solution using DP
'''


class str_dist_top_down:
    def __init__(self, str_a, str_b):
        self.str_a = str_a
        self.str_b = str_b
        # Create a -1 filled 2D array to store all the computed values
        self.dist_arr = [[]]*(len(str_a)+1)
        # now iterate through the outer len to fill up inner columns
        for iterator in range(0, len(str_a) + 1):
            self.dist_arr[iterator] = [-1]*(len(str_b) + 1)

    def dist(self, len_str_a, len_str_b):
        if self.dist_arr[len_str_a][len_str_b] != -1:
            return self.dist_arr[len_str_a][len_str_b]

        else:
            if len_str_a == 0:
                return len_str_b

            if len_str_b == 0:
                return len_str_a

            # Traversing from end
            if self.str_b[len_str_b - 1] == self.str_a[len_str_a - 1]:
                replace_cost = 0
            else:
                replace_cost = 1

            # Delete Cost
            delete_cost = 1 + self.dist(len_str_a - 1, len_str_b)

            # Insert Cost
            insert_cost = 1 + self.dist(len_str_a, len_str_b - 1)

            # Replace cost
            replace_cost = self.dist(len_str_a - 1, len_str_b - 1) + replace_cost

            # Memotize this value before returning the min
            self.dist_arr[len_str_a][len_str_b] = min(delete_cost, insert_cost, replace_cost)

            return min(delete_cost, insert_cost, replace_cost)

    def calculate_final_dist(self):
        return self.dist(len(self.str_a), len(self.str_b))


if __name__ == '__main__':
    test_str = str_dist_top_down("TodayIsSaturday", "TomorrowIsSunday")
    print(test_str.calculate_final_dist())







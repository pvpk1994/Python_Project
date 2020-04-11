'''
String Distance Score Calculation
Author: Pavan Kumar Paluri
Brute Force Approach
'''


class string_dist:
    def __init__(self, str_a, str_b):
        self.str_a = str_a
        self.str_b = str_b

    def dist(self, len_a, len_b):
        if len_b == 0:
            return len_a
        if len_a == 0:
            return len_b
        # Cal replace cost (0 if char to replace is same) 1 otherwise (Proceeding from end)
        if self.str_a[len_a - 1] == self.str_b[len_b - 1]:
            replace_cost = 0
        else:
            replace_cost = 1

        # Other costs ( Delete and Insert)
        # Delete: Delete a character from source string
        delete_cost = 1 + self.dist(len_a-1, len_b)

        # Insert: Delete a character from Dest string
        insert_cost = 1 + self.dist(len_a, len_b - 1)

        # Replace: Replace a char from source and dest string
        replace_cost = self.dist(len_a - 1, len_b - 1) + replace_cost

        # Compute Min of all costs
        return min(delete_cost, replace_cost, insert_cost)

    def compute_final(self):
        return self.dist(len(self.str_a), len(self.str_b))


if __name__ == '__main__':
    test_str = string_dist("Saturday", "Sundays")
    print(test_str.compute_final())
'''
Calculating String Distance b/n Source and Dest String
Author: Pavan Kumar Paluri
Using Bottom Up Mem Optimized Approach
'''


class string_dist_mem_optimized:
    def __init__(self, str_source, str_dest):
        self.str_source = str_source
        self.str_dest = str_dest
        self.dist_read = [-1]*(len(str_source) + 1)
        self.dist_write = [-1]*(len(str_source) + 1)

        # Outer loop to run for the length of dest string
        # inner loop to run for the length of source string
        for outer in range(0, len(str_dest) + 1):
            for inner in range(0, len(str_source) + 1):
                # Only do write operations on dist_write array
                if outer == 0:
                    self.dist_write[inner] = inner
                elif inner == 0:
                    self.dist_write[inner] = outer
                else:
                    if self.str_dest[outer - 1] == self.str_source[inner  - 1]:
                        replace_cost = 0
                    else:
                        replace_cost = 1

                    delete_cost = 1 + self.dist_write[inner - 1]
                    insert_cost = 1 + self.dist_read[inner]
                    replace_cost = replace_cost + self.dist_read[inner - 1]
                    self.dist_write[inner] = min(delete_cost, insert_cost, replace_cost)
            # Out of inner for loop, we now perform swapping of read and write arrays
            (self.dist_write, self.dist_read) = (self.dist_read, self.dist_write)
            print(self.dist_read)

    def print_result(self):
        return self.dist_read[len(self.str_source)]


if __name__ == '__main__':
    test_str = string_dist_mem_optimized("TodayIsSaturday", "TomorrowIsSunday")
    print(test_str.print_result())




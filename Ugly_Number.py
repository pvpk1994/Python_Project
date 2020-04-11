'''
Ugly Number DP
Author: Pavan Kumar Paluri
Source: Geeks for Geeks
'''


class ugly_number_cal:
    def __init__(self, num):
        self.num = num
        self.num_mul_2 = 2
        self.num_mul_3 = 3
        self.num_mul_5 = 5
        self.i2, self.i3, self.i5 = 0, 0, 0
        # Array that accommodates all latest ugly numbers
        self.ugly_arr = [0] * self.num
        # FIll the first elem with 1
        self.ugly_arr[0] = 1
        for number in range(1, num):
            # Cal the min ugly number to put in ...
            self.ugly_arr[number] = min(self.num_mul_2, self.num_mul_3, self.num_mul_5)
            if self.ugly_arr[number] == self.num_mul_2:
                self.i2 += 1
                self.num_mul_2 = self.ugly_arr[self.i2] * 2

            if self.ugly_arr[number] == self.num_mul_3:
                self.i3 += 1
                self.num_mul_3 = self.ugly_arr[self.i3] * 3

            if self.ugly_arr[number] == self.num_mul_5:
                self.i5 += 1
                self.num_mul_5 = self.ugly_arr[self.i5] * 5

    def print_ugly_result(self):
        return self.ugly_arr[self.num - 1]


if __name__ == '__main__':
    n = 150
    ugly = ugly_number_cal(n)
    print(ugly.print_ugly_result())


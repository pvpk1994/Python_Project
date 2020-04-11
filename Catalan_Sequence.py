'''
Catalan Sequence
Author: Pavan Kumar Paluri
Source: Geeks for Geeks
'''


class catalan_seq:
    def __init__(self, n_plus_one):
        self.n_plus_one = n_plus_one
        self.counter = 0

    def cat_seq_cal(self, num):
        # Stopping condition
        result = 0
        if num == 0 or num == 1:
            return 1

        else:
            for i in range(0, num):
                result += self.cat_seq_cal(i)*self.cat_seq_cal(num-i-1)
            return result


# Dynamic Programming approach using Top-Down Memoization
class catalan_seq_top_down:
    def __init__(self, catalan_num):
        self.catalan_num = catalan_num
        self.mem_arr = [-1]*(catalan_num+1)
        self.mem_arr[0] = 1
        self.mem_arr[1] = 1

    # recursive function
    def cat_rec(self):
        for i in range(2, self.catalan_num+1):
            self.mem_arr[i] = 0
            for j in range(0, i):
                self.mem_arr[i] += self.mem_arr[j]*self.mem_arr[i-j-1]
        return self.mem_arr[self.catalan_num]


if __name__ == '__main__':
    # ---- without DP -------
    cat_seq = catalan_seq(5)
    print(cat_seq.cat_seq_cal(5))
    # ---- with DP --------
    cat_seq_dp = catalan_seq_top_down(5)
    print(cat_seq_dp.cat_rec())

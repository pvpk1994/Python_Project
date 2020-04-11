'''
Bell Number Sequences
Author: Pavan Kumar Paluri
'''


class bell_seq:
    def __init__(self, bell_num):
        self.bell_num = bell_num
        # create a 2D array and init with -1s
        self.mem_arr = [[]]*(bell_num+1)
        for i in range(0, bell_num+1):
            self.mem_arr[i] = [-1]*(bell_num+1)

    # ---------- without DP, using brute force recursive -------
    def s_func(self, n, k):
        if k > n:
            return 0
        if k == 1 or k == n:
            return 1
        return k * self.s_func(n - 1, k) + self.s_func(n - 1, k - 1)

    # ---------- with DP, using Top-Down Memoization ---------
    def s_func_top_down(self, n, k):
        if self.mem_arr[n][k] != -1:
            return self.mem_arr[n][k]
        if k > n:
            return 0
        if k == 1 or k == n:
            return 1
        self.mem_arr[n][k] = k*self.s_func_top_down(n-1, k) + self.s_func(n-1, k-1)
        result = self.mem_arr[n][k]
        return result

    def compute_bell_res(self):
        bell_result = 0
        for i in range(1, self.bell_num+1):
            bell_result += self.s_func_top_down(self.bell_num, i)
        return bell_result


if __name__ == '__main__':
    bell_given = bell_seq(5)
    print(bell_given.compute_bell_res())

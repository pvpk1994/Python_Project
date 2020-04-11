'''
Author: Pavan Kumar Paluri
Binomial Coefficient Calculation
Iterative Approach - Bottom Up
'''


class BC:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self. arr = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    def bc_bottom_up(self):
        for i in range(0, self.n+1):
            for j in range(0, self.k+1):
                # Stopping conditions
                if j == 0 or j == i:
                    self.arr[i][j] = 1
                else:
                    self.arr[i][j] = self.arr[i-1][j-1] + self.arr[i-1][j]
        return self.arr[self.n][self.k]


if __name__ == '__main__':
    bcc = BC(1000, 23)
    print("BC for (" + str(1000) + "," + str(23) + ") is:" + str(bcc.bc_bottom_up()))
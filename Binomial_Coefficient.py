'''
Calculate Binomial Coefficient
Author: Pavan Kumar Paluri
Using Recursion - Top Down Approach
NOTE: Recursion using Top Down approach does not work beyond 1000 iterations as recursion has a
Max limit of 1000 recursions ONLY, need to deploy a Bottom-Up Approach
'''

import sys


class Binomial_Top_Down:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        # Create a 2D array to store (n,k)
        self.arr = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    def binomial_coefficient(self, n, k):
        if self.arr[n][k] != -1:
            return self.arr[n][k]
        if n == k or k == 0:
            self.arr[n][k] = 1
            return 1
        self.arr[n][k] = self.binomial_coefficient(n-1, k-1) + self.binomial_coefficient(n-1, k)

        return self.arr[n][k]


if __name__ == '__main__':
    number = int(input("Enter n:"))
    k_val = int(input("Enter k: "))
    bc_class = Binomial_Top_Down(number, k_val)
    print(f"BC for C{(number, k_val)} is {bc_class.binomial_coefficient(number, k_val)}")
    print("Recursion limit is " + str(sys.getrecursionlimit()))

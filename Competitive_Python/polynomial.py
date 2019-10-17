import numpy as np
'''
Polynomial Operations 
Author: Pavan Kumar Paluri
'''

'''
Given list of coefficients of a Polynomial equation, return the value of the equation
when value of x is fed as an input
'''


def polynomial_calc(list_pol: list, x_val: float):
    return np.polyval(list(list_pol), x_val)


if __name__ == '__main__':
    list_poly = (list(map(float, input().split())))
    x_sub = float(input())
    # print(list_poly)
    print(polynomial_calc(list_poly, x_sub))
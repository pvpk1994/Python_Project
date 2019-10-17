import numpy
'''
Given an N*N matrix, compute its determinant
Author : Pavan Kumar Paluri
Question / Source: Hacker Rank
'''


def determinant_matrix(list_mat: list) -> int:
    det = numpy.linalg.det(list_mat)
    return det


if __name__ == '__main__':
    list_matrix = []
    n = int(input())
    for _ in range(0, n):
        list_matrix.append(list(map(float, input().rstrip().split())))
    # determinant_matrix(list_matrix)
    print(round(determinant_matrix(list_matrix), 2))
    # numpy.linalg.det()


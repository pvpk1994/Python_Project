'''
Given the moves of players A and B
Decide the final state of the matrix
Author: Pavan Kumar Paluri
Source: LeetCode
'''


def tic_tac_toe_final(chances: list) -> str:
    '''
    empty 3*3 matrix with -1's as init vals
    '''
    var = 0
    matrix = [[-1 for _ in range(0, 3)] for _ in range(0, 3)]
    print(matrix)
    dict_store = {
        1: 'A',
        2: 'B',
        3: 'Pending'
    }
    for index, coord in enumerate(chances):
        if index % 2 == 0:
            matrix[coord[0]][coord[1]] = 1
        elif index % 2 != 0:
            matrix[coord[0]][coord[1]] = 2

    # Player A has 1 on board and B has 2 on Board
    # Win condition
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            # row / col / diagonal check
            if matrix[i][0] == matrix[i][1] == matrix[i][2] or matrix[0][j] == matrix[1][j] == matrix[2][j] or \
                    matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[2][0] == matrix[1][1] == matrix[0][2]:
                if matrix[i][j] != -1:
                    var = matrix[i][j]
            else:
                var = 3
    print(matrix)
    return f'{dict_store[var]}'


if __name__ == '__main__':
    moves = []
    num_moves_A_B = int(input())
    level = 0
    for _ in range(num_moves_A_B*2):
        moves.append([])
        move_coord_x = int(input())
        move_coord_y = int(input())
        moves[level].append(move_coord_x)
        moves[level].append(move_coord_y)
        level += 1

    print(moves)
    print(f'Final State: {tic_tac_toe_final(moves)}')
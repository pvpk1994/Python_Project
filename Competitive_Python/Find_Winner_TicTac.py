'''
Given the moves of players A and B
Decide the final state of the matrix
Author: Pavan Kumar Paluri
Source: LeetCode
'''


def tic_tac_toe_final(chances: list):
    '''
    empty 3*3 matrix with -1's as init vals
    '''
    var = 0
    matrix = [[-1 for _ in range(0, 3)] for _ in range(0, 3)]

    dict_store = {
        1: 'A',
        2: 'B',
        3: 'Pending',
        0: 'Game Yet to Begin',
        4: 'Draw'
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
            # row / col checks
            if matrix[i][0] == matrix[i][1] == matrix[i][2] or matrix[0][j] == matrix[1][j] == matrix[2][j]:
                if matrix[i][j] != -1:
                    var = matrix[i][j]
                # Diagonal checks
            elif matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[2][0] == matrix[1][1] == matrix[0][2]:
                if matrix[1][1] != -1:
                    var = matrix[1][1]
            else:
                var = 3
    # print(matrix)
    print(matrix)
    # Draw Condition Check here..
    for k in matrix:
        if -1 not in k and var == 3:
            var = 4
    return f'{dict_store[var]}'


if __name__ == '__main__':
    moves = []
    num_moves_A = int(input('Enter Number of moves for Player A: '))
    num_moves_B = int(input('Enter Number of Moves for Player B: '))
    level = 0
    for _ in range(0, num_moves_A + num_moves_B):
        moves.append([])
        move_coord_x = int(input())
        move_coord_y = int(input())
        moves[level].append(move_coord_x)
        moves[level].append(move_coord_y)
        level += 1

    # print(moves)
    print(f'Final State: {tic_tac_toe_final(moves)}')

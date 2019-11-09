import random
'''
Design a Tic-Tac-Toe 3x3 using only lists
NOTE: DO NOT USE NUMPY LIBRARY 
Author: Pavan Kumar Paluri
Source: LeetCode
'''


def random_list_supplier(list_board: list) -> list:
    list_supply = []
    for i in range(len(list_board)):
        for j in range(len(list_board)):
            if list_board[i][j] is None:
                # pick and port the i,j indices of such None params
                list_supply.append([i, j])
    return list_supply


def random_placement(list_board: list, player: str) -> list:
    # Selection of a random place first...
    res = random_list_supplier(list_board)

    index_picker = random.choice(res)
    # print(index_picker)
    i, j = index_picker[0], index_picker[1]
    list_board[i][j] = player
    # print(list_board)
    return list_board


def row_comp(list_game: list, player: str) -> int:
    for i in range(len(list_game)):
        if list_game[i][0] == list_game[i][1] == list_game[i][2] is player:
            return 0
    return -1


def col_comp(list_game: list, player: str) -> int:
    for j in range(len(list_game)):
        if list_game[0][j] == list_game[1][j] == list_game[2][j] is player:
            return 0
    return -1


def diag_comp(list_game: list, player: str) -> int:
    if list_game[0][0] == list_game[1][1] == list_game[2][2] is player:
        return 0
    return -1


def evaluate(list_game: list) -> str:
    # invoke row, col and diagonal functions...
    winner = []
    winner_str = 'None'
    for player in ['x', 'o']:
        if row_comp(list_game, player) == 0 or \
                col_comp(list_game, player) == 0 or \
                diag_comp(list_game, player) == 0:
            winner.append(player)
            winner_str = player
    # Draw condition check...
    win_comp = []
    for i in range(len(list_game)):
        for j in range(len(list_game)):
            win_comp.append(list_game[i][j])
    # Absolute draw is ensured if condition below is satisfied, then change winner_str to 'Draw'
    if all(val is not None for val in win_comp) and winner_str is 'None':
        winner_str = 'Draw'
    return winner_str


def tic_tac_toe(list_tic_tac: list) -> str:
    # Define Winner param
    winner = 'None'
    counter = 0
    while winner is 'None':
        # Randomize the control to place
        for player in ['x', 'o']:
            list_tic_tac = random_placement(list_tic_tac, player)
            counter += 1
            print(f'Player {player} has made {counter}th move')
            print(f'\n{list_tic_tac[0]}\n{list_tic_tac[1]}\n{list_tic_tac[2]}')
            # winner += 1  # Dummy
            winner = evaluate(list_tic_tac)
            if winner is not 'None':
                break
    return winner


if __name__ == '__main__':
    '''
    Load an empty two dimensional list of 3x3 matrix
    using list comprehension
    '''
    list_matrix = [[None for _ in range(0, 3)] for _ in range(0, 3)]
    # list_matrix = []
    print(f'Initial Board State: \n{list_matrix[0]}\n{list_matrix[1]}\n{list_matrix[2]}')
    print(f'{tic_tac_toe(list_matrix)} won the match')

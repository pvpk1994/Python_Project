'''
Candy Crush
Author: Pavan Kumar Paluri
Source: LeetCode
'''

'''
Given a 2d matrix, perform candy crush operations on it and 
return the final state of the board when there are no candies to crush 
anymore
'''


def candy_crush(board: list) -> list:
    # get the number of rows and cols
    rows = len(board)
    cols = len(board[0])
    # Set a boolean variable to check if there are any candies to crush
    to_crush = False

    # Condition checks begin here
    # Traversing row wise first by having column fixed..
    for row in range(rows-2):
        for col in range(cols):
            if abs(board[row][col]) == abs(board[row+1][col]) == abs(board[row+2][col]) != 0:
                # If so, set all to a const param, say -ve board[row][col]
                board[row][col] = board[row+1][col] = board[row+2][col] = -abs(board[row][col])
                to_crush = True
    # Traversing column wise now by having row fixed
    for row in range(rows):
        for col in range(cols - 2):
            if abs(board[row][col]) == abs(board[row][col+1]) == abs(board[row][col+2]) != 0:
                board[row][col] = board[row][col+1] = board[row][col+2] = -abs(board[row][col])
                to_crush = True

    # Now, try to bring down elements from upper rows into these vacant cells
    # Then fill upper rows that are vacant with 0's
    for col in range(cols):
        # have a marker at the end of a row
        row_marker = rows - 1
        # Traverse in a reverse direction row-wise..
        for row in range(rows-1, -1, -1):
            if board[row][col] > 0:
                board[row_marker][col] = board[row][col]
                row_marker -= 1
        for row_new in range(row_marker, -1 , -1):
            # in this phase, set all entries from row_marker's present val until the head
            board[row_new][col] = 0
    return candy_crush(board) if to_crush is True else board


if __name__ == '__main__':
    board_new = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
                 [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2],
                 [4, 1, 4, 4, 1014]]
    print(f'{candy_crush(board_new)}')




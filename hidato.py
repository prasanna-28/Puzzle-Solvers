#board can be adusted to any nxn size
hidato_board = [
    [ 6,  0,  0, 15, 16],
    [ 0,  0,  0,  0, 17],
    [ 0,  0,  1,  0, 18],
    [ 0,  0,  0,  0, 19],
    [26,  0,  0, 22, 20],
]

def is_valid_hidato(board, row, col, num):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if 0 <= row+x < len(board) and 0 <= col+y < len(board[0]):
                if board[row+x][col+y] == num:
                    return False
    return True

def solve_hidato(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                if is_valid_hidato(board, i, j, num+1):
                    board[i][j] = num+1
                    if num+1 == len(board)**2 or solve_hidato(board, num+1):
                        return True
                    board[i][j] = 0
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = ' ')
        print()

def solve_hidato_puzzle(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if solve_hidato(board, 1):
                    print_board(board)
                    return
    print("No solution exists.")


solve_hidato_puzzle(hidato_board)
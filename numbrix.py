#board can be adusted to any nxn size
numbrix_board = [
    [ 5,  0,  0,  0, 15],
    [ 0,  0,  0,  0, 16],
    [ 0,  0,  1,  0,  0],
    [ 0,  0,  0,  0,  0],
    [25,  0,  0,  0, 20],
]


def is_valid(board, row, col, num):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if abs(x-y) == 1 and 0 <= row+x < len(board) and 0 <= col+y < len(board[0]):
                if board[row+x][col+y] == num:
                    return False
    return True

def solve(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                for n in [num-1, num+1]:
                    if is_valid(board, i, j, n):
                        board[i][j] = n
                        if n == len(board)**2 or solve(board, n):
                            return True
                        board[i][j] = 0
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = ' ')
        print()

def solve_numbrix(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if solve(board, 1):
                    print_board(board)
                    return
    print("No solution exists.")

solve_numbrix(numbrix_board)
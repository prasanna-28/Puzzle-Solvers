#size of board may be adjusted
latin_square = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
]



def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, len(board) + 1):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")

        print()

def solve_latin_square(board):
    if solve(board):
        print_board(board)
    else:
        print("No solution exists.")


solve_latin_square(latin_square)
import itertools

def possibilities(clue, length):
    #Return a list of all possible fillings of a row or column of length 'length', given the clue.
    clue = [0] + clue + [0]
    spaces = [clue[i-1] + clue[i] + 1 for i in range(1, len(clue))]
    total_spaces = sum(spaces)
    extra_spaces = length - total_spaces + len(spaces) - 1
    space_possibilities = []
    for i in range(len(spaces)):
        space_possibilities.append(list(itertools.combinations(range(extra_spaces + i), i)))
    all_possibilities = list(itertools.product(*space_possibilities))
    row_possibilities = []
    for possibility in all_possibilities:
        spaces = list(possibility)
        spaces.append(extra_spaces + len(spaces))
        spaces.insert(0, 0)
        row = [0] * length
        for i in range(1, len(clue)-1):
            for j in range(sum(spaces[:i+1]), sum(spaces[:i+1]) + clue[i]):
                row[j] = 1
        row_possibilities.append(row)
    return row_possibilities

def solve(nonogram):
    rows, cols = nonogram
    row_possibilities = [possibilities(row, len(cols)) for row in rows]
    col_possibilities = [possibilities(col, len(rows)) for col in cols]
    solution = [None] * len(rows)
    while None in solution:
        for i in range(len(rows)):
            if solution[i] is not None:
                continue
            possible_rows = row_possibilities[i]
            for j in range(len(cols)):
                possible_cols = col_possibilities[j]
                possible_cells = [row[j] for row in possible_rows]
                if 0 not in possible_cells:
                    for col in possible_cols:
                        col[i] = 1
                if 1 not in possible_cells:
                    for col in possible_cols:
                        col[i] = 0
            possible_rows = [row for row in possible_rows if all(cell == 1 or row[j] == 0 for j, cell in enumerate(solution[i]))]
            if len(possible_rows) == 1:
                solution[i] = possible_rows[0]
    return solution

def print_solution(solution):
    for row in solution:
        print(''.join('#' if cell else '.' for cell in row))

#board size may be adjusted
nonogram = (
    [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]],
    [[0, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 0]]
)

solution = solve(nonogram)
print_solution(solution)

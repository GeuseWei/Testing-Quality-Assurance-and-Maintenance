'''Magic Square

https://en.wikipedia.org/wiki/Magic_square

A magic square is a n * n square grid filled with distinct positive integers in
the range 1, 2, ..., n^2 such that each cell contains a different integer and
the sum of the integers in each row, column, and diagonal is equal.

'''

from z3 import Solver, sat, unsat, Int, Distinct


def solve_magic_square(n, r, c, val):
    solver = Solver()

    # CREATE CONSTRAINTS AND LOAD STORE THEM IN THE SOLVER
    # Create an n x n array of integer variables
    X = []
    for i in range(n):
        row = []
        for j in range(n):
            name = f'x_{i}_{j}'
            var = Int(name)
            row.append(var)
        X.append(row)

    # Each cell contains a different integer from 1 to n^2
    distinct_cells = []
    for i in range(n):
        for j in range(n):
            distinct_cells.append(X[i][j])
    solver.add(Distinct(distinct_cells))

    for i in range(n):
        for j in range(n):
            solver.add(X[i][j] >= 1)

    for i in range(n):
        for j in range(n):
            solver.add(X[i][j] <= n * n)

    # Set the given cell to the given value
    solver.add(X[r][c] == val)

    # Sum of each row, column and diagonal is the same
    magic_sum = 0
    for i in range(n):
        magic_sum += X[i][i]

    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += X[i][j]
        solver.add(row_sum == magic_sum)

        col_sum = 0
        for j in range(n):
            col_sum += X[j][i]
        solver.add(col_sum == magic_sum)

    second_diagonal_sum = 0
    for i in range(n):
        second_diagonal_sum += X[i][n - 1 - i]
    solver.add(second_diagonal_sum == magic_sum)

    if solver.check() == sat:
        mod = solver.model()
        res = []

        # CREATE RESULT MAGIC SQUARE BASED ON THE MODEL FROM THE SOLVER
        for i in range(n):
            row_res = []
            for j in range(n):
                value = mod.eval(X[i][j]).as_long()
                row_res.append(value)
            res.append(row_res)

        return res
    else:
        return None


def print_square(square):
    '''
    Prints a magic square as a square on the console
    '''
    n = len(square)

    assert n > 0
    for i in range(n):
        assert len(square[i]) == n

    for i in range(n):
        line = []
        for j in range(n):
            line.append(str(square[i][j]))
        print('\t'.join(line))


def puzzle(n, r, c, val):
    res = solve_magic_square(n, r, c, val)
    if res is None:
        print('No solution!')
    else:
        print('Solution:')
        print_square(res)


if __name__ == '__main__':
    n = 3
    r = 1
    c = 1
    val = 5
    puzzle(n, r, c, val)

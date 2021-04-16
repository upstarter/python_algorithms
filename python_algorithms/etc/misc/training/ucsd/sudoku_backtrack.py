import numpy as np

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def possible(y, x, n):
    global grid
    # check rows
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    # check cols
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    # cleverly check subgrids
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


# no params, working on global grid
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    # reduce by subproblem of finding cell solution
                    grid[y][x] = n
                    # try to expand search space as long as finding solutions
                    solve()
                    # tried all possibilities, failed to solve grid, backtrack
                    grid[y][x] = 0
                return
    print(np.matrix(grid))
    input("More?")


solve()

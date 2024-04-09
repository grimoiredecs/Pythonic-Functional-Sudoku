import numpy as np

def check(grid, y, x, n):
    in_row = any(grid[y][i] == n for i in range(9))
    in_column = any(grid[i][x] == n for i in range(9))
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    in_box = any(grid[y0 + i][x0 + j] == n for i in range(3) for j in range(3))
    return not (in_row or in_column or in_box)

def solve_sudoku(grid):
    solve = lambda: next((False, grid)
                         for y in range(9)
                         for x in range(9)
                         if grid[y][x] == 0
                         for n in range(1, 10)
                         if check(grid, y, x, n) and (grid.__setitem__((y, x), n) or solve()[0] or grid.__setitem__((y, x), 0)))
    return solve()[1]

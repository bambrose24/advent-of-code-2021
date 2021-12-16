
from math import inf, isinf

import sys

def main():
    sys.setrecursionlimit(500 * 500)
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_input():
    with open('input.txt', 'r') as f:
        res = []
        for l in f.readlines():
            res.append([int(c) for c in l.strip()])
        return res

def part_one():
    grid = get_input()
    data = [[inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
    data[0][0] = 0

    for i in range(1, len(grid)):
        data[i][0] = grid[i][0] + data[i-1][0]
    for i in range(1, len(grid[0])):
        data[0][i] = grid[0][i] + data[0][i-1]
    
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            data[i][j] = grid[i][j] + min(data[i-1][j], data[i][j-1])
    return data[-1][-1]

def part_two():
    grid = get_input()

    new_grid = []
    for row_repeat in range(5):
        for i in range(len(grid)):
            row = grid[i]
            new_row = []
            for inc in range(5):
                sub_row = []
                for i in range(len(row)):
                    x = ((row[i] + row_repeat + inc - 1) % 9) + 1
                    sub_row.append(x)
                new_row += sub_row
            new_grid.append(new_row)

    grid = new_grid

    # visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    cache = [[inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return dfs(grid, cache, len(grid)-1, len(grid[0])-1)


    # data = [[inf for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # data[0][0] = 0
    # for i in range(1, len(grid)):
    #     data[i][0] = grid[i][0] + data[i-1][0]
    # for i in range(1, len(grid[0])):
    #     data[0][i] = grid[0][i] + data[0][i-1]
    
    # for i in range(1, len(grid)):
    #     for j in range(1, len(grid[0])):
    #         data[i][j] = grid[i][j] + min(data[i-1][j], data[i][j-1])
    
    return data[-1][-1]

def dfs(grid, cache, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return inf
    if (x,y) == (0,0):
        cache[0][0] = 0
    if cache[x][y] != inf:
        return cache[x][y]
    res = grid[x][y] + min(dfs(grid, cache, x-1, y), dfs(grid, cache, x, y-1))
    cache[x][y] = res
    return res


    
def get_neighbors(grid, x, y):
    candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    res = []
    for xc,yc in candidates:
        if xc < 0 or xc >= len(grid) or yc < 0 or yc >= len(grid[0]):
            continue
        res.append((xc,yc))
    return res
        


if __name__ == '__main__':
    main()
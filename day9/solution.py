
def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_grid():
    with open('input.txt', 'r') as f:
        return [[int(y) for y in x.strip()] for x in f.readlines()]


def part_one():
    grid = get_grid()
    low_vals = get_low_vals(grid)
    print('part one num low vals', len(low_vals))
    return sum([grid[x][y] + 1 for (x,y) in low_vals])

def get_low_vals(grid):
    low_vals = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            v = grid[r][c]
            neighbor_vals = [grid[x][y] for (x,y) in get_neighbors(grid, r, c)]
            if min(neighbor_vals) > v:
                low_vals.append((r,c))
    return low_vals
    

def get_neighbors(grid, r, c):
    rmax = len(grid) - 1
    cmax = len(grid[0]) - 1
    l = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    return [x for x in l if x[0] >= 0 and x[1] >= 0 and x[0] <= rmax and x[1] <= cmax]

def get_neighbors_vals(grid, r, c):
    rmax = len(grid) - 1
    cmax = len(grid[0]) - 1
    l = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    return [(x[0], x[1], grid[x[0]][x[1]]) for x in l if x[0] >= 0 and x[1] >= 0 and x[0] <= rmax and x[1] <= cmax]

def part_two():
    grid = get_grid()
    low_vals = get_low_vals(grid)
    counts = []
    for (r,c) in low_vals:
        count = get_basin_count(grid, (r,c), 0)
        counts.append(count)
    top_three = list(sorted(counts))[-3:]
    return top_three[0] * top_three[1] * top_three[2]

def get_basin_count(grid, xy, curr_count):
    x,y = xy
    if grid[x][y] == -1 or grid[x][y] == 9:
        return curr_count
    grid[x][y] = -1
    return 1 + sum([get_basin_count(grid, (x,y), curr_count) for (x,y,v) in get_neighbors_vals(grid, x, y)])


if __name__ == '__main__':
    main()

def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_grid():
    with open('input.txt', 'r') as f:
        res = []
        for line in f.readlines():
            res.append([int(x) for x in line.strip()])
        return res

def part_one():
    grid = get_grid()
    flash_count = 0
    for step_num in range(100):
        # make 100 steps, count flashes
        
        flashed_set = set()
        greater_than_nine = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    greater_than_nine.append((x,y))
        
        while len(greater_than_nine) > 0:
            (x,y) = greater_than_nine.pop()
            if (x,y) in flashed_set:
                continue
            flashed_set.add((x,y))
            for (x,y) in get_flash_neighbors(grid, x,y):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    greater_than_nine.append((x,y))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 9:
                    flash_count += 1
                    grid[x][y] = 0
    return flash_count

def get_flash_neighbors(grid, x, y):
    candidates = [
        (x-1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x, y-1),
        (x, y+1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1),
    ]
    return [(r,c) for (r,c) in candidates if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])]


def part_two():
    grid = get_grid()
    all_flashed = False
    step_num = 0
    while not all_flashed:
        # make 100 steps, count flashes
        step_num += 1
        flashed_set = set()
        greater_than_nine = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    greater_than_nine.append((x,y))
        
        while len(greater_than_nine) > 0:
            (x,y) = greater_than_nine.pop()
            if (x,y) in flashed_set:
                continue
            flashed_set.add((x,y))
            for (x,y) in get_flash_neighbors(grid, x,y):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    greater_than_nine.append((x,y))

        flash_count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 9:
                    flash_count += 1
                    grid[x][y] = 0
        if flash_count == (len(grid) * len(grid[0])):
            all_flashed = True
    return step_num

if __name__ == '__main__':
    main()
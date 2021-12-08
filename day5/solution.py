
from typing import List, Tuple


def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_lines() -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    with open('input.txt', 'r') as f:
        res = []
        for l in f:
            a,b = l.strip().split('->')
            x1,y1 = a.strip().split(',')
            x2,y2 = b.strip().split(',')
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
            res.append(((x1,y1), (x2,y2)))
        return res
            


def part_one():
    ranges = get_lines()
    max_x = max([r[0][0] for r in ranges] + [r[1][0] for r in ranges])
    max_y = max([r[0][1] for r in ranges] + [r[1][1] for r in ranges])

    table = [[0 for y in range(max_y + 1)] for x in range(max_x + 1)]

    for (x1,y1), (x2,y2) in ranges:
        if x1 != x2 and y1 != y2:
            continue

        if x1 == x2:
            y1,y2 = min(y1,y2), max(y1,y2)
            x = x1
            for y in range(y1, y2 + 1):
                table[x][y] += 1

        else: # y1 == y2
            y = y1
            x1,x2 = min(x1,x2), max(x1,x2)
            for x in range(x1, x2 + 1):
                table[x][y] += 1
        
    total = 0
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] > 1:
                total += 1
    return total

def part_two():
    ranges = get_lines()
    max_x = max([r[0][0] for r in ranges] + [r[1][0] for r in ranges])
    max_y = max([r[0][1] for r in ranges] + [r[1][1] for r in ranges])

    table = [[0 for y in range(max_y + 1)] for x in range(max_x + 1)]

    for (x1,y1), (x2,y2) in ranges:
        if x1 == x2:
            y1,y2 = min(y1,y2), max(y1,y2)
            x = x1
            for y in range(y1, y2 + 1):
                table[x][y] += 1
        elif y1 == y2: # y1 == y2
            x1,x2 = min(x1,x2), max(x1,x2)
            y = y1
            for x in range(x1, x2 + 1):
                table[x][y] += 1
        else:
            x_inc = 1 if x1 < x2 else -1
            y_inc = 1 if y1 < y2 else -1
            x,y = x1,y1
            for i in range(abs(x1 - x2) + 1):
                table[x][y] += 1
                x += x_inc
                y += y_inc
        
    total = 0
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] > 1:
                total += 1
    return total

if __name__ == '__main__':
    main()
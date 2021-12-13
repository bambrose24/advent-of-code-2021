
def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_input(): # List[Tuple[int, int], Tuple["x" | "y", int]]
    with open('input.txt', 'r') as f:
        points = []
        flips = []
        for line in f.readlines():
            line = line.strip()
            if ',' in line:
                x,y = line.split(',')
                x,y = int(x), int(y)
                points.append((x,y))
            elif len(line) > 0:
                if 'x=' in line:
                    flips.append(('x', int(line.split('x=')[1])))
                elif 'y=' in line:
                    flips.append(('y', int(line.split('y=')[1])))
    return points,flips


def part_one():
    points,flips = get_input()
    points = set(points)
    flips = [flips[0]]
    for flip in flips:
        direction, value = flip
        flipped_points = set()
        if direction == 'y':
            points_to_flip = [p for p in points if p[1] > value]
            for x,y in points_to_flip:
                new_p = (x, value - abs(y-value))
                flipped_points.add(new_p)
        else:
            points_to_flip = [p for p in points if p[0] > value]
            for x,y in points_to_flip:
                new_p = (value - abs(x-value), y)
                flipped_points.add(new_p)
        new_points = set()
        for x,y in points:
            if direction == 'x' and x < value:
                new_points.add((x,y))
            elif direction == 'y' and y < value:
                new_points.add((x,y))
        points = new_points.union(flipped_points)
    return len(points)


def part_two():
    points,flips = get_input()
    points = set(points)
    for flip in flips:
        direction, value = flip
        flipped_points = set()
        if direction == 'y':
            points_to_flip = [p for p in points if p[1] > value]
            for x,y in points_to_flip:
                new_p = (x, value - abs(y-value))
                flipped_points.add(new_p)
        else:
            points_to_flip = [p for p in points if p[0] > value]
            for x,y in points_to_flip:
                new_p = (value - abs(x-value), y)
                flipped_points.add(new_p)
        new_points = set()
        for x,y in points:
            if direction == 'x' and x < value:
                new_points.add((x,y))
            elif direction == 'y' and y < value:
                new_points.add((x,y))
        points = new_points.union(flipped_points)
    
    # now print the thing
    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])

    res = ''
    for y in range(max_y + 1):
        line = ''
        for x in range(max_x + 1):
            if (x,y) in points:
                line += '#'
            else:
                line += '.'
        res += line + "\n"
    return "\n" + res + "\n"

if __name__ == '__main__':
    main()
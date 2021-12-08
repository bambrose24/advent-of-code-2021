
from collections import defaultdict

def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_input():
    with open('input.txt', 'r') as f:
        return [int(x) for x in f.readline().strip().split(',')]

def part_one():
    l = get_input()
    d = defaultdict(int)
    for v in l:
        d[v] += 1
    
    num_days = 80
    for day in range(num_days):
        new_d = {}
        for i in range(9):
            if i not in d:
                continue
            if i == 0:
                new_d[6] = d[i]
                new_d[8] = d[i]
            else:
                if (i-1) not in new_d:
                    new_d[i-1] = 0
                new_d[i-1] += d[i]
        d = new_d
    return sum(d.values())



def part_two():
    l = get_input()
    d = defaultdict(int)
    for v in l:
        d[v] += 1
    
    num_days = 256
    for day in range(num_days):
        new_d = {}
        for i in range(9):
            if i not in d:
                continue
            if i == 0:
                new_d[6] = d[i]
                new_d[8] = d[i]
            else:
                if (i-1) not in new_d:
                    new_d[i-1] = 0
                new_d[i-1] += d[i]
        d = new_d
    return sum(d.values())

if __name__ == '__main__':
    main()
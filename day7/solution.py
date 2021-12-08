
def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_crabs():
    with open('input.txt', 'r') as f:
        return list(sorted([int(x) for x in f.readline().strip().split(',')]))

def part_one():
    crabs = get_crabs()
    med = crabs[len(crabs)//2]

    med_count = 0
    for i in range(len(crabs)):
        crab = crabs[i]
        med_count += abs(med - crab)
    return med_count

def part_two():
    crabs = get_crabs()
    best_count = -1
    for i in range(min(crabs), max(crabs) + 1):
        count = 0
        for crab in crabs:
            diff = abs(i - crab)
            count += (diff * (diff+1)) // 2
        if best_count == -1 or count < best_count:
            best_count = count
    return best_count

if __name__ == '__main__':
    main()
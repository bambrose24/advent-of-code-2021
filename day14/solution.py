
from typing import List, Tuple
from collections import defaultdict

def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_input() -> Tuple[str, List[Tuple[str, str]]]:
    with open('input.txt', 'r') as f:
        template = f.readline().strip()
        empty = f.readline().strip()
        if len(empty) > 0:
            raise Exception('non empty second line', empty)
        res = []
        for l in f.readlines():
            a,b = l.split('->')
            a,b = a.strip(),b.strip()
            res.append((a,b))
        return template,dict(res)

def part_one():
    return run_steps_clever(10)

def part_two():
    return run_steps_clever(40)

def run_steps_clever(step_count):
    template,formulas = get_input()
    pair_counts = defaultdict(int)
    counts = defaultdict(int)
    for i in range(len(template)-1):
        pair_counts[template[i] + template[i+1]] += 1
        counts[template[i]] += 1
    counts[template[-1]] += 1
    for _ in range(step_count):
        new_counts = defaultdict(int)
        for pair,val in pair_counts.items():
            if pair in formulas:
                mapping = formulas[pair]
                new_counts[pair[0] + mapping] += val
                new_counts[mapping + pair[1]] += val
                counts[mapping] += val
            else:
                new_counts[pair] += val
        pair_counts = new_counts
    # return counts
    return max(counts.values()) - min(counts.values())


def run_steps_normal(step_count):
    template,formulas = get_input()
    curr = template
    for _ in range(step_count):
        i = 0
        while i < len(curr) - 1:
            ab = curr[i] + curr[i+1]
            if ab in formulas:
                replacement = curr[i] + formulas[ab] + curr[i+1]
                curr = curr[:i] + replacement + curr[i+2:]
                i+=1
            i+=1
    counts = {}
    for c in curr:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return max(counts.values()) - min(counts.values())


if __name__ == '__main__':
    main()
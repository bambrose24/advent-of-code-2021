
from typing import List


def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)

    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_lines() -> List[str]:
    with open('input.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]

def part_one():
    lines = get_lines()
    total = 0
    for line in lines:
        bad_char = None
        stack = []
        for i in range(len(line)):
            c = line[i]
            if not is_closed(c):
                stack.insert(0, c)
            else:
                if not matches(stack, c):
                    bad_char = c
                    break
        if bad_char:
            total += score(bad_char)
    return total

def score(c):
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137
    raise Exception(f"no score found for char {c}")

def get_score2(c):
    if c == ')':
        return 1
    if c == ']':
        return 2
    if c == '}':
        return 3
    if c == '>':
        return 4
    raise Exception(f"no score2 found for char {c}")


def is_closed(c):
    return c in {')', ']', '}', '>'}

def pairs():
    return {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

def matches(stack, c):
    if len(stack) == 0:
        return False
    prev = stack.pop(0)
    return (prev == '(' and c == ')') \
        or (prev == '[' and c == ']') \
        or (prev == '{' and c == '}') \
        or (prev == '<' and c == '>')

def part_two():
    lines = get_lines()
    scores = []
    p = pairs()
    for line in lines:
        bad_char = None
        stack = []
        for i in range(len(line)):
            c = line[i]
            if not is_closed(c):
                stack.insert(0, c)
            else:
                if not matches(stack, c):
                    bad_char = c
                    break
        if not bad_char:
            curr_score = 0
            while len(stack) > 0:
                c = p[stack.pop(0)]
                score2 = get_score2(c)
                curr_score = (curr_score * 5) + score2
            scores.append(curr_score)

    return list(sorted(scores))[len(scores)//2]

if __name__ == '__main__':
    main()
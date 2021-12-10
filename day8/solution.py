
from typing import List, Tuple


segment_set_to_num = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_input() -> Tuple[List[str], List[str]]:
    res = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            l,r = line.split('|')
            res.append((l.strip().split(' '), r.strip().split(' ')))
        return res

def part_one():
    nums_input = get_input()
    total = 0
    for training,output in nums_input:
        for num in output:
            if len(num) in {2,3,4,7}:
                total += 1
    return total

def part_two():
    nums_input = get_input()
    total = 0
    for training,output in nums_input:
        figured_out_map = {} # Dict[Tuple[str], int]
        segment_map = {} # Dict[str, str]

        # figure out the 7 top segment
        seven = [x for x in training if len(x) == 3][0]
        one = [x for x in training if len(x) == 2][0]
        top_char = list(set(seven) - set(one))[0]
        segment_map[top_char] = 'a'

        # find the top part of 1 -- 6, 9, and 0 have six segments
        # but only 6 will have a single overlap with 1
        six = [x for x in training if len(x) == 6 and len(set(x).intersection(set(one))) == 1][0]
        bottom_part_of_one = list(set(six).intersection(set(one)))[0]
        top_part_of_one = list(set(one) - set(bottom_part_of_one))[0]
        segment_map[top_part_of_one] = 'c'
        segment_map[bottom_part_of_one] = 'f'
        
        # next figure out middle rung based on seven overlap with the size five ones
        # (3, 5, 2) -- only 3 will have full intersection (len 3). From there, we can
        # intersect with 4, and get the middle rung, and upper left one from the remaining of 4
        three = [x for x in training if len(x) == 5 and len(set(x).intersection(set(seven))) == 3][0]
        four = [x for x in training if len(x) == 4][0]
        middle_bar = list(set(three).intersection(set(four)) - set(one))[0]
        segment_map[middle_bar] = 'd'
        top_left = list(set(four) - set(one + middle_bar))[0]
        segment_map[top_left] = 'b'

        # now use 9 to get the bottom bar because we have all of 9 except that
        figured_out = set(segment_map.keys())
        nine = [x for x in training if len(x) == 6 and set(x).intersection(figured_out) == figured_out][0]
        bottom_bar = list(set(nine) - figured_out)[0]
        segment_map[bottom_bar] = 'g'

        # remaining one is bottom left
        bottom_left = [x for x in 'abcdefg' if x not in segment_map][0]
        segment_map[bottom_left] = 'e'

        # great! now we can map the output to sets of strings, sort the strings, and
        # index into segment_set_to_num to find the value, and accrue a result string to find an integer
        # print('segment map')
        # for k in segment_map:
        #     print(' ', k, segment_map[k])
        # print()

        # test = {
        #     'one': one,
        #     'seven': seven,
        #     'three': three,
        #     'four': four,
        #     'six': six,
        #     'nine': nine,
        # }
        # for k,v in test.items():
        #     digit_res = ''
        #     for c in v:
        #         digit_res += str(segment_map[c])
        #     digit_res = ''.join(sorted(digit_res))
        #     print('digit res for', k, f"({v})", digit_res)
        #     print(segment_set_to_num[digit_res])


        digits = ''
        for mixed_digit_str in output:
            digit_res = ''
            for c in mixed_digit_str:
                digit_res += str(segment_map[c])
            digit_res = ''.join(sorted(digit_res))
            digits += str(segment_set_to_num[digit_res])

        total += int(digits)
    return total
    

if __name__ == '__main__':
    main()
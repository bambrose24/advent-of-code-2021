from collections import defaultdict

def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def part_one():
    with open('input.txt', 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        size = len(lines[0])
        epsilon = ''
        gamma = ''
        for index in range(size):
            counts = defaultdict(int)
            for i in range(len(lines)):
                 counts[lines[i][index]] += 1
            if counts['1'] < counts['0']:
                epsilon += '1'
                gamma += '0'
            else:
                epsilon += '0'
                gamma += '1'
            
        epsilon = int(epsilon, 2)
        gamma = int(gamma, 2)
        return epsilon * gamma


def part_two():
    with open('input.txt', 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        size = len(lines[0])
        epsilon = ''
        gamma = ''
        oxygen_remaining = [x for x in lines]
        carbon_remaining = [x for x in lines]
        for index in range(size):
            if len(oxygen_remaining) > 1:
                oxygen_counts = defaultdict(int)
                for i in range(len(oxygen_remaining)):
                    oxygen_counts[oxygen_remaining[i][index]] += 1
                oxygen_char = '0' if oxygen_counts['1'] < oxygen_counts['0'] else '1'
                oxygen_remaining = [x for x in oxygen_remaining if x[index] == oxygen_char]

            if len(carbon_remaining) > 1:
                carbon_counts = defaultdict(int)
                for i in range(len(carbon_remaining)):
                    carbon_counts[carbon_remaining[i][index]] += 1
                carbon_char = '1' if carbon_counts['1'] < carbon_counts['0'] else '0'
                carbon_remaining = [x for x in carbon_remaining if x[index] == carbon_char]
            
        carbon = int(carbon_remaining[0], 2)
        oxygen = int(oxygen_remaining[0], 2)
        return carbon * oxygen

if __name__ == '__main__':
    main()
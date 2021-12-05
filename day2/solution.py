
def main():
    part_one()
    part_two()

def part_two():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        xpos = 0
        ypos = 0
        aim = 0
        for l in lines:
            action,num = l.split(' ')
            num = int(num)
            if action == 'forward':
                xpos += num
                ypos += (aim * num)
            elif action == 'down':
                aim += num
            elif action == 'up':
                aim -= num
        print('Part 2 answer:', xpos * ypos)


def part_one():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        xpos = 0
        ypos = 0
        for l in lines:
            action,num = l.split(' ')
            num = int(num)
            if action == 'forward':
                xpos += num
            elif action == 'down':
                ypos += num
            elif action == 'up':
                ypos -= num
        print('Part 1 answer:', xpos * ypos)

if __name__ == '__main__':
    main()

def main():
    count = 0
    with open('input.txt', 'r') as f:
        l = f.readlines()
        prev = int(l[0]) + int(l[1]) + int(l[2])
        for i in range(1, len(l) - 2):
            curr = int(l[i]) + int(l[i+1]) + int(l[i+2])
            if curr > prev:
                count += 1
            prev = curr
    print('Answer:', count)


if __name__ == '__main__':
    main()
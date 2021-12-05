
def main():
    count = 0
    with open('input.txt', 'r') as f:
        l = f.readlines()
        prev = int(l[0])
        for i in range(1, len(l)):
            curr = int(l[i])
            if curr > prev:
                count += 1
            prev = curr
    print('Answer:', count)


if __name__ == '__main__':
    main()
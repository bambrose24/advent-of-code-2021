
from typing import List, Tuple
import re

def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)
    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)


def get_board() -> Tuple[List[int], List[List[List[int]]]]:
    with open('input.txt', 'r') as f:
        inputs = [int(x) for x in f.readline().strip().split(',')]

        boards = []
        curr_board = []
        for l in f:
            l = l.strip()
            if l == '':
                boards.append(curr_board)
                curr_board = []
            else:
                curr_board.append([int(x.strip()) for x in re.split(r"\s+", l)])
        boards.append(curr_board)
    return (inputs, [x for x in boards if len(x) > 0])

def mark_board(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == num:
                board[i][j] = -1

def score_board(board, n):
    total = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] > 0:
                total += board[i][j]
    return total * n

def has_bingo(board):
    # rows
    for i in range(len(board)):
        row_set = set(board[i])
        if -1 in row_set and len(row_set) == 1:
            return True

    # cols
    for i in range(len(board)):
        col = set()
        for j in range(len(board[i])):
            col.add(board[j][i])
        if -1 in col and len(col) == 1:
            return True
    
    return False
        
def print_board(board):
    res = "\n"
    for row in board:
        row_str = ''
        for i in range(len(row)):
            n = row[i]
            if n < 10:
                row_str += f"{n}  "
            else:
                row_str += f"{n} "
        res += row_str + "\n"
    print(res)


def part_one():
    nums,boards = get_board()
    for i in range(len(nums)):
        n = nums[i]
        for j in  range(len(boards)):
            board = boards[j]
            mark_board(board, n)
            if has_bingo(board):
                return score_board(board, n)

    return None

def part_two():
    nums,boards = get_board()
    scores = []
    bingo_cache = set()
    for i in range(len(nums)):
        n = nums[i]
        for j in  range(len(boards)):
            if j not in bingo_cache:
                board = boards[j]
                mark_board(board, n)
                if has_bingo(board):
                    bingo_cache.add(j)
                    scores.append(score_board(board, n))
        if len(scores) == len(boards):
            break
    return scores[-1]

if __name__ == '__main__':
    main()
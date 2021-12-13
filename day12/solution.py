
from typing import List, Optional
from collections import defaultdict

def main():
    p1_answer = part_one()
    print('Part 1 Answer:', p1_answer)

    p2_answer = part_two()
    print('Part 2 Answer:', p2_answer)

def get_graph():
    with open('input.txt', 'r') as f:
        g = {}
        for line in f.readlines():
            a,b = line.strip().split('-')
            if a not in g:
                g[a] = []
            if b not in g:
                g[b] = []
            g[a].append(b)
            g[b].append(a)
        return g

def part_one():
    paths = []
    dfs1(get_graph(), 'start', 'end', [], paths)
    return len(paths)

def dfs1(graph, start_node, end_node, curr_path, paths):
    small = is_small(start_node)
    if small:
        if start_node in curr_path:
            return
    curr_path = curr_path + [start_node]
    if start_node == end_node:
        paths.append(curr_path)
        return
    for other in graph[start_node]:
        dfs1(graph, other, end_node, curr_path, paths)
    return


def is_small(c: str) -> bool:
    return c.lower() == c

def part_two():
    paths = []
    dfs2(get_graph(), 'start', 'end', [], paths)
    return len(paths)

def dfs2(graph, start_node, end_node, curr_path, paths):
    small = is_small(start_node)
    if small:
        curr_counts = defaultdict(int)
        for n in curr_path:
            if is_small(n):
                curr_counts[n] += 1
        if start_node in curr_counts and (2 in curr_counts.values() or start_node == 'start'):
            return
    curr_path = curr_path + [start_node]
    if start_node == end_node:
        paths.append(curr_path)
        return
    for other in graph[start_node]:
        dfs2(graph, other, end_node, curr_path, paths)
    return

if __name__ == '__main__':
    main()
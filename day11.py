from util import * 

import sys
from collections import defaultdict, deque, namedtuple
from dataclasses import dataclass, field
from math import *
from typing import *
from itertools import *

# from intcode import *

# import math
# from statistics import mean

DEBUG = '-v' in sys.argv
if DEBUG: sys.argv.remove('-v')
def dprint(*args, **kwargs): 
    if DEBUG: print(*args, **kwargs)

INPUT = 'day11_input.txt' if len(sys.argv) == 1 else sys.argv[1]

# import numpy as np 
# import scipy as sp

def parse(lines):
    out = [] 
    for l in lines:
        l = l.strip()
        out.append(list(l))
    return out 
# parse = parse_by_blank

# def solve_1(data):
#     data = set(data)
#     device = max(data) + 3
    
#     paths = [(device, )]
#     while paths:
#         print(paths)
#         path = paths.pop() 
#         tail = path[-1]

#         if tail == 0: return path

#         for i in range(3):
#             if tail - i in data - set(path):
#                 paths.append(path + (tail - i, ))

#     return paths

SHIFTS = [(-1)]

OCCUPIED = "#"
EMPTY = 'L'
FLOOR = '.'

def count_adjacent(seats, r, c):
    x = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0: continue
            for mul in count(1):
                r2 = r+dr*mul
                c2 = c+dc*mul
                if not (0 <= r2 < len(seats) and 0 <= c2< len(seats[0])): break
                if seats[r2][c2] == OCCUPIED:
                    x += 1
                    break
                if seats[r2][c2] == EMPTY:
                    break
    # print(r, c, x)
    return x

from copy import deepcopy

def solve_1(data): 
    return
    # print(data)

    prev = data
    changed = True
    while changed:
        changed = False

        new_state = deepcopy(prev)
        for r in range(len(new_state)):
            for c in range(len(new_state[0])):
                old = prev[r][c]
                if old == FLOOR: continue
                if old == EMPTY:
                    if count_adjacent(prev, r, c) == 0:
                        new = OCCUPIED
                    else:
                        new = EMPTY
                elif old == OCCUPIED:
                    if count_adjacent(prev, r, c) >= 4:
                        new = EMPTY
                    else:
                        new = OCCUPIED
                if new != old: changed = True
                new_state[r][c] = new

        prev = new_state

    return sum(sum(x == OCCUPIED for x in row) for row in new_state)

from sortedcontainers import sorteddict, sortedlist
from functools import lru_cache

def solve_2(data):

    non_floor = []
    neighbours = {}
    for r in range(len(data)):
        for c in range(len(data[0])):
            x = set() 
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == dc == 0: continue
                    for mul in count(1):
                        r2 = r+dr*mul
                        c2 = c+dc*mul
                        if not (0 <= r2 < len(data) and 0 <= c2< len(data[0])): break
                        if data[r2][c2] == FLOOR: continue
                        x.add((r2, c2))
                        break
            neighbours[r, c] = x

            if data[r][c] != FLOOR:
                non_floor.append((r, c))

    # row_seats = defaultdict(sortedlist.SortedList)
    # col_seats = defaultdict(sortedlist.SortedList)
    # dd_seats = defaultdict(sortedlist.SortedList)
    # du_seats = defaultdict(sortedlist.SortedList)

    # def adj(r, c):
    #     dd = r + c
    #     du = r - c

    #     x = 0
    #     if row_seats[r]:
    #         x += row_seats[r][0] < c
    #         x += row_seats[r][-1] > c
    #     if col_seats[c]:
    #         x += col_seats[c][0] < r
    #         x += col_seats[c][-1] > r
    #     if du_seats[du]:
    #         x += du_seats[du][0] < dd
    #         x += du_seats[du][-1] > dd
    #     if dd_seats[dd]:
    #         x += dd_seats[dd][0] < du
    #         x += dd_seats[dd][-1] > du
    #     return x

    num_adjacent = defaultdict(int)

    while True:
        # a, b, c2, d = row_seats, col_seats, dd_seats, du_seats

        new_occupied = []
        new_empty = []

        for r, c in non_floor:
            old = data[r][c]
            if old == FLOOR: continue

            new = old
            adj = num_adjacent[(r, c)]
            if old == EMPTY:
                if adj == 0:
                    new = OCCUPIED
            elif old == OCCUPIED:
                if adj >= 5:
                    new = EMPTY

            if new != old: 
                if new == OCCUPIED:
                    new_occupied.append((r, c))
                else:
                    new_empty.append((r, c))

        for r, c in new_empty:
            data[r][c] = EMPTY
            for x in neighbours[r, c]:
                num_adjacent[x] -= 1

        for r, c in new_occupied:
            data[r][c] = OCCUPIED
            for x in neighbours[r, c]:
                num_adjacent[x] += 1

        # print('---')
        # for row in row_seats.values():
        #     x = [' ']*len(data[0])
        #     for i in row:
        #         x[i] = '#'
        #     print(''.join(x))
        # for row in data:
        #     print(''.join(row))
        # input()

        if not new_occupied and not new_empty:
            break

    # print(row_seats)
    # print(col_seats)
    # print(dd_seats)
    # print(du_seats)

    return sum(x == OCCUPIED for row in data for x in row)

    print(sum(len(y) for y in col_seats.values()    ))
    print(sum(len(y) for y in dd_seats.values()    ))
    print(sum(len(y) for y in du_seats.values()    ))

    return x


if __name__ == "__main__":
    with open(INPUT) as f:
        data = parse(f.readlines())
        print('sol 1:', solve_1(data))
        print()
        f.seek(0)
        print('sol 2:', solve_2(data))
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

INPUT = 'dayXX_input.txt' if len(sys.argv) == 1 else sys.argv[1]

# import numpy as np 
# import scipy as sp

def parse(lines: List[str]):
    return

def process(data):
    return

def solve_1(data, extra):
    return

def solve_2(data, extra):
    return 

if __name__ == "__main__":
    with open(INPUT) as f:
        data = parse(f.readlines())
        extra = process(data)
        print('sol 1:', solve_1(data, extra))
        print()
        print('sol 2:', solve_2(data, extra))
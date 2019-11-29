#!/usr/bin/env python3

import math
from time import time

def count_lattice_paths(n):
    """
    Counts the total number of possible routes in an `n`x`n` grid
    from the top left to the bottom right moving only down and right.
    """
    return int(math.factorial(2 * n) / math.factorial(n)**2)

if __name__ == '__main__':
    start = time()
    solu = count_lattice_paths(20)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

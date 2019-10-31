#!/usr/bin/env python3

import numpy as np
from time import time

def sum_sqr_diff(n):
    """
    Calculates the difference between the sum of squares of hte first
    `n` natural numbers and the square of the sum.
    """
    sum_of_sqr = np.sum(np.square(np.arange(n + 1)))
    sqr_of_sum = int(((n * (n + 1)) / 2)**2)
    return sqr_of_sum - sum_of_sqr

if __name__ == '__main__':
    start = time()
    solu = sum_sqr_diff(100)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

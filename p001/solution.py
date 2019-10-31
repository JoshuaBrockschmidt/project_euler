#!/usr/bin/env python3

import numpy as np
from time import time

def sum_mults_3_5(limit):
    threes = np.arange(3, 1000, 3)
    fives = np.arange(5, 1000, 5)
    nums = np.unique(np.concatenate((threes, fives)))
    return np.sum(nums)

if __name__ == '__main__':
    start = time()
    solu = sum_mults_3_5(1000)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

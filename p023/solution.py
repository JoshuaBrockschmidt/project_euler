#!/usr/bin/env python3

import numpy as np
from time import time

ABU_LIMIT = 28123

def sum_nonabundant_sums():
    not_sums = np.arange(0, ABU_LIMIT)

    # Find all abundant numbers.
    abun = []
    prop_sums = []
    for i in range(1, ABU_LIMIT):
        # Sum all of the proper divisors.
        div_sum = 1
        for d in range(2, int(i**0.5) + 1):
            if i % d == 0:
                if d == i / d:
                    div_sum += d
                else:
                    div_sum += d + int(i / d)
        if div_sum > i:
            abun.append(i)
            for a in abun:
                sum_two = a + i
                if sum_two < len(not_sums):
                    not_sums[sum_two] = 0
                else:
                    break

    # Calculate sum of all positive integers which cannot be written as the sum
    # of two abundant numbers.
    return np.sum(not_sums)

if __name__ == '__main__':
    start = time()
    solu = sum_nonabundant_sums()
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

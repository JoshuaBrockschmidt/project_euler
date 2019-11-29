#!/usr/bin/env python3

import numpy as np
import math
from time import time

def find_largest_collatz(limit):
    cache = {1: 1}
    max_n = 1
    for n in range(2, limit):
        to_update = []
        m = n
        while True:
            is_even = m % 2 == 0
            if is_even:
                m = int(m / 2)
            else:
                m = int(3 * m + 1)

            to_update.insert(0, m)
            if m in cache:
                break

        clen = cache[to_update[0]] + 1
        for u in to_update[1:]:
            cache[u] = clen
            clen += 1
        cache[n] = clen

        if cache[n] > cache[max_n]:
            max_n = n

    return max_n

if __name__ == '__main__':
    start = time()
    solu = find_largest_collatz(int(1e6))
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

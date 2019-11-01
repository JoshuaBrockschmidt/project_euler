#!/usr/bin/env python3

from time import time

def find_tri_div(n):
    """ Find the smallest triangle number with over `n` divisors. """
    if n < 1:
        return 1
    # Start with the 2nd triangular number
    tri = 3
    num = 2
    while True:
        # Start divisor count with 1 and the number itself.
        div_cnt = 2
        i = 2
        limit = tri
        while True:
            if i >= limit:
                break
            if tri % i == 0:
                div_cnt += 2
                limit = int(tri / i)
            i += 1
        if div_cnt > n:
            return tri
        num += 1
        tri += num

if __name__ == '__main__':
    start = time()
    solu = find_tri_div(500)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

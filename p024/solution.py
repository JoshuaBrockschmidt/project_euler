#!/usr/bin/env python3

from math import factorial as fact
from time import time

def get_nth_lex_perm(n):
    nums = list(range(0, 10))
    assert n < fact(len(nums))

    perm = []
    m = n - 1
    while len(nums) > 0:
        div = fact(len(nums) - 1)
        to_pop = int(m // div)
        perm.append(nums.pop(to_pop))
        m = m % div

    res = ''.join(map(str, perm))
    return res

if __name__ == '__main__':
    start = time()
    solu = get_nth_lex_perm(1e6)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

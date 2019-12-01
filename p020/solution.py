#!/usr/bin/env python3

import math
from time import time

N = 100

def fact_digit_sum(n):
    res = math.factorial(n)
    print(res)
    total = 0
    for c in str(res):
        digit = int(c)
        total += digit
    return total

if __name__ == '__main__':
    start = time()
    solu = fact_digit_sum(N)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

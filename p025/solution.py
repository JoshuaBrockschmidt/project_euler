#!/usr/bin/env python3

from math import log10
from time import time

def first_fib_with_n_digits(n):
    fib1 = 1
    fib2 = 1
    if n == 1:
        return 1
    else:
        i = 3
        while True:
            old_fib1 = fib1
            fib1 = fib2
            fib2 = old_fib1 + fib2
            if int(log10(fib2)) + 1 == n:
                return i
            i += 1

if __name__ == '__main__':
    start = time()
    solu = first_fib_with_n_digits(1000)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

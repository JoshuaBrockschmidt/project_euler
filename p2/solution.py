#!/usr/bin/env python3

from time import time

def fib_sum(limit):
    prev2 = 1
    prev1 = 2
    fib_sum = 0
    while prev2 < limit:
        # There is probably a more clever solution that skips the calculation
        # of every 1st and 3rd element.
        # For now, we will just cherry-pick the even values.
        if prev1 % 2 == 0:
            fib_sum += prev1
        old_prev1 = prev1
        prev1 = prev1 + prev2
        prev2 = old_prev1
    return fib_sum

if __name__ == '__main__':
    start = time()
    solu = fib_sum(4e6)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

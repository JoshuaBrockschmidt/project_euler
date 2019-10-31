#!/usr/bin/env python3

from time import time

def sum_primes_below(n):
    """ Calculates the sum of all primes below `n`. """
    primes = [2, 3]
    num = primes[-1] + 2
    while num < n:
        is_prime = True
        limit = int(num**0.5)
        for p in primes:
            if p > limit:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2

    return sum(primes)

if __name__ == '__main__':
    start = time()
    solu = sum_primes_below(2e6)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

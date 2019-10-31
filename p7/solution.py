#!/usr/bin/env python3

from time import time

def get_nth_prime(n):
    """ Calculates the `n`th prime. """
    primes = [2, 3]
    num = primes[-1] + 2
    while len(primes) < n:
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
    return primes[-1]

if __name__ == '__main__':
    start = time()
    solu = get_nth_prime(10001)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

#!/usr/bin/env python3

from time import time

def smallest_mult(upper):
    """
    Find the smallest positive number that is evenly divisible from all
    numbers from 1 to `upper`.
    """
    # Find all prime number between 1 and `upper`.
    primes = [2, 3]
    for n in range(primes[-1] + 2, upper + 1, 2):
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
        if is_prime:
            primes.append(n)

    # Count the maximum number of times each prime is a factor of each number
    # between 1 and `upper`.
    factor_cnt = {p : 1 for p in primes}
    for n in range(1, upper + 1):
        cur_fact_cnt = {}
        while n > 1:
            for p in primes:
                if n % p == 0:
                    if p in cur_fact_cnt:
                        cur_fact_cnt[p] += 1
                    else:
                        cur_fact_cnt[p] = 1
                    n /= p
        for fact, cnt in cur_fact_cnt.items():
            factor_cnt[fact] = max(factor_cnt[fact], cnt)

    num = 1
    for fact, cnt in factor_cnt.items():
        num *= fact**cnt
    return num

if __name__ == '__main__':
    start = time()
    solu = smallest_mult(20)
    elapse = time() - start
    print('\nSolution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

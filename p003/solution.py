#!/usr/bin/env python3

from time import time

def get_max_factor(num):
    known_primes = [2, 3]
    max_fact = -1
    while True:
        limit = int(num**0.5) + 1
        found = False
        # Test remaining factor against our known primes.
        for kp in known_primes:
            if num % kp == 0:
                num /= kp
                max_fact = max(max_fact, kp)
                found = True
        if found:
            continue

        # Find new primes.
        for p in range(known_primes[-1], limit, 2):
            # Check if `p` is a prime.
            is_prime = True
            for kp in known_primes:
                if p % kp == 0:
                    is_prime = False
                    break
            if is_prime:
                known_primes.append(p)
                if num % kp == 0:
                    num /= kp
                    max_fact = max(max_fact, kp)
                    found = True
                    break

        if not found:
            max_fact = max(max_fact, num)
            break
    return max_fact

if __name__ == '__main__':
    start = time()
    solu = get_max_factor(600851475143)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

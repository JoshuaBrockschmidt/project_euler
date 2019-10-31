#!/usr/bin/env python3

from time import time

def find_pythagorean_triplet(n):
    """ Find a Pythagorean triplet a^2+b^2=c^2 for which a+b+c=`n`. """
    for c in range(n - 2, 0, -1):
        for a in range(n - c - 1, 0, -1):
            b = n - c - a
            # Check if a,b,c form a valid Pythagorean triplet.
            if a**2 + b**2 == c**2:
                return a, b, c

if __name__ == '__main__':
    start = time()
    a, b, c = find_pythagorean_triplet(1000)
    elapse = time() - start
    print('Pythagorean triplet found: {} + {} + {} = 1000'.format(a, b, c))
    print('\nSolution: {}'.format(a * b * c))
    print('Solution found in {:.8f}s'.format(elapse))

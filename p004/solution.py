#!/usr/bin/env python3

from time import time

def is_palindrome(num):
    digits = str(num)
    for i in range(int(len(digits) / 2)):
        if digits[i] != digits[-(i + 1)]:
            return False
    return True

def largest_palin():
    largest = 0
    factors = []
    for i in range(999, 99, -1):
        for j in range(i - 1, 99, -1):
            prod = i * j
            if prod <= largest:
                break
            elif is_palindrome(prod):
                largest = prod
                factors = (i, j)
                break
    print('Largest palindrome with 3 digits: {} x {} = {}\n'.format(
        factors[0], factors[1], prod))
    return largest

if __name__ == '__main__':
    start = time()
    solu = largest_palin()
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

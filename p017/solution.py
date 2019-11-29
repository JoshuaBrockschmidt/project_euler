#!/usr/bin/env python3

import inflect
from time import time

def count_alpha(s):
    total = 0
    for c in s:
        if c.isalpha():
            total += 1
    return total

def count_letters_1_to_1000():
    p = inflect.engine()
    words = map(p.number_to_words, range(1, 1001))
    letter_cnt = sum(map(count_alpha, words))
    return letter_cnt

if __name__ == '__main__':
    start = time()
    solu = count_letters_1_to_1000()
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

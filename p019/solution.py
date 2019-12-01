#!/usr/bin/env python3

from time import time

# 0 for January, 1 for February, ..., 11 for December
MONTH_LENS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

assert len(MONTH_LENS) == 12
assert sum(MONTH_LENS) == 365

def count_first_sundays():
    num_sundays = 0

    # 0 for Sunday, 1 for Monday, ..., 6 for Saturday
    cur_day = (366 - 6) % 7

    for year in range(1901, 2001):
        for i, mlen in enumerate(MONTH_LENS):
            if cur_day == 0:
                num_sundays += 1

            if i == 1 and year % 4 == 0:
                mlen += 1
            cur_day = (cur_day + mlen) % 7

    return num_sundays

if __name__ == '__main__':
    start = time()
    solu = count_first_sundays()
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

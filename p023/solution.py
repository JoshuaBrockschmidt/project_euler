#!/usr/bin/env python3

from time import time

ABU_LIMIT = 28123

def sum_nonabundant_sums():
    # Find all abundant numbers.
    abun = []
    prop_sums = []
    for i in range(1, ABU_LIMIT):
        # Sum all of the proper divisors.
        div_sum = 1
        for d in range(2, int(i**0.5) + 1):
            if i % d == 0:
                if d == i / d:
                    div_sum += d
                else:
                    div_sum += d + int(i / d)
        if div_sum > i:
            abun.append(i)

    # Calculate sum of all positive integers which cannot be written as the sum
    # of two abundant numbers.
    total = 0
    for i in range(1, 28123):
        if i % 1000 == 0:
            print(i, total)
        is_abun_sum = False
        lims = [0 for _ in range(len(abun))]
        for j, n in enumerate(abun):
            if n > i:
                break
            for k in range(max(j, lims[j]), len(abun)):
                m = abun[k]
                abun_sum = n + m
                if abun_sum > i:
                    lims[j] = k - 1
                    break
                elif abun_sum == i:
                    is_abun_sum = True
                    break
            if is_abun_sum:
                break
        if not is_abun_sum:
            total += i
    return total

if __name__ == '__main__':
    start = time()
    solu = sum_nonabundant_sums()
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

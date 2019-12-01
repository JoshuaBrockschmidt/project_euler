#!/usr/bin/env python3

from time import time

def sum_amicable_nums(n):
    # Calculate the sum of properr divisors for all numbers [1, n).
    upper_bound = n
    prop_sums = []
    i = 1
    while i < upper_bound:
        div_sum = 1
        for d in range(2, int(i**0.5) + 1):
            if i % d == 0:
                div_sum += d + int(i / d)
        prop_sums.append(div_sum)

        if i < n and div_sum > upper_bound:
            upper_bound = div_sum + 1
        i += 1

    # Find all amicable numbers and sum them.
    sum_amic = 0
    for i, b in enumerate(prop_sums[:n]):
        if i == 0:
            continue
        a = i + 1
        j = b - 1
        if prop_sums[j] == a and a != b:
            print(a)
            sum_amic += a

    return sum_amic

if __name__ == '__main__':
    start = time()
    solu = sum_amicable_nums(10000)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

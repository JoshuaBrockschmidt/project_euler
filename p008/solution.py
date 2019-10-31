#!/usr/bin/env python3

from time import time

DIGITS = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

def greatest_prod(digits, n):
    """ Find the `n` adjacent digits in `digits` with the greatest product. """
    # Calculate the product of the first `n` digits.
    prod = 1
    zero_cnt = 0
    for c in digits[:n]:
        d = int(c)
        if d > 1:
            prod *= d
        elif d == 0:
            zero_cnt += 1
    max_prod = prod

    # Evaluate all other products.
    for i in range(1, len(digits) - n + 1):
        # Divide by the left-most digit/factor of the previous product.
        left = int(digits[i - 1])
        if left > 1:
            prod /= left
        elif left ==0:
            zero_cnt -= 1

        # Multiply by our new right-most digit.
        right = int(digits[i + n - 1])
        if right > 1:
            prod *= right
        elif right == 0:
            zero_cnt += 1

        # As long as there are zeros within our `n` adjacent digits,
        # our product is 0 and should be ignored.
        if zero_cnt == 0:
            max_prod = max(max_prod, prod)

    return int(max_prod)

if __name__ == '__main__':
    start = time()
    solu = greatest_prod(DIGITS, 13)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

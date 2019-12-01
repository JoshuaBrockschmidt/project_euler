#!/usr/bin/env python3

from time import time

from triangle import Triangle

TRI_PATH = 'triangle.txt'

def find_max_tri_path(tri):
    best_tri = tri.copy()

    # Go from bottom-up.
    num_rows = tri.get_num_rows()
    for row in range(num_rows - 2, -1, -1):
        for col in range(best_tri.get_num_cols(row)):
            cur = (row, col)
            left, right = best_tri.get_next_below(cur)
            new_val = best_tri.get_val(cur) + max(best_tri.get_val(left), best_tri.get_val(right))
            best_tri.set_val(cur, new_val)

    return best_tri.get_val((0, 0))

if __name__ == '__main__':
    start = time()
    tri = Triangle(TRI_PATH)
    solu = find_max_tri_path(tri)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

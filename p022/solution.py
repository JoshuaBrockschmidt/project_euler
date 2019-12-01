#!/usr/bin/env python3

from time import time

NAME_PATH = 'p022_names.txt'

def load_names(path):
    names = []
    with open(path, 'r') as f:
        content = f.readlines()[0]
        for name in content.split(','):
            names.append(name[1:-1].upper())
    return names

def total_name_score(path):
    names = load_names(path)
    names.sort()
    total = 0
    for i, name in enumerate(names):
        pos_score = i + 1
        alpha_score = 0
        for c in name:
            alpha_score += ord(c) - 64
        total += pos_score * alpha_score
    return total

if __name__ == '__main__':
    start = time()
    solu = total_name_score(NAME_PATH)
    elapse = time() - start
    print('Solution: {}'.format(solu))
    print('Solution found in {:.8f}s'.format(elapse))

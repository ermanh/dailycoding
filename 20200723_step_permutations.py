'''
There exists a staircase with N steps, and you can climb up either 1 or 2 
steps at a time. Given N, write a function that returns the number of unique 
ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could 
climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

from itertools import permutations


def step_permutations_simple(N):
    basic = [1 for _ in range(N)]
    procedures = [tuple(basic)]

    while len([n for n in basic if n == 1]) > N % 2:
        basic = basic[2:] + [2]
        perms = (permutations(basic))
        for perm in perms:
            if perm not in procedures:
                procedures.append(perm)

    print(procedures)
    return len(procedures)


'''
# TESTS

step_permutations_simple(2) == 2
step_permutations_simple(3) == 3
step_permutations_simple(4) == 5
step_permutations_simple(5) == 8
step_permutations_simple(6) == 13
'''

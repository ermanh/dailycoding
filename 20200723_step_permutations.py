'''
2020-07-23
[from dailycodingproblem.com #12]
# TODO: Customized steps solution still a work in progress

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

from collections import defaultdict, OrderedDict
from itertools import permutations


def step_permutations_simple(N):
    """Calculates the number of unique ways to climb a staircase of N steps 
    by increments of 1 step and/or 2 steps
    """
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


class StepPermutations:
    """Calculates the number of unique ways to climb a staircase of N steps 
    by increments of all possible permutations of a customized list of steps
    """

    def __init__(self, N, steps):
        self.N = N
        self.steps = sorted(steps)
        self.subs = self.substitutions()
        self.procedures = []
        self.step_permutations()

    def base_steps(self):
        basics = []
        for i in range(len(self.steps)):
            basic = []
            for step in self.steps[i:] + self.steps[:i]:
                if sum(basic) == self.N:
                    break
                while sum(basic) + step > self.N:
                    if len(basic) > 0:
                        basic.pop()
                    else:
                        break
                basic += [step for _ in range((self.N - sum(basic)) // step)]
            basics.append(basic)
        basics = [b for b in basics if sum(b) == self.N]
        return basics

    def substitutions(self):
        substitutions = OrderedDict()
        for i, larger in enumerate(self.steps[1:], start=1):
            mixed_sum = []
            for j, smaller in enumerate(self.steps[:i]):
                if larger % smaller == 0:
                    substitutions[larger] = [smaller for _
                                             in range(int(larger/smaller))]
                else:
                    while larger > sum(mixed_sum) + self.steps[j+1]:
                        mixed_sum.append(smaller)
            if larger == sum(mixed_sum):
                substitutions[larger] = mixed_sum
        return substitutions

    def is_subset(self, smaller_list, larger_list):
        smaller_dict = defaultdict(int)
        larger_dict = defaultdict(int)
        for s in smaller_list:
            smaller_dict[s] += 1
        for l in larger_list:
            larger_dict[s] += 1
        if all(key in larger_dict for key in smaller_dict):
            if all([smaller_dict[key] <= larger_dict[key] for key in smaller_dict]):
                return True
        return False

    def new_variations(self, start):
        procedures = []
        for procedure in self.procedures[start:]:
            for key in self.subs:
                new_variation = []
                value_list = [v for v in self.subs[key]]
                if self.is_subset(value_list, procedure):
                    for num in procedure:
                        if num in value_list:
                            for i, v in enumerate(value_list):
                                if num == v:
                                    value_list.pop(i)
                                    break
                        else:
                            new_variation.append(num)
                if len(value_list) == 0:
                    new_variation.append(key)

                if sum(new_variation) == self.N:
                    new_perms = permutations(new_variation)
                    for np in new_perms:
                        if np not in procedures and np not in self.procedures:
                            procedures.append(np)

        return procedures, start

    def step_permutations(self):
        if min(self.steps) > self.N:
            return 0

        basics = self.base_steps()
        if len(basics) == 0:
            return 0

        for basic in basics:
            basic_perms = permutations(basic)
            for bp in basic_perms:
                if bp not in self.procedures:
                    self.procedures.append(bp)

        start = 0
        while len(self.new_variations(start)[0]) > 0:
            new_procedures, new_start = self.new_variations(start)
            start = new_start + len(self.procedures)
            self.procedures += new_procedures

    def ways(self):
        return len(self.procedures)



'''
# TESTS

step_permutations_simple(2) == 2
step_permutations_simple(3) == 3
step_permutations_simple(4) == 5
step_permutations_simple(5) == 8
step_permutations_simple(6) == 13

StepPermutations(2, [1, 2]).ways() == 2
StepPermutations(3, [1, 2]).ways() == 3
StepPermutations(4, [1, 2]).ways() == 5
StepPermutations(5, [1, 2]).ways() == 8
StepPermutations(6, [1, 2]).ways() == 13

StepPermutations(4, [1, 3, 5]).ways() == 3
StepPermutations(5, [1, 3, 5]).ways() == 5  # TODO
StepPermutations(6, [1, 3, 5]).ways() == 8  # TODO
StepPermutations(7, [1, 3, 5]).ways() == 12  # TODO
StepPermutations(8, [1, 3, 5]).ways() == 19  # TODO
StepPermutations(9, [1, 3, 5]).ways() == 30  # TODO
StepPermutations(10, [1, 3, 5]).ways() == 47  # TODO

StepPermutations(18, [3, 5, 7]) == 12  # FAIL, returns only 1
StepPermutations(19, [3, 5, 7]) ==  # TODO
StepPermutations(20, [3, 5, 7]) ==  # TODO
StepPermutations(21, [3, 5, 7]) ==  # TODO
StepPermutations(22, [3, 5, 7]) ==  # TODO
StepPermutations(23, [3, 5, 7]) ==  # TODO
'''

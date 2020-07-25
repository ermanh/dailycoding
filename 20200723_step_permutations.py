'''
2020-07-23
[from dailycodingproblem.com #12]

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
    ways = [tuple(basic)]

    while len([n for n in basic if n == 1]) > N % 2:
        basic = basic[2:] + [2]
        perms = (permutations(basic))
        for perm in perms:
            if perm not in ways:
                ways.append(perm)

    print(ways)
    return len(ways)


class StepPermutations:
    """Calculates the number of unique ways to climb a staircase of N steps 
    by increments of all possible permutations of a customized list of step
    lengths passed as an argument
    """

    def __init__(self, N, step_lengths):
        self.N = N
        self.steps = sorted(step_lengths)
        self.substitutions = self._substitutions()
        self.ways = []
        self._step_permutations()

    def _substitutions(self):
        """Returns a dictionary where larger step lengths are keys, and if
        they can be composed of combinations of smaller step lengths, those 
        combinations are stored as their values
        """
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
    
    def _base_steps(self):
        """Returns a list of ways to achieve N steps using more 
        straightforward looping techniques
        """
        basics = []
        for i in range(len(self.steps)):

            # If N = 5, steps = [2, 3], then basic_variations would become
            # [[2, 2], [2], [3]]
            basic_variations = []
            for step in self.steps:
                variation = [step for _ in range(self.N // step)]
                while len(variation) > 0:
                    basic_variations.append([v for v in variation])
                    variation.pop()

            # Adds other step lengths to each list in basic_variations
            for basic in basic_variations:
                for step in self.steps[i:] + self.steps[:i]:
                    if step in basic and len(set(basic)) == 1:
                        break
                    if sum(basic) == self.N:
                        break
                    while sum(basic) + step > self.N:
                        if len(basic) > 0:
                            basic.pop()
                        else:
                            break
                    basic += [step for _
                              in range((self.N - sum(basic)) // step)]
                basics.append(basic)

        basics = [b for b in basics if sum(b) == self.N]
        return basics

    def _is_subset(self, smaller_list, larger_list):
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

    def _new_variations(self, start_index):
        """Goes through each step combo/progression in self.ways 
        starting at start_index, and replaces combinations of smaller steps 
        with larger steps using the self.substitutions dictionary, and returns 
        the new combos/progressions created
        """
        ways = []
        for way in self.ways[start_index:]:
            for key in self.substitutions:
                new_variation = []
                value_list = [v for v in self.substitutions[key]]
                if self._is_subset(value_list, way):
                    for num in way:
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
                        if np not in ways and np not in self.ways:
                            ways.append(np)

        return ways, start_index

    def _step_permutations(self):
        """Core function for creating the unique ways to climb N steps using
        above worker functions
        """
        if min(self.steps) > self.N:
            return 0

        basics = self._base_steps()
        if len(basics) == 0:
            return 0

        for basic in basics:
            basic_perms = permutations(basic)
            for bp in basic_perms:
                if bp not in self.ways:
                    self.ways.append(bp)

        start_index = 0
        while len(self._new_variations(start_index)[0]) > 0:
            new_ways, new_start_index = self._new_variations(start_index)
            start_index = new_start_index + len(self.ways)
            self.ways += new_ways

    def count(self):
        return len(self.ways)


'''
# TESTS

step_permutations_simple(2) == 2
step_permutations_simple(3) == 3
step_permutations_simple(4) == 5
step_permutations_simple(5) == 8
step_permutations_simple(6) == 13

StepPermutations(2, [1, 2]).count() == 2
StepPermutations(3, [1, 2]).count() == 3
StepPermutations(4, [1, 2]).count() == 5
StepPermutations(5, [1, 2]).count() == 8
StepPermutations(6, [1, 2]).count() == 13

StepPermutations(4, [1, 3, 5]).count() == 3
StepPermutations(5, [1, 3, 5]).count() == 5
StepPermutations(6, [1, 3, 5]).count() == 8
StepPermutations(7, [1, 3, 5]).count() == 12
StepPermutations(8, [1, 3, 5]).count() == 19
StepPermutations(9, [1, 3, 5]).count() == 30
StepPermutations(10, [1, 3, 5]).count() == 47

StepPermutations(11, [3, 4, 5]).count() == 6
StepPermutations(12, [3, 4, 5]).count() == 8
StepPermutations(13, [3, 4, 5]).count() == 10
StepPermutations(14, [3, 4, 5]).count() == 13
StepPermutations(15, [3, 4, 5]).count() == 18
StepPermutations(16, [3, 4, 5]).count() == 24
StepPermutations(17, [3, 4, 5]).count() == 31

StepPermutations(18, [3, 5, 7]).count() == 17 
StepPermutations(19, [3, 5, 7]).count() == 18
StepPermutations(20, [3, 5, 7]).count() == 25
StepPermutations(21, [3, 5, 7]).count() == 32
StepPermutations(22, [3, 5, 7]).count() == 37
StepPermutations(23, [3, 5, 7]).count() == 52
'''

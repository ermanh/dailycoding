'''
WORK IN PROGRESS
[from dailycodingproblem.com #34]
# Log 2020-07-08 
# -- two tests fail (words with a partial palindrome in the middle)
# -- execution time extremely slow when string > 6 chars, because of 
#    exponential increase in number of permutations, need a better method

Given a string, find the palindrome that can be made by inserting the fewest 
number of characters as possible anywhere in the word. If there is more than 
one palindrome of minimum length that can be made, return the 
lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we 
can add three letters to it (which is the smallest amount to make a 
palindrome). There are seven other palindromes that can be made from "race" 
by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''
from collections import defaultdict
from itertools import permutations


def is_palindrome(string):
    mid_point = round(len(string) / 2)
    if ''.join(reversed(string[:mid_point])) == string[-mid_point:]:
        return True
    return False

def has_original_sequence(candidate, string):
    """Filter out palindromes where the original string is no longer in its
    original sequence"""
    copy = list(string)
    for i in range(len(candidate) - 1, -1, -1):
        if len(copy) == 0:
            break
        if copy[-1] == candidate[i]:
            copy.pop()

    if len(copy) == 0:
        return True
    return False

def has_partial_palindrome(string, is_reverse=False):
    copy = ''.join(reversed(string)) if is_reverse else string
    palindromes = []

    mid_point = round(len(copy) / 2)
    before = list(reversed(copy[:mid_point]))
    after = list(copy[mid_point:])

    palindrome_start = mid_point - 1
    for _ in range(mid_point):
        if before == after[:len(before)]:
            break
        else:
            after = [before[0]] + after
            before = before[1:]
            palindrome_start -= 1

    if palindrome_start >= 0:
        candidate = ''.join(
            reversed(copy[palindrome_start * 2 + 2:])) + copy
        if is_reverse:
            candidate = ''.join(reversed(candidate))
        palindromes.append(candidate)

    return palindromes

def palindrome(string):
    # check if already a palindrome
    if is_palindrome(string):
        return string

    had_partial_palindromes = []
    letters = defaultdict(int)
    for s in string:
        letters[s] += 1

    had_partial_palindromes += has_partial_palindrome(string)
    had_partial_palindromes += has_partial_palindrome(string, is_reverse=True)

    letters_to_add = []
    if len(set(string)) == len(string):
        for i, s in enumerate(string):
            letters_to_add.append(string + string[:i] + string[i+1:])

    else:
        for i in range(1, max(letters.values()) + 1):
            to_add = string
            for key in letters:
                if letters[key] == i:
                    to_add += key * i
            letters_to_add.append(to_add)

    palindromes = list(had_partial_palindromes)
    for l in letters_to_add:
        p = permutations(l)
        for item in p:
            if (
                is_palindrome(''.join(item)) and 
                has_original_sequence(''.join(item), string)
            ):
                palindromes.append(''.join(item))

    palindromes.sort(key=lambda x: (len(x), x))
    return palindromes[0]


'''
# TESTS

# Words with no repeated letters
palindrome('race') == 'ecarace'
palindrome('pear') == 'pearaep'
palindrome('stare') == 'erastsare'  

# Words with partial palindromes 
palindrome('google') == 'elgoogle'  # front
palindrome('alool') == 'aloola'  # end
palindrome('timid') == 'dtimitd'  # inside  # FAIL
palindrome('vvdfaa') == 'aafdvvdfaa'  # both front and end 
palindrome('ttimidd') == 'ddttimittdd'  # everywhere  # FAIL

# Words with some repeated letters but no partial palindromes
palindrome('ravage') == 'egravvarge'
palindrome('effort') == 'etrofforte'
palindrome('leeves') == 'lsevevesl'
'''

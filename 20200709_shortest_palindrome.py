'''
2020-07-09
[from dailycodingproblem.com #34]

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

# Solution Comment: 
# Execution speed is slow if string length >= 10 without repeated chars

from collections import defaultdict
from itertools import permutations, combinations


def is_palindrome(string):
    mid_point = round(len(string) / 2)
    if ''.join(reversed(string[:mid_point])) == string[-mid_point:]:
        return True
    return False

def has_original_sequence(candidate, string):
    copy = list(string)
    for i in range(len(candidate) - 1, -1, -1):
        if len(copy) == 0:
            break
        if copy[-1] == candidate[i]:
            copy.pop()

    if len(copy) == 0:
        return True
    return False

def mirror(string):
    single_pivot_mirror = ''.join(reversed(string)) + string[1:]
    full_mirror = ''.join(reversed(string)) + string
    return [single_pivot_mirror, full_mirror]

def permutate_mirror_and_check(candidate, string):
    palindromes = []
    for p in permutations(candidate):
        maybes = mirror(''.join(p))
        maybes = [m for m in maybes 
                  if (is_palindrome(m) and has_original_sequence(m, string))]
        palindromes += maybes
    return palindromes

def palindrome(string):
    letters = defaultdict(int)
    for s in string:
        letters[s] += 1
    
    base = ''.join([key for key in letters])
    palindromes = permutate_mirror_and_check(base, string)
    if len(palindromes) > 0:
        palindromes.sort(key=lambda x: (len(x), x))
        return palindromes[0]

    for i in range(2, max(letters.values()) + 1):
        letters_to_add = [key for key in letters if letters[key] >= i]
        for j in range(1, len(letters_to_add) + 1):
            for c in combinations(letters_to_add, j):
                expanded = base + ''.join(c)
                palindromes += permutate_mirror_and_check(expanded, string)
        if len(palindromes) > 0:
            palindromes.sort(key=lambda x: (len(x), x))
            return palindromes[0]

    return ''


'''
# TESTS

# Words with no repeated letters
palindrome('race') == 'ecarace'
palindrome('pear') == 'pearaep'
palindrome('stare') == 'erastsare'  

# Words with partial palindromes on the edges
palindrome('google') == 'elgoogle'  
palindrome('alool') == 'aloola'  
palindrome('vvdfaa') == 'aafdvvdfaa'  
palindrome('aardvark') == 'akrardvdrarka'

# Words with partial palindromes inside
palindrome('timid') == 'dtimitd'  
palindrome('ravage') == 'egravarge'
palindrome('effort') == 'etrofforte'
palindrome('leeves') == 'lsevevesl'

# Words with partial palindromes everywhere
palindrome('ttimidd') == 'ddttimittdd'

# Longer words
palindrome('antiestablishment')

# Empty string returns empty string
palindrome('') == ''
'''

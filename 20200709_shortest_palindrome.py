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
# Execution speed is slow if string length ~> 10 without repeated chars 
# because of using permutations and combinations

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
    for p in sorted(permutations(candidate), reverse=True):
        maybes = mirror(''.join(p))
        maybes = [m for m in maybes
                  if (is_palindrome(m) and has_original_sequence(m, string))]
        maybes.sort(key=lambda x: len(x))
        if len(maybes) > 0:
            return maybes[:1]
    return []

def palindrome(string):
    letters = defaultdict(int)
    for s in string:
        letters[s] += 1

    base = ''.join([key for key in letters])
    palindromes = permutate_mirror_and_check(base, string)
    if len(palindromes) > 0:
        return palindromes[0]

    for i in range(2, max(letters.values()) + 1):
        to_add = [key for key in letters if letters[key] >= i]
        for j in range(1, len(to_add) + 1):
            combos = (base + ''.join(c) for c in combinations(to_add, j))
            batch = (permutate_mirror_and_check(c, string) for c in combos)
            tops = (sorted(b, key=lambda x: (len(x), x))[:1] for b in batch)
            for t in tops:
                palindromes += t
                palindromes.sort(key=lambda x: (len(x), x))
                palindromes = palindromes[:1]
        if len(palindromes) > 0:
            return palindromes[0]
        base += ''.join(to_add)

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
palindrome('leeves') == 'lesevesel'
                          
# Words with partial palindromes everywhere
palindrome('ttimidd') == 'ddttimittdd'

# Longer words
palindrome('establish') == 'ehsilbatablishe'
palindrome('establishm') == 'emhsilbatablishme'
palindrome('establishme') == 'emhsilbatablishme'
palindrome('establishmen') == 'nemhsilbatablishmen'
palindrome('establishment')  # TAKES TOO LONG TO EXECUTE

# Empty string returns empty string
palindrome('') == ''
'''

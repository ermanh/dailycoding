'''
WIP
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
from collections import defaultdict
from itertools import permutations


def palindrome(string):
    palindrome_candidates = []
    
    # google type palindrome
    letters = defaultdict(int)
    
    for s in string:
        letters[s] += 1

    letters_to_add = []
    more_letters_to_add = []

    if len(letters) < len(string):
        for key in letters:
            if letters[key] == 1:
                letters_to_add.append(key)
            if letters[key] > 2:
                more_letters_to_add.append(key)

        jumbles = [s for s in string] + letters_to_add
        jumbles += more_letters_to_add
        palindrome_candidates = permutations(jumbles)

        for key in letters:
            if letters[key] > 2:
                letters_to_add.append(key)

    # race type palindrome
    else:
        for s in string:
            jumbles = [c for c in string] + [c for c in string if c != s]
            palindrome_candidates += [p for p in permutations(jumbles)]

    palindromes = []
    for candidate in palindrome_candidates:
        c = ''.join(candidate)
        mid_point = round(len(c) / 2)
        first_half = ''.join(reversed(c[:mid_point]))
        back_half = c[mid_point:]

        if len(c) % 2 != 0:
            back_half = c[-mid_point:]

        if first_half == back_half:
            copy = list(string)

            for i in range(len(c) - 1, -1, -1):
                if len(copy) == 0:
                    break

                if copy[-1] == c[i]:
                    copy.pop()

            if len(copy) == 0:
                palindromes.append(''.join(c))

    palindromes.sort(key=lambda x: (x, len(x)))
    return palindromes[0]

'''
# TESTS

palindrome('race') == 'ecarace'
palindrome('google') == 'elgoogle'
palindrome('ravage') == 'egravvarge'
palindrome('effort') == 'etrofforte'
palindrome('leeves') == 'lsevevesl'
palindrome('aardvark') == 'kravdraardvark'
palindrome('crazyeights')


racecar


'''

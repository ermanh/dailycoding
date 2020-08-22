'''
2020-08-22
[from dailycodingproblem.com #81]

Given a mapping of digits to letters (as in a phone number), and a digit 
string, return all possible letters the number could represent. You can assume 
each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should 
return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
'''

MAPPING = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

def mappings(string):
    mappings = [MAPPING[char] for char in string]
    combos = [char for char in mappings[0]]
    for i, letters in enumerate(mappings[1:], start=1):
        for char in letters:
            for combo in combos:
                if len(combo) == i:
                    combos.append(combo + char)
        combos = [combo for combo in combos if len(combo) == i + 1]
    return combos


'''
# TESTS

set(mappings('23')) == set(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

'free' in mappings('3733')
len(mappings('3733')) == len(set(mappings('3733')))

'flowers' in mappings('3569377')
len(mappings('3569377')) == len(set(mappings('3569377')))
'''

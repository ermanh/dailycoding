'''
2020-07-01
[from dailycodingproblem.com #31]

The edit distance between two strings refers to the minimum number of 
character insertions, deletions, and substitutions required to change one 
string to the other. For example, the edit distance between “kitten” and 
“sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, 
and append a “g”.

Given two strings, compute the edit distance between them.
'''

def edit_distance(string1, string2):
    """This solution assumes appending can occur in either direction
    """
    longer = string1 if len(string1) >= len(string2) else string2
    shorter = string2 if longer == string1 else string1
    distance = len(longer)

    # check only up to the index on the longer word where the number of
    # chars uncompared is still less than the length of the longer word
    for i in range(len(longer) - round(len(shorter)/2) + 1):
        
        uncompared = (len(longer) + len(shorter) 
                      - min([len(longer[i:]), len(shorter)]) * 2)
        count = sum([l != s for l, s in zip(longer[i:], shorter)])
        
        if uncompared + count < distance:
            distance = uncompared + count
    
    # check the other direction
    for i in range(len(shorter)):
        
        uncompared = (len(longer) + len(shorter)
                      - len(shorter[i:]) * 2)
        count = sum([s != l for s, l in zip(shorter[i:], longer)])
        
        if uncompared + count < distance:
            distance = uncompared + count

    return distance


'''
# TESTS (must all return True)

edit_distance('kitten', 'sitting') == 3
edit_distance('kitten', 'kittens') == 1
edit_distance('smitten', 'kitten') == 2 
edit_distance('correction', 'action') == 5
edit_distance('preemptively', 'priestly') == 9
edit_distance('attorney general', 'general attorney') == 15
edit_distance('antiestablishmentarian', 'establishmentarians') == 5
edit_distance('establishmentarian', 'mentarianisms') == 13
edit_distance('even-handednesses', 're-elections') == 15 
edit_distance('abcde', 'efghi') == 5
edit_distance('abcde', 'cdefg') == 4
edit_distance('abcde', 'cdefgh') == 5
edit_distance('abc', 'bcdefghi') == 7
edit_distance('abc', 'bcdefgh') == 6
edit_distance('abcdefg', 'fghi') == 7
edit_distance('abcdefg', 'fgh') == 6
'''

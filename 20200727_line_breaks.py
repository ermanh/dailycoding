'''
2020-07-27
[from dailycodingproblem.com]

Given a string s and an integer k, break up the string into multiple lines 
such that each line has a length of k or less. You must break it up so that 
words don't break across lines. Each line has to have the maximum possible 
amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that 
there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" 
and k = 10, you should return: ["the quick", "brown fox", "jumps over", 
"the lazy", "dog"]. No string in the list has a length of more than 10.
'''

def line_breaks(string, k):
    lines = []
    line = ''
    for word in string.split(' '):
        if line == '':
            line = word
        else:
            if len(line + ' ' + word) <= k:
                line += ' ' + word
            else:
                lines.append(line)
                line = word
    lines.append(line)
    return lines


'''
# TESTS

line_breaks("the quick brown fox jumps over the lazy dog", 5) == [
    "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
line_breaks("the quick brown fox jumps over the lazy dog", 10) == [
    "the quick", "brown fox", "jumps over", "the lazy", "dog"]
line_breaks("the quick brown fox jumps over the lazy dog", 15) == [
    'the quick brown', 'fox jumps over', 'the lazy dog']
line_breaks("the quick brown fox jumps over the lazy dog", 20) == [
    'the quick brown fox', 'jumps over the lazy', 'dog']
'''


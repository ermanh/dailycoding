'''
[WORK IN PROGRESS - NOT COMPLETED YET]
[from www.dailycodingproblem.com #25]

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular 
expression and returns whether or not the string matches the regular 
expression.

For example, given the regular expression "ra." and the string "ray", your 
function should return true. The same regular expression on the string 
"raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function 
should return true. The same regular expression on the string "chats" should 
return false.
'''


def match(regex, string):
    if '**' in regex or regex[0] == '*':
        raise ValueError('Malformed regex')

    ri = len(regex) - 1
    si = len(string) - 1

    after_is_dot_all_with_asterisk = False
    after_is_normal_with_asterisk = False
    last_ri = None
    last_si = None

    threshold = 1 if regex[:2] == ".*" else -1
    while (ri > threshold and si > -1):
        if regex[ri] == '*':
            pre_pre_r = regex[ri-2] if ri - 2 >= 0 else None
            if regex[ri-1] == '.':
                if pre_pre_r == string[si]:
                    last_ri = ri
                    last_si = si
                    ri -= 3
                    si -= 1
                    after_is_dot_all_with_asterisk = True
                else:
                    si -= 1
            else:
                if (ri-2 >= 0 and regex[ri-2] == regex[ri-1]
                        and regex[ri-2] != '.'):
                    after_is_normal_with_asterisk = True
                    ri -= 2
                    continue
                if regex[ri-1] == string[si]:
                    si -= 1
                else:
                    ri -= 2
        elif regex[ri] == '.':
            ri -= 1
            si -= 1
        else:
            if regex[ri] == string[si]:
                ri -= 1
                si -= 1
                if after_is_normal_with_asterisk:
                    while string[si] == regex[ri+1]:
                        si -= 1
            else:
                if after_is_normal_with_asterisk:
                    if ri+4 < len(regex):
                        if regex[ri+4] != '*' and regex[ri+1] in [regex[ri+3], '.']:
                            after_is_normal_with_asterisk = False
                            continue
                    elif ri+3 < len(regex):
                        if regex[ri+1] in [regex[ri+3], '.']:
                            after_is_normal_with_asterisk = False
                            continue
                    ri -= 1
                    after_is_normal_with_asterisk = False
                else:
                    if after_is_dot_all_with_asterisk:
                        ri = last_ri
                        si = last_si - 1
                        after_is_dot_all_with_asterisk = False
                    else:
                        return False

    if si > -1:
        if (ri == 1 and regex[:2] == '.*' and si < len(string)-1
        and ri < len(regex) - 1):
            return True
        return False
    else:
        if ri > -1:
            if regex[1] == '*':
                return True
            return False
        else:
            return True
        

"""
Tests (should all return True)

match('asdf**asdf', 'asdf')  # ValueError
match('*asdf', 'asdf')  # ValueError

match('ra.', 'ray') == True 
match('ra.', 'raymond') == False
match('ra.*', 'raymond') == True

match('.*at', 'chat') == True
match('*.at', 'chat') == False
match('.*at', 'at') == True
match('.*at', 'nougat') == True

match('.*at.*', 'nougat') == True
match('.*at.*', 'atnou') == True

match('.*at*', 'attttt') == True
match('.at*', 'watt') == True
match('.at*', 'watson') == False

match('.at.*at.*at.*', 'batatat') == True
match('.at.*at.*at.*', 'batbatbatb') == True
match('.at.*at.*at.*', 'batbat') == False

match('.*at.*at.*at.*', 'atatat') == True
match('.*at.*at.*at.*', 'ratarataratara') == True

match('.*.*at', 'at') == True
match('t*t*at', 'at') == True
match('t*t*at', 'tat') == True
match('t*t*at', 'ttat') == True
match('t*t*at', 'tttttttttttat') == True
match('t*t*at', 'abat') == False

match('att*t*', 'at') == True
match('att*t*', 'att') == True
match('att*t*', 'attt') == True 
match('att*t*', 'atttt') == True 
match('att*t*', 'atab') == False

match('att*ta', 'atta') == True
match('att*ta', 'atttta') == True
match('att*ta', 'atbta') == False
match('att*ta', 'ata') == False

match('att*.*t*ta', 'atta') == True
match('att*.*t*ta', 'atttta') == True
match('att*.*t*ta', 'atbta') == True
match('att*.*t*ta', 'atbtbtta') == True
"""



'''
2020-07-06
[from dailycodingproblem.com #27]

Given a string of round, curly, and square open and closing brackets, return 
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''

def balanced(string):
    # start with placeholder to avoid index error / clumsy empty list checking
    ledger = [' ']  

    for s in string:
        last_open_bracket = ledger[-1]
        
        if s not in '({[]})':
            pass
        if s in '({[':
            if last_open_bracket not in ' ({[':
                return False
            ledger.append(s)
        elif s in ')}]':
            if (
                (s == ')' and last_open_bracket == '(') or
                (s == '}' and last_open_bracket == '{') or
                (s == ']' and last_open_bracket == '[')
            ):
                ledger.pop()
            else:
                return False
    
    if ledger[-1] != ' ':
        return False
    return True


'''
# TESTS (must all return True)

# Base cases from question
balanced("([])[]({})") == True
balanced("([)]") == False
balanced("((()") == False

balanced("((((((((((asdf))))))))))") == True
balanced("((((((((((asdf)))))))))))))") == False

# No brackets should still return True
balanced("asdf") == True 

# Starting with a closing bracket should return False
balanced("]asdf[") == False
balanced("))asdf((") == False
balanced("}}}asdf") == False
'''

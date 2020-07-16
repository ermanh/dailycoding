'''
2020-07-16
[from dailycodingproblems.com #46]

Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana".
'''
'asdf'


def is_palindrome(string):
    mid_point = int(len(string)/2)
    front = string[:mid_point]
    back = ''.join(reversed(string[-mid_point:]))
    if front == back:
        return True
    return False

def longest_palindrome(string):
    palindromes = []
    
    for i in range(len(string)-1):
        for j in range(len(string), i, -1):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)
    
    if len(palindromes) > 0:
        palindromes.sort(key=lambda x: len(x))
        return palindromes[-1]
    return ''


'''
# TESTS

# No palindromes
longest_palindrome("") == ""
longest_palindrome("a") == ""  
longest_palindrome("abcde") == ""

# Full string palindromes
longest_palindrome("aa") == "aa"
longest_palindrome("i!i") == "i!i"  
longest_palindrome("racecar") == "racecar"

# Substring palindromes
longest_palindrome("aabcdcb") == "bcdcb" 
longest_palindrome("bananas") == "anana"
longest_palindrome("bbcccddddee") == "dddd"
longest_palindrome("racecaraceca") == "acecaraceca"
'''

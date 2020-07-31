'''
2020-07-31
[from dailycodingproblems.com #61]

Implement integer exponentiation. That is, implement the pow(x, y) function, 
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.
'''

# SOLUTION COMMENTS
# This solution takes the same number of processing turns as simple/naive
# multiplication when the exponent y is <= 4 (note: an exponent of y 
# programatically means self-multiplying [y - 1] times when y > 1), 
# but takes proportionally fewer and fewer turns with higher and higher 
# exponents, especially when the exponent is itself an exponentiation of 2, 
# plus 1 (see processing_turns in tests)


def exponentiate(x, y):
    if y == 1:
        return x
    if y == 0:
        return 1

    processing_turns = 1
    power = 2
    exponentiated = x * x
    while power * 2 < y:
        processing_turns += 1
        power *= 2
        exponentiated *= exponentiated
    
    for _ in range(y - power):
        processing_turns += 1
        exponentiated *= x

    print('processing_turns =', processing_turns)
    return exponentiated


'''
# TESTS
exponentiate(2, 10) == 2 ** 10        # processing_turns = 5
exponentiate(2, 9) == 2 ** 9          # processing_turns = 4
exponentiate(2, 8) == 2 ** 8          # processing_turns = 6
    
exponentiate(5, 7) == 5 ** 7          # processing_turns = 5
exponentiate(5, 6) == 5 ** 6          # processing_turns = 4
    
exponentiate(3, 5) == 3 ** 5          # processing_turns = 3
exponentiate(3, 4) == 3 ** 4          # processing_turns = 3
exponentiate(3, 3) == 3 ** 3          # processing_turns = 2
exponentiate(3, 2) == 3 ** 2          # processing_turns = 1
exponentiate(3, 1) == 3 ** 1          # processing_turns = 0
exponentiate(3, 0) == 3 ** 0          # processing_turns = 0

exponentiate(2, 258) == 2 ** 258      # processing_turns = 10
exponentiate(2, 257) == 2 ** 257      # processing_turns = 9
exponentiate(2, 256) == 2 ** 256      # processing_turns = 135

exponentiate(2, 129) == 2 ** 129      # processing_turns = 8
exponentiate(2, 128) == 2 ** 128      # processing_turns = 70

exponentiate(2, 65) == 2 ** 65        # processing_turns = 7
exponentiate(2, 50) == 2 ** 50        # processing_turns = 23
exponentiate(2, 40) == 2 ** 40        # processing_turns = 13
exponentiate(2, 33) == 2 ** 33        # processing_turns = 6

exponentiate(21, 23) == 21 ** 23
round(exponentiate(1.42, 7), 10) == round(1.42 ** 7, 10)  
'''

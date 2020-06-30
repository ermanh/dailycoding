""" Longest Common Subsequence (LCS)

A review/demo of recursive vs. dynamic approaches
[from https://www.techiedelight.com/longest-common-subsequence/]
"""

import timeit


# Recursive approach
# Worse case time complexity is O(2^(m+n))
def lcs_recursive(X, Y, m, n):

    if m == 0 or n == 0:
        return 0

    if X[m - 1] == Y[n - 1]:
        return lcs_recursive(X, Y, m-1, n-1) + 1

    return max(lcs_recursive(X, Y, m, n-1), lcs_recursive(X, Y, m-1, n))


# Recursive with dynamic approach, memorize steps to avoid duplicate processing
# WAY faster: O(mn) time complexity, auxiliary space also O(mn)
lookup = {}


def lcs_dynamic(X, Y, m, n, lookup):
    if m == 0 or n == 0:
        return 0
    key = (m, n)
    if key not in lookup:
        if X[m-1] == Y[n-1]:
            lookup[key] = lcs_dynamic(X, Y, m-1, n-1, lookup) + 1
        else:
            lookup[key] = max(lcs_dynamic(X, Y, m-1, n, lookup),
                              lcs_dynamic(X, Y, m, n-1, lookup))
    return lookup[key]


if __name__ == '__main__':

    X = 'ABCBDAB'
    Y = 'BDCABA'

    print("The length calculated from lcs_recursive is",
          lcs_recursive(X, Y, len(X), len(Y)))

    print("And execution time (n=10000):",
          timeit.timeit("lcs_recursive(X, Y, len(X), len(Y))",
                        setup="from lcs import X, Y, LCS",
                        number=10000))

    lookup = {}
    print("The length calculated from lcs_dynamic is",
          lcs_dynamic(X, Y, len(X), len(Y), lookup))

    print("And execution time (n=10000):",
          timeit.timeit("lcs_dynamic(X, Y, len(X), len(Y), lookup)",
                        setup="from lcs import X, Y, lookup, lcs_dynamic",
                        number=10000))

    # The dynamic approach is just slightly faster in this case, likely because
    # the strings being compared are rather short.

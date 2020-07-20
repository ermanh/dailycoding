'''
2020-07-20
[from dailycodingproblem.com #50]

Suppose an arithmetic expression is given as a binary tree. Each leaf is an 
integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

        *
       / \       .
      +    +
     / \  / \    .
    3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
'''


class Node:

    def __init__(self, node, left=None, right=None):
        if node not in ['*', '/', '+', '-'] and type(node) != int:
            raise ValueError('node must be an integer or ' + 
                             '"*", "/", "+", or "-"')
        self.node = node
        self.left = left
        self.right = right


def bintree_math(tree):
    if type(tree.node) == int:
        return tree.node
    
    elif tree.node in ['*', '/', '+', '-']:
        if tree.node == '*':
            return bintree_math(tree.left) * bintree_math(tree.right)
        elif tree.node == '/':
            return bintree_math(tree.left) / bintree_math(tree.right)
        elif tree.node == '+':
            return bintree_math(tree.left) + bintree_math(tree.right)
        elif tree.node == '-':
            return bintree_math(tree.left) - bintree_math(tree.right)


'''
# TESTS

tree = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
bintree_math(tree) == 45

tree = Node('/', Node('-', Node(3), Node(2)), Node('*', Node(4), Node(5)))
bintree_math(tree) == 0.05

tree = Node('-', Node('/', Node(3), Node(2)), Node('-', Node(4), Node(5)))
bintree_math(tree) == 2.5

tree = Node('+', Node('*', Node(3), Node(2)), Node('/', Node(4), Node(5)))
bintree_math(tree) == 6.8
'''

'''
2020-06-18
[from www.dailycodingproblem.com #3]

Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string back 
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node, level=1):
    serial = []
    if node:
        serial += [node.val]
        serial += ['#' * level] 
        serial += serialize(node.left, level + 1) if node.left else [None]
        serial += ['#' * level]
        serial += serialize(node.right, level + 1) if node.right else [None]
    else:
        serial += ['#' * level, None]
    return serial

def split(array):
    split_point = None

    if len(array) >= 4:
        breaker = array[0]    
        for i, val in enumerate(array[1:], start=1):
            if val == breaker:
                split_point = i
                break

    if split_point is not None:
        return array[1:split_point], array[split_point + 1:]
    return None, None

def deserialize(array):
    node = array[0]
    if node is None:
        return None
    left, right = split(array[1:])
    return Node(node, deserialize(left), deserialize(right))


'''
# Quick test

node = Node('root', Node('left', Node('left.left')), Node('right'))
serialize(node) == ['root', '#', 'left', '##', 'left.left', '###', None, 
                    '###', None, '##', None, '#', 'right', '##', None, 
                    '##', None]
deserialize(serialize(node)).left.left.val == 'left.left'
'''

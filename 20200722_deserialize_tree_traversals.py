'''
2020-07-22
[from dailycodingproblem.com #48]

Given pre-order and in-order traversals of a binary tree, write a function to 
reconstruct the tree.

For example, given the following preorder traversal:
[a, b, d, e, c, f, g]

And the following inorder traversal:
[d, b, e, a, f, c, g]

You should return the following tree:
        a
       / \          
      b   c
     / \ / \        
    d  e f  g

'''


class Node:

    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


def deserialize(preorder, inorder):
    """Recursively determine and return Nodes using a top-to-bottom approach
    """
    if len(preorder) == 0:
        return None

    elif len(preorder) == 1:
        return Node(root=preorder[0])

    else:
        if preorder == list(reversed(inorder)):
            return Node(root=preorder[0], 
                        left=deserialize(preorder[1:], inorder[:-1]))
        
        elif preorder == inorder:
            return Node(root=preorder[0],
                        right=deserialize(preorder[1:], inorder[1:]))
        
        else:
            root = preorder[0]
            right_inorder = []
            for node in list(reversed(inorder)):
                if node != root:
                    right_inorder.append(inorder.pop())
                else:
                    inorder.pop()
                    break
            
            left_inorder = list(inorder)
            right_inorder = list(reversed(right_inorder))
            left_preorder = preorder[1:len(left_inorder) + 1]
            right_preorder = preorder[-len(right_inorder):]

            return Node(root=root, 
                        left=deserialize(left_preorder, left_inorder), 
                        right=deserialize(right_preorder, right_inorder))


'''
# TESTS

preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
t = deserialize(preorder, inorder)
all([t.root == 'a',
     t.left.root == 'b',
     t.right.root == 'c',
     t.left.left.root == 'd',
     t.left.right.root == 'e',
     t.right.left.root == 'f',
     t.right.right.root == 'g']) == True

# Tree where one node has only one child
preorder = ['a', 'b', 'd', 'c', 'e', 'f']
inorder = ['d', 'b', 'a', 'e', 'c', 'f']
t = deserialize(preorder, inorder)
all([t.root == 'a',
     t.left.root == 'b',
     t.right.root == 'c',
     t.left.left.root == 'd',
     t.right.left.root == 'e',
     t.right.right.root == 'f']) == True

# Tree where children of root only have successive single children
preorder = ['a', 'b', 'd', 'f', 'c', 'e', 'g']
inorder = ['f', 'd', 'b', 'a', 'c', 'e', 'g']
t = deserialize(preorder, inorder)
all([t.root == 'a',
     t.left.root == 'b',
     t.right.root == 'c',
     t.left.left.root == 'd',
     t.right.right.root == 'e',
     t.left.left.left.root == 'f',
     t.right.right.right.root == 'g']) == True
'''
    
    
    

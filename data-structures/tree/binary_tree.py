"""
Authors:
Ron Megini - 318955499
Noy Krief - 206943045
"""

import random
from collections import deque


class Node:
    """
    Desc:
        Class Node
    Attr:
        data - data itself
        right - pointer to right node
        left - pointer to left node
    """
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self, treelist=''):
        if self.data==None:
            return
        #traverse left subtree
        inorder_print(self.left)
        #traverse current node
        print(self.data, end = '')
        treelist+=str(self.data)
        #traverse right subtree
        inorder_print(self.right)   
        return treelist


def islbt(root):
    """
    Desc:
        Return true if lbt, false either
    Param:
        root (Node Object) - pointer to Node root node
    Return:
        True / False
    """
    # Empty Node case - LBT
    if root is None:
        return True

    # No sons case - LBT
    elif root.right is None and root.left is None:
        return True

    # Right leaf only case - Not LBT
    elif root.right is not None and root.left is None:
        return False

    # Left son OR both case - keep check
    elif (root.right is not None and root.left is not None) or (root.right is None and root.left is not None):
        return (islbt(root.left) & islbt(root.right))


def count_sons(root):
    """
    Desc:
        Count the number of root + sons in a tree
    Param:
        root - Node object
    Return:
        number
    """
    if root is None:
        return 0
    else:
        return (count_sons(root.left) + count_sons(root.right) + 1)


def convert_tree_to_series(node, nodes_num, counter=0, series=list()):
    """
    Desc:
        Map tree into a list according to the format (size, left leafs, right leafs)
    Param:
        node - Node object to map
        nodes_num - the number of nodes in the tree
        counter - count the iterations
        series - record the series calsulated
    Return:
        list
    """
    if counter <= nodes_num:
        if not node:
            return list()
        series.append(count_sons(node))
        counter =+ 1
        if node.right is not None:
            convert_tree_to_series(node.right, nodes_num, counter, series)
        if node.left is not None:
            convert_tree_to_series(node.left, nodes_num, counter, series)
    return series


def generate_random_tree(size, counter=0, node=Node(random.randint(0,9))):
    if counter <= size:
        counter += 1
        if True:
            node.left = Node(random.randint(0,9))
            generate_random_tree(size,counter,node)
        if True:
            node.right = Node(random.randint(0,9))
            generate_random_tree(size,counter,node)
    return node

def inorder_print(root):
    #if root is None,return
    if root==None:
        return
    #traverse left subtree
    inorder_print(root.left)
    #traverse current node
    print(root.data, end = '')
    #traverse right subtree
    inorder_print(root.right)   

if __name__ == '__main__':

    MESSAGE = """Tree name: {}
Represented by this series (according to the task): {}
And is LBT (True/False): {}"""

    # Create the tree according to the example
    example_tree = Node(1)
    example_tree.left = Node(2)
    example_tree.right = Node(3)
    example_tree.left.left = Node(4)
    example_tree.left.left.left = Node(5)
    example_tree.right.left = Node(0)
    example_tree.right.right = Node(0)
    example_tree.right.left.left = Node(0)
    example_tree.right.left.left.left = Node(0)
    example_tree.right.left.left.right = Node(0)

    # Print example tree content
    print(MESSAGE.format("example_tree", convert_tree_to_series(example_tree, count_sons(example_tree)), islbt(example_tree)))
    example_tree_nodes_number = count_sons(example_tree)
    print("inorder scan:")
    print(example_tree)
    # Print random tree content
    rand_tree = generate_random_tree(20)
    print(MESSAGE.format("rand_tree", convert_tree_to_series(rand_tree, count_sons(rand_tree)), islbt(rand_tree)))
    example_tree_nodes_number = count_sons(rand_tree)


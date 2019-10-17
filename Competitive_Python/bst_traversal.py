'''
Binary Tree: Traversals and various Operations
(Inorder, PreOrder, PostOrder)
Author:: Pavan Kumar Paluri
'''

list_node = []
list_xor = []


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def in_order(node: Node):
    if node is not None:
        in_order(node.left)
        # When here
        print(f'{node.key}')
        list_node.append(node.key)
        # Now right
        in_order(node.right)


def pre_order(node: Node):
    # print(f'{node.key}')
    if node is not None:
        print(f'{node.key}')
        pre_order(node.left)
        pre_order(node.right)


def post_order(node: Node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(f'{node.key}')


# Given the BST, find the node with a min value and a max value
def min_node():

    # Do an inorder traversal
    return min(list_node)


def max_node():
    return max(list_node)


# search a given node to see if it is in the given BST
def search_node(key: int) -> bool:
    for val in range(len(list_node)):
        if list_node[val] == key:
            return True
    return False


# Find the max node at a given level in a binary tree
def find_max_node_level(root_node: Node, level: int) -> int:
    if root_node is None:
        return 0
        # if level is first, output its val
    if level == 0:
        return root_node.key
    elif root_node is not None:
        x = find_max_node_level(root_node.left, level-1)
        y = find_max_node_level(root_node.right, level-1)
        return max(x, y)


# Find the sum of all nodes at a given level in a Binary Search tree
def find_sum_node_level(root_node: Node, level: int) -> int:
    if root_node is None:
        return 0
    if level == 0:
        return root_node.key
    elif root_node is not None:
        # Explore left subtree
        x = find_sum_node_level(root_node.left, level-1)
        # Explore Right Subtree
        y = find_sum_node_level(root_node.right, level-1)
        return x+y


# Find the nodes in the given level, and then XOR it with each node
# in the BST.
def level_xor(root_node: Node, level_int: int):
    if root_node is None:
        return
    if level_int == 0:
        return root_node.key
    elif root_node is not None:
        x = level_xor(root_node.left, level_int-1)
        y = level_xor(root_node.right, level_int-1)
        # return max(x ^ val, y ^ val)
        if x != 0 or y != 0:
            if x is not None or y is not None:
                list_xor.append(x)
                list_xor.append(y)


if __name__ == '__main__':
    # Tree Construction
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(5)
    in_order(root)
    # pre_order(root)
    print(f'\n')
    post_order(root)
    print(f'Node with min key is: {min_node()} and max key is: {max_node()}')
    print(f'{search_node(int(input("Enter the key to search: ")))}')
    print(f'Max Node at level 0 :{find_max_node_level(root, 0)}')
    print(f'Sum of nodes at level 1 is: {find_sum_node_level(root, 1)}')
    # Set: {Level Number, XOR value} - STATIC input
    Q = [[2, 5], [0, 3], [1, 3], [3, 6]]
    for vals in range(len(Q)):
        level = Q[vals][0]
        XOR_val = Q[vals][1]
        level_xor(root, level)
        if level == 0:
            print(f'Max Val @ Level: {level} is: {root.key ^ XOR_val}')
            continue
        # Filter function to elimiate None's out of the list
        list_xor = list(filter(None, list_xor))
        for val in range(len(list_xor)):
            list_xor[val] = list_xor[val] ^ XOR_val
        print(f'Max val @ Level: {level} is : {max(list_xor)}')
        list_xor = []

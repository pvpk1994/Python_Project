'''
preorder, inorder, postorder iterative approaches
DO NOT USE RECURSION
Author: Pavan Kumar Paluri
Source: Leet Code
'''


class BstNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = False

    def in_order(self, root: BstNode) -> list:
        '''
        inorder iteration using stack concept
        :param root:
        :return:
        '''
        stack = []
        output = []
        current = root
        while stack or current:
            while current:  # is not None
                stack.append(current)
                current = current.left
            # if here current is none,
            current = stack.pop()  # pops the most recently inputted node
            output.append(current.key)
            current = current.right
        return output

    def post_order(self, root: BstNode) -> list:
        stack = [root, ]
        output = []
        '''
        Boundary Case: if root is none,
        '''
        if root is None:
            return []
        # Traverse and gather the elements in reverse order and then reverse the list.
        while stack:
            root = stack.pop()
            output.append(root.key)
            # since reverse order, collect left subtree elements
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return output[::-1]

    def pre_order(self, root: BstNode) -> list:
        stack = [root, ]
        output = []
        while stack:
            root = stack.pop()
            output.append(root.key)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return output

    def morris_inorder(self, root: BstNode):
        current = root
        while current:
            # If left subtree is none:
            if current.left is None:
                print(current.key)
                current = current.right
            # If left subtree is present..
            else:
                # Left subtree exploration begins...
                new_node = current.left
                while new_node.right is not None and new_node.right != current:
                    # Get to the right most node
                    new_node = new_node.right
                if new_node.right is None:
                    # Now is the time to link new_node's right to current.
                    new_node.right = current
                    # Advance current to its left for process repeatition...
                    current = current.left

                else:
                    # new_node.right is not None
                    # Therefore restore the right to its original state
                    new_node.right = None
                    print(current.key)
                    current = current.right

    def sum_traversal(self, root: BstNode, sum_num: int) -> bool:
        def helper(current_node: BstNode, key_sum: int):
            if current_node.left is None and current_node.right is None:
                # then we are definitely at the leaf node..
                if key_sum == sum_num:
                    self.ans = True
            if current_node.left is not None:
                # Explore left subtree
                helper(current_node.left, key_sum+current_node.left.key)
            if current_node.right is not None:
                # Explore the right subtree (But from very root again)
                helper(current_node.right, key_sum+current_node.right.key)
            # return False
        helper(root, root.key)
        return self.ans


if __name__ == '__main__':
    # Create a fixed BST
    bst_node = BstNode(1)
    bst_node.left = BstNode(-3)
    bst_node.left.left = BstNode(-2)
    bst_node.left.left.left = BstNode(7)
    bst_node.left.left.left.left = BstNode(-10)
    # bst_node.left.right = BstNode(4)
    # bst_node.right = BstNode(6)
    # bst_node.right.left = BstNode(8)
    # bst_node.right.right = BstNode(7)
    # inorder invoke
    new_inorder = Solution()
    print(new_inorder.in_order(bst_node))
    print(new_inorder.post_order(bst_node))
    print(new_inorder.pre_order(bst_node))
    # print(new_inorder.morris_inorder(bst_node))
    print(new_inorder.sum_traversal(bst_node, -7))




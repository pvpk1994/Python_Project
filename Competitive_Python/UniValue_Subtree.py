'''
Design a uni-value subtree
Author: Pavan Kumar Paluri
Source: LeetCode
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def check_bool_sub_tree(self, node: Node) -> bool:
        if node is None:
            return False
        if node.right is None and node.left is None:
            self.count += 1
            return True
        bool_var = True

        # begin subtree access (left and right)
        if node.left is not None:
            bool_var = self.check_bool_sub_tree(node.left) and node.left.val == node.val and bool_var
        if node.right is not None:
            bool_var = self.check_bool_sub_tree(node.right) and node.right.val == node.val and bool_var
        # if here, determine the count outcome based on bool_var result
        if bool_var is True:
            self.count += 1
        else:
            self.count += 0
        return bool_var

    def uni_val_sub_tree(self, root_node: Node) -> int:
        self.check_bool_sub_tree(root_node)
        return self.count


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(1)
    root.right = Node(5)
    root.left.right = Node(5)
    root.left.left = Node(5)
    root.right.left = Node(5)
    sol = Solution()
    print(sol.uni_val_sub_tree(root))


from collections import deque
'''
Level Order Traversal - Binary Tree
Author: Pavan Kumar Paluri
Source : LeetCode
'''

'''
Description: Display all the nodes of each level in separate sub-lists
2 Approaches - Recursive and Iterative for BFS 
DFS (Pre-order, post-order and in-order cannot be of much help here)
'''


class BstNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def level_order_traversal(self, root: BstNode) -> list:
        '''
        Iterative Approach
        :param root:
        :return:
        '''
        que = deque([root, ])
        output = []
        if root is None:
            return output
        level = 0
        while que:
            output.append([])
            # queue is maintained to get all nodes from a particular level...
            len_que = len(que)
            for _ in range(len_que):
                node = que.popleft()
                # Pop each node of que and put it in the level subarray
                output[level].append(node.key)
                # adding child nodes of current level, preparing for next level
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            # Proceed to next level
            level += 1
        return output

    def level_order_recursion(self, root: BstNode) -> list:
        '''
        Recursion Approach
        :param root:
        :param level:
        :return:
        '''
        output = []
        if root is None:
            return []

        def helper(node, level):
            # @ current level
            if len(output) == level:
                output.append([])
            output[level].append(node.key)

            if node.left is not None:
                helper(node.left, level+1)
            if node.right is not None:
                helper(node.right, level+1)
        helper(root, 0)
        return output

    def symmetric_tree(self, root: BstNode) -> bool:
        '''
        This Function handles edge cases as well, In that, it returns false if
        single leaf nodes do not form mirror images of one another...
        :param root: Root of BST
        :return: True or False
        '''
        # init a dequeue
        que = deque([root, root, ])
        while que:
            root1 = que.popleft()
            root2 = que.popleft()
            if root1 is None and root2 is None:
                continue
            if root1 is None or root2 is None:
                return False
            if root1.key != root2.key:
                return False

            que.append(root1.left)
            que.append(root2.right)

            que.append(root1.right)
            que.append(root2.left)
        return True

    def complete_symmetric_tree(self, root: BstNode) -> bool:
        '''
        Iterative approach
        Do a level order traversal and check if left subtree is an exact mirror image of right subtree
        :param root:
        :return:
        Shortcoming: Only works when the tree is a complete tree, else it treats both lonely leaf
        nodes as mirror images which is not true....
        '''
        if root is None:
            return True
        list_nodes = self.level_order_traversal(root)
        print(list_nodes)
        for lister in list_nodes:
            list_temp_1, list_temp_2, list_smth = [], [], []
            print(f'Lister index: {list_nodes.index(lister)}')
            if len(lister) == 1 and list_nodes.index(lister) != 0:
                return False
            mid = len(lister) // 2
            for i in range(0, mid):
                list_temp_1.append(lister[i])
            for j in range(mid, len(lister)):
                list_temp_2.append(lister[j])
            list_smth = list_temp_1.copy()
            list_smth.reverse()
            for val in range(len(list_smth)):
                if list_smth[val] == list_temp_2[val]:
                    continue
                else:
                    return False

        return True

    def level_order_zigzag(self, root:BstNode) -> list:
        '''
        Iterative yet Zig-Zag Level Order Traversal
        :param root:
        :return:
        '''
        que = deque([root, ])
        output = []
        level = 0
        if root is None:
            return []
        while que:
            output.append([])
            # Cal length of list
            len_list = len(que)
            for _ in range(len_list):
                node = que.popleft()
                output[level].append(node.key)
                '''
                To establish a zigzag pattern, for every even numbered
                level, the program appends left to the que first and then right..
                '''
                if node.left is not None and level % 2 is 0 and node.right is not None:
                    que.append(node.left)
                    que.append(node.right)
                elif node.left is not None and level % 2 is not 0 and node.right is not None:
                    que.append(node.right)
                    que.append(node.left)
            level += 1
        return output

    def get_depth(self, root: BstNode, level: int) -> int:
        # If root is Null,
        if root is None:
            raise AssertionError('Root is None, No tree to compute depth')
        if root.left is None and root.right is None and root is not None:
            self.ans = max(self.ans, level)
        if root.left is not None:
            self.get_depth(root.left, level+1)
        if root.right is not None:
            self.get_depth(root.right, level+1)
        return self.ans


if __name__ == '__main__':
    # Create a fixed BST
    bst_node = BstNode(1)
    bst_node.left = BstNode(3)
    bst_node.left.left = BstNode(2)
    bst_node.left.right = BstNode(4)
    bst_node.right = BstNode(6)
    bst_node.right.left = BstNode(8)
    bst_node.right.right = BstNode(7)
    bst_node.left.left.left = BstNode(11)
    # inorder invoke
    new_inorder = Solution()
    print(new_inorder.level_order_traversal(bst_node))
    print(new_inorder.level_order_recursion(bst_node))
    print(new_inorder.level_order_zigzag(bst_node))
    print(new_inorder.get_depth(bst_node, 0))
    # New symmetric tree Construction
    new_node = BstNode(1)
    new_node.left = BstNode(2)
    new_node.right = BstNode(2)
    new_node.left.left = BstNode(3)
    new_node.right.left = BstNode(3)
    new_level_traversal = Solution()
    print(f'Complete Symmetric Tree Function Returns: {new_level_traversal.complete_symmetric_tree(new_node)}')
    print(f'Symmetric Tree Function Returns: {new_level_traversal.symmetric_tree(new_node)}')




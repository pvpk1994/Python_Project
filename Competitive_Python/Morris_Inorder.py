'''
No Recursion, No Stack Inorder Iterative Approach
Morris Inorder Traversal
Author: Pavan Kumar Paluri
Time Complexity: O(n) - since each node is being visited while Traversal.
Space Complexity: O(1) - Since none of the nodes are being stored anywhere.
'''

class BstNode:
  def __init__(self, val):
    self.key = val
    self.right = None
    self.left = None

class Solution:
  # Morris Inorder Traversal
  def morris_inorder(self, root: BstNode):
    current = root
    while current is not None:
      # If left subtree is none:
      if current.left is None:
        # Simply explore right subtree
        print(current.key)
        current = current.right
      # however, if left subtree is not None
      else:
        new_node = current.left
        # Make sure we dock the current node to the rightmost leaf BstNode
        while new_node.right is not None and new_node.right != current:
          # Go to the last rightmost node now...
          new_node = new_node.right
        # If here, check for 2 conditions...
        if new_node.right is None:
          # Make current as right child 
          new_node.right = current
          # Now proceed with current to be current.left
          current = current.left
        else:
          # Restore the original left subtree as it is...
          # Dismiss the new_node.right now
          new_node.right = None
          print(current.key)
          current = current.right

root_node = BstNode(1)
root_node.left = BstNode(3)
root_node.left.left = BstNode(2)
root_node.left.right = BstNode(4)
root_node.right = BstNode(6)
root_node.right.left = BstNode(8)
root_node.right.right = BstNode(7)

Morris_Inorder = Solution()
Morris_Inorder.morris_inorder(root_node)

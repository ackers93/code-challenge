# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1, null, 2, 3]
#   1
#     \
#          2
#     /
#    3

# Output: [1, 3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode, result=None) -> List[int]:
        if result is None:
            result = list()

        if root is None:
            return []

        if root.left:
            self.inorderTraversal(root.left, result)

        result.append(root.val)

        if root.right:
            self.inorderTraversal(root.right, result)

        return result

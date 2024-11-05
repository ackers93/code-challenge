# This question was asked by Apple.

# Given a binary tree, find a minimum path sum from root to a leaf.

# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_path_sum(root):
    if not root:
        return 0

    def dfs(node, current_sum):
        # Base case: if it's a leaf node, return the path sum
        if not node.left and not node.right:
            return current_sum + node.val
        
        # Initialize left and right path sums with a large value
        left_sum = float('inf')
        right_sum = float('inf')
        
        # Traverse left and right subtrees if they exist
        if node.left:
            left_sum = dfs(node.left, current_sum + node.val)
        if node.right:
            right_sum = dfs(node.right, current_sum + node.val)
        
        # Return the minimum of the left and right path sums
        return min(left_sum, right_sum)

    # Start DFS traversal from the root with an initial sum of 0
    return dfs(root, 0)

# Example usage:
# Construct the tree from the example
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(5)
root.left.right = TreeNode(2)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(-1)

# Call the function and print the minimum path sum
print(min_path_sum(root))  # Output: 15

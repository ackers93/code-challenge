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

# Define the structure for a tree node
class TreeNode
    attr_accessor :val, :left, :right
  
    def initialize(val = 0, left = nil, right = nil)
      @val = val
      @left = left
      @right = right
    end
  end
  
  def min_path_sum(root)
    return 0 if root.nil?
    
    # Helper function to traverse the tree and calculate path sums
    def dfs(node, current_sum)
      # Base case: If it's a leaf node, return the path sum
      return current_sum + node.val if node.left.nil? && node.right.nil?
      
      # Initialize left and right path sums with a large value
      left_sum = Float::INFINITY
      right_sum = Float::INFINITY
      
      # Traverse left and right subtrees if they exist
      left_sum = dfs(node.left, current_sum + node.val) if node.left
      right_sum = dfs(node.right, current_sum + node.val) if node.right
      
      # Return the minimum of the left and right path sums
      [left_sum, right_sum].min
    end
  
    # Start DFS traversal from the root with an initial sum of 0
    dfs(root, 0)
  end
  
  # Example usage:
  # Construct the tree from the example
  root = TreeNode.new(10)
  root.left = TreeNode.new(5)
  root.right = TreeNode.new(5)
  root.left.right = TreeNode.new(2)
  root.right.right = TreeNode.new(1)
  root.right.right.left = TreeNode.new(-1)
  
  # Call the function and print the minimum path sum
  puts min_path_sum(root)  # Output: 15
  

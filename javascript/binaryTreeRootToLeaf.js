// This question was asked by Apple.

// Given a binary tree, find a minimum path sum from root to a leaf.

// For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

//   10
//  /  \
// 5    5
//  \     \
//    2    1
//        /
//      -1

class TreeNode {
    constructor(val = 0, left = null, right = null) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
  }
  
  function minPathSum(root) {
    if (!root) return 0;
  
    function dfs(node, currentSum) {
      // Base case: if it's a leaf node, return the path sum
      if (!node.left && !node.right) {
        return currentSum + node.val;
      }
  
      // Initialize left and right path sums with a large value
      let leftSum = Infinity;
      let rightSum = Infinity;
  
      // Traverse left and right subtrees if they exist
      if (node.left) {
        leftSum = dfs(node.left, currentSum + node.val);
      }
      if (node.right) {
        rightSum = dfs(node.right, currentSum + node.val);
      }
  
      // Return the minimum of the left and right path sums
      return Math.min(leftSum, rightSum);
    }
  
    // Start DFS traversal from the root with an initial sum of 0
    return dfs(root, 0);
  }
  
  // Construct the example tree
  let root = new TreeNode(10);
  root.left = new TreeNode(5);
  root.right = new TreeNode(5);
  root.left.right = new TreeNode(2);
  root.right.right = new TreeNode(1);
  root.right.right.left = new TreeNode(-1);
  
  // Call the function and print the minimum path sum
  console.log(minPathSum(root));  // Output: 15
  
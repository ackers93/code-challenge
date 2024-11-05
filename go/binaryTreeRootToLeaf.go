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

package main

import (
	"fmt"
	"math"
)

// TreeNode represents a node in a binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// minPathSum calculates the minimum path sum from root to a leaf
func minPathSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	// Helper function to perform DFS
	var dfs func(node *TreeNode, currentSum int) int
	dfs = func(node *TreeNode, currentSum int) int {
		// Base case: if it's a leaf node, return the path sum
		if node.Left == nil && node.Right == nil {
			return currentSum + node.Val
		}

		// Initialize left and right path sums with a large value
		leftSum, rightSum := math.MaxInt32, math.MaxInt32

		// Traverse left and right subtrees if they exist
		if node.Left != nil {
			leftSum = dfs(node.Left, currentSum+node.Val)
		}
		if node.Right != nil {
			rightSum = dfs(node.Right, currentSum+node.Val)
		}

		// Return the minimum of the left and right path sums
		return min(leftSum, rightSum)
	}

	// Start DFS traversal from the root with an initial sum of 0
	return dfs(root, 0)
}

// Helper function to find minimum of two integers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Main function to demonstrate the usage
func main() {
	// Construct the example tree
	root := &TreeNode{Val: 10}
	root.Left = &TreeNode{Val: 5}
	root.Right = &TreeNode{Val: 5}
	root.Left.Right = &TreeNode{Val: 2}
	root.Right.Right = &TreeNode{Val: 1}
	root.Right.Right.Left = &TreeNode{Val: -1}

	// Call the function and print the minimum path sum
	fmt.Println(minPathSum(root)) // Output: 15
}

// This problem was asked by Google.

// Given the head of a singly linked list, swap every two nodes and return its head.

// For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

package main

import "fmt"

// ListNode represents a node in the singly linked list
type ListNode struct {
	Val  int
	Next *ListNode
}

// swapPairs swaps every two adjacent nodes and returns the new head of the list
func swapPairs(head *ListNode) *ListNode {
	// Create a dummy node to simplify edge cases
	dummy := &ListNode{Next: head}
	prev := dummy

	for prev.Next != nil && prev.Next.Next != nil {
		// Identify the nodes to be swapped
		first := prev.Next
		second := prev.Next.Next

		// Perform the swap
		first.Next = second.Next
		second.Next = first
		prev.Next = second

		// Move the prev pointer two nodes ahead
		prev = first
	}

	return dummy.Next
}

// printList is a helper function to print the linked list
func printList(head *ListNode) {
	for head != nil {
		fmt.Printf("%d -> ", head.Val)
		head = head.Next
	}
	fmt.Println("nil")
}

func main() {
	// Example usage
	head := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}
	fmt.Println("Original list:")
	printList(head)

	swappedHead := swapPairs(head)
	fmt.Println("Swapped list:")
	printList(swappedHead)
}

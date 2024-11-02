//  Given an array of integers, find if the array contains any duplicates.

//  Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

//  Example 1:

//  Input: [1, 2, 3, 1]
//  Output: true
//  Example 2:

//  Input: [1, 2, 3, 4]
//  Output: false
//  Example 3:

//  Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
//  Output: true

package main

import (
	"fmt"
)

func listDupes(array []int) bool {
	selectedItems := make(map[int]bool)
	for _, num := range array {
		if selectedItems[num] {
			return true
		}
		selectedItems[num] = true
	}
	return false
}

// Test cases
func main() {
	arr1 := []int{1, 2, 3, 1}                   // Expected output: true
	arr2 := []int{1, 2, 3, 4}                   // Expected output: false
	arr3 := []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2} // Expected output: true

	fmt.Println(listDupes(arr1))
	fmt.Println(listDupes(arr2))
	fmt.Println(listDupes(arr3))
}

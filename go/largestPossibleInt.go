// Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
// For example, given [10, 7, 76, 415], you should return 77641510.

package main

import (
	"fmt"
	"sort"
	"strconv"
)

// Custom comparator for sorting
func compare(a, b string) bool {
	return a+b > b+a
}

func largestPossibleInteger(numbers []int) int {
	// Convert numbers to strings for comparison
	strNumbers := make([]string, len(numbers))
	for i, num := range numbers {
		strNumbers[i] = strconv.Itoa(num)
	}

	// Sort numbers based on custom comparator
	sort.Slice(strNumbers, func(i, j int) bool {
		return compare(strNumbers[i], strNumbers[j])
	})

	// Join sorted numbers to form the largest possible integer
	result := ""
	for _, num := range strNumbers {
		result += num
	}

	// Convert the result back to an integer
	largestInt, _ := strconv.Atoi(result)
	return largestInt
}

// Example usage
func main() {
	numbers := []int{10, 7, 76, 415}
	fmt.Println(largestPossibleInteger(numbers)) // Output: 77641510
}

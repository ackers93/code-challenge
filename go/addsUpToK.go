package main

import (
	"fmt"
)

func allPairsThatAddUpToK(array []int, k int) [][]int {
	seenNumbers := make(map[int]bool)
	pairs := [][]int{}

	for _, num := range array {
		complement := k - num
		if seenNumbers[complement] {
			pairs = append(pairs, []int{complement, num})
		}
		seenNumbers[num] = true
	}

	if len(pairs) == 0 {
		return nil
	}
	return pairs
}

func main() {
	arr := []int{10, 15, 3, 7, 7, 10}
	k := 17
	result := allPairsThatAddUpToK(arr, k)

	if result != nil {
		fmt.Printf("Pairs that add up to %d: %v\n", k, result)
	} else {
		fmt.Printf("No pairs add up to %d\n", k)
	}
}

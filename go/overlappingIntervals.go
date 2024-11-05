// This problem was asked by Snapchat.

// Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

// The input list is not necessarily ordered in any way.

// For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

package main

import (
	"fmt"
	"sort"
)

func mergeIntervals(intervals [][2]int) [][2]int {
	// Step 1: Sort intervals by the start time
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	// Step 2: Initialize a slice to store merged intervals
	merged := make([][2]int, 0)

	for _, interval := range intervals {
		// If merged is empty or there is no overlap, add the interval
		if len(merged) == 0 || merged[len(merged)-1][1] < interval[0] {
			merged = append(merged, interval)
		} else {
			// Overlapping intervals, merge them
			merged[len(merged)-1][1] = max(merged[len(merged)-1][1], interval[1])
		}
	}

	return merged
}

// Helper function to find the maximum of two integers
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	intervals := [][2]int{{1, 3}, {5, 8}, {4, 10}, {20, 25}}
	merged := mergeIntervals(intervals)
	fmt.Println(merged)
}

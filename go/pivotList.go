// Given a pivot x, and a list lst, partition the list into three parts.

// The first part contains all elements in lst that are less than x
// The second part contains all elements in lst that are equal to x
// The third part contains all elements in lst that are larger than x
// Ordering within a part can be arbitrary.

// For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]

package main

import (
	"fmt"
)

func partitionList(lst []int, x int) []int {
	var lessThanX, equalToX, greaterThanX []int

	for _, n := range lst {
		if n < x {
			lessThanX = append(lessThanX, n)
		} else if n == x {
			equalToX = append(equalToX, n)
		} else {
			greaterThanX = append(greaterThanX, n)
		}
	}

	return append(append(lessThanX, equalToX...), greaterThanX...)
}

func main() {
	x := 10
	lst := []int{9, 12, 3, 5, 14, 10, 10}
	result := partitionList(lst, x)
	fmt.Println(result) // Output will be [9, 3, 5, 10, 10, 12, 14]
}

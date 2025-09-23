// This problem was asked by Facebook.

// On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

// Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

// For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

//         Arrangement       |   Change
// ----------------------------------------
// ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
// ['B', 'B', 'G', 'B']      | (B, G) -> R
// ['B', 'R', 'B']           | (R, B) -> G
// ['B', 'G']                | (B, G) -> R
// ['R']

package main

import "fmt"

func quxes(quxes []string) int {
	if len(quxes) == 0 {
		return 0
	}

	// Create a copy to avoid mutating input
	current := make([]string, len(quxes))
	copy(current, quxes)

	// Keep transforming while possible
	for len(current) > 1 {
		transformed := false

		// Look for adjacent different colors to transform
		for i := 0; i < len(current)-1; i++ {
			if current[i] != current[i+1] {
				// Get the third color
				a, b := current[i], current[i+1]
				third := getThirdColor(a, b)

				// Replace pair with third color
				current = append(current[:i], append([]string{third}, current[i+2:]...)...)
				transformed = true
				break
			}
		}

		// If no transformations possible, we're done
		if !transformed {
			break
		}
	}

	return len(current)
}

func getThirdColor(a, b string) string {
	colors := map[string]bool{"R": true, "G": true, "B": true}
	delete(colors, a)
	delete(colors, b)
	for c := range colors {
		return c
	}
	return ""
}

func main() {
	fmt.Println(quxes([]string{"R", "G", "B", "G", "B"})) // 1
	// Empty array
	fmt.Println(quxes([]string{})) // 0

	// Single element
	fmt.Println(quxes([]string{"R"})) // 1

	// Mixed parities that reduce to 1
	fmt.Println(quxes([]string{"R", "G"}))      // 1
	fmt.Println(quxes([]string{"R", "G", "B"})) // 1

	// Same parity that reduce to 2
	fmt.Println(quxes([]string{"R", "G", "R", "G"}))           // 2
	fmt.Println(quxes([]string{"R", "R", "G", "G", "B", "B"})) // 2
	fmt.Println(quxes([]string{"R", "G", "B", "R", "G", "B"})) // 2

	// All same color - no transformations possible
	fmt.Println(quxes([]string{"R", "R", "R"}))      // 3
	fmt.Println(quxes([]string{"G", "G", "G", "G"})) // 4

	// Two colors, same parity
	fmt.Println(quxes([]string{"R", "G", "R", "G"})) // 2
	fmt.Println(quxes([]string{"R", "R", "G", "G"})) // 2

	// Two colors, different parity
	fmt.Println(quxes([]string{"R", "G", "R"})) // 1
	fmt.Println(quxes([]string{"R", "G", "G"})) // 1
}

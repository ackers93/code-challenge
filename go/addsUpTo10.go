// Good morning! Here's your coding interview problem for today.

// This problem was asked by Microsoft.

// A number is considered perfect if its digits sum up to exactly 10.

// Given a positive integer n, return the n-th perfect number.

// For example, given 1, you should return 19. Given 2, you should return 28.

package main

import "fmt"

func nthPerfectNumber(n int) int {
	count := 0
	number := 0
	for count < n {
		number += 1
		if sumDigits(number) == 10 {
			count += 1
		}
	}
	return number
}

func sumDigits(number int) int {
	sum := 0
	for number > 0 {
		sum += number % 10
		number /= 10
	}
	return sum
}

func main() {
	fmt.Println(nthPerfectNumber(1))  // 19
	fmt.Println(nthPerfectNumber(2))  // 28
	fmt.Println(nthPerfectNumber(3))  // 37
	fmt.Println(nthPerfectNumber(4))  // 46
	fmt.Println(nthPerfectNumber(5))  // 55
	fmt.Println(nthPerfectNumber(6))  // 64
	fmt.Println(nthPerfectNumber(7))  // 73
	fmt.Println(nthPerfectNumber(8))  // 82
	fmt.Println(nthPerfectNumber(9))  // 91
	fmt.Println(nthPerfectNumber(10)) // 109
}

// Good morning! Here's your coding interview problem for today.

// This problem was asked by Microsoft.

// A number is considered perfect if its digits sum up to exactly 10.

// Given a positive integer n, return the n-th perfect number.

// For example, given 1, you should return 19. Given 2, you should return 28.


function nthPerfectNumber(n) {
  let count = 0;
  let number = 0;
  while (count < n) {
    number += 1;
    if (number.toString().split('').reduce((acc, digit) => acc + parseInt(digit), 0) === 10) {
      count += 1;
    }
  }
  return number;
}

console.log(nthPerfectNumber(1)); // 19
console.log(nthPerfectNumber(2)); // 28
console.log(nthPerfectNumber(3)); // 37
console.log(nthPerfectNumber(4)); // 46
console.log(nthPerfectNumber(5)); // 55
console.log(nthPerfectNumber(6)); // 64
console.log(nthPerfectNumber(7)); // 73
console.log(nthPerfectNumber(8)); // 82
console.log(nthPerfectNumber(9)); // 91
console.log(nthPerfectNumber(10)); // 109
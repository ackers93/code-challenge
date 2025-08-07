// Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
// For example, given [10, 7, 76, 415], you should return 77641510.

function largestPossibleInteger(numbers) {
    // Convert numbers to strings for comparison
    numbers = numbers.map(String);
    
    // Custom comparator for sorting
    numbers.sort((a, b) => (b + a) - (a + b));
    
    // Join sorted numbers to form the largest possible integer
    return parseInt(numbers.join(''), 10);
}

// Example usage
const numbers = [10, 7, 76, 415];
console.log(largestPossibleInteger(numbers));  // Output: 77641510

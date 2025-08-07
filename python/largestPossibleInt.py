# Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
# For example, given [10, 7, 76, 415], you should return 77641510.

from functools import cmp_to_key

def largest_possible_integer(numbers):
    # Convert numbers to strings for comparison
    numbers = list(map(str, numbers))
    
    # Custom comparator for sorting
    def compare(a, b):
        return (b + a > a + b) - (b + a < a + b)
    
    # Sort numbers based on custom comparator
    numbers.sort(key=cmp_to_key(compare))
    
    # Join sorted numbers to form the largest possible integer
    return int(''.join(numbers))

# Example usage
numbers = [10, 7, 76, 415]
print(largest_possible_integer(numbers))  # Output: 77641510

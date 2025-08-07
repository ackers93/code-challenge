# Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
# For example, given [10, 7, 76, 415], you should return 77641510.

def largest_possible_integer(numbers)
  # Convert numbers to strings for comparison
  numbers.map!(&:to_s)
  
  # Sort numbers based on custom comparator
  numbers.sort! do |a, b|
    (b + a) <=> (a + b)
  end
  
  # Join sorted numbers to form the largest possible integer
  numbers.join.to_i
end

# Example usage
numbers = [10, 7, 76, 415]
puts largest_possible_integer(numbers)  # Output: 77641510
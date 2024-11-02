# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

require 'set'

def all_pairs_that_add_up_to_k(array, k)
  seen_numbers = Set.new
  pairs = []

  array.each do |num|
    complement = k - num
    if seen_numbers.include?(complement)
      pairs << [complement, num]
    end
    seen_numbers.add(num)
  end

  pairs.empty? ? nil : pairs
end

# Test the function
#test1
# arr = [10, 15, 3, 7, 7, 10]
# knumber = 17
#test2
arr = [10, 15, 3, 7, 6, 10, 4, 7]
knumber = 14
result = all_pairs_that_add_up_to_k(arr, knumber)
if result
  puts "Pairs that add up to #{knumber}: #{result}"
else
  puts "No pairs add up to #{knumber}"
end


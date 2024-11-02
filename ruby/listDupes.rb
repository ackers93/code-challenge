# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1, 2, 3, 1]
# Output: true
# Example 2:

# Input: [1, 2, 3, 4]
# Output: false
# Example 3:

# Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true

def listDupes(arr)
  selected_items = []
  
  arr.each do |item|
    if selected_items.include?(item)
      return true
    else
      selected_items << item
    end
  end

  false
end

# Test cases
arr1 = [1, 2, 3, 1] # Expected output: true
arr2 = [1, 2, 3, 4] # Expected output: false
arr3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] # Expected output: true

puts listDupes(arr1)
puts listDupes(arr2)
puts listDupes(arr3)
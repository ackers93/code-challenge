# Given a pivot x, and a list lst, partition the list into three parts.

# The first part contains all elements in lst that are less than x
# The second part contains all elements in lst that are equal to x
# The third part contains all elements in lst that are larger than x
# Ordering within a part can be arbitrary.

# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]

def partition_list(lst, x)
    less_than_x, greater_or_equal_to_x = lst.partition { |n| n < x }
    equal_to_x, greater_than_x = greater_or_equal_to_x.partition { |n| n == x }
  
    less_than_x + equal_to_x + greater_than_x
  end
  
  x = 10
  lst = [9, 12, 3, 5, 14, 10, 10]
  result = partition_list(lst, x)
  puts result.inspect  # Output will be [9, 3, 5, 10, 10, 12, 14]
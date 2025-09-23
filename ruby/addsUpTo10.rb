# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.
# 
#
def nth_perfect_number(n)
  count = 0
  number = 0
  while count < n
    number += 1
    if number.to_s.chars.map(&:to_i).sum == 10
      count += 1
    end
  end
  number
end

puts nth_perfect_number(1) # 19
puts nth_perfect_number(2) # 28
puts nth_perfect_number(3) # 37
puts nth_perfect_number(4) # 46
puts nth_perfect_number(5) # 55
puts nth_perfect_number(6) # 64
puts nth_perfect_number(7) # 73
puts nth_perfect_number(8) # 82
puts nth_perfect_number(9) # 91
puts nth_perfect_number(10) # 109
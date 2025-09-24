# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.
# 
#

def nth_perfect_number(n):
    count = 0
    number = 0
    while count < n:
        number += 1
        if sum(int(digit) for digit in str(number)) == 10:
            count += 1
    return number

print(nth_perfect_number(1)) # 19
print(nth_perfect_number(2)) # 28
print(nth_perfect_number(3)) # 37
print(nth_perfect_number(4)) # 46
print(nth_perfect_number(5)) # 55
print(nth_perfect_number(6)) # 64
print(nth_perfect_number(7)) # 73
print(nth_perfect_number(8)) # 82
print(nth_perfect_number(9)) # 91
print(nth_perfect_number(10)) # 109
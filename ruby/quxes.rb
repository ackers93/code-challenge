# This problem was asked by Facebook.

# On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

# Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

#         Arrangement       |   Change
# ----------------------------------------
# ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
# ['B', 'B', 'G', 'B']      | (B, G) -> R
# ['B', 'R', 'B']           | (R, B) -> G
# ['B', 'G']                | (B, G) -> R
# ['R']                     |

def quxes(quxes)
  while quxes.length > 1
    quxes = quxes.each_cons(2).map do |a, b|
      if a == b
        a
      else
        quxes.delete(a)
        quxes.delete(b)
        quxes.push(a == 'R' ? 'G' : 'R')
      end
    end
  end
  quxes.length
end

puts quxes(['R', 'G', 'B', 'G', 'B']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B', 'R']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B', 'R', 'G']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B', 'R']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B', 'R', 'G']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B']) # 1
puts quxes(['R', 'G', 'B', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B', 'R', 'G', 'B', 'R']) # 1
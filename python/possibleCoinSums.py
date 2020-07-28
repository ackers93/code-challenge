# def recurse(coins, quantity, s, running_total):
#     # when there are no more coins left
#     if quantity == [0 for _ in range(len(coins))]:
#         return
#     # loop through coins
#     for i, coin in enumerate(coins):
#         # if there is a positive quantity of that coin, take it
#         if quantity[i] > 0:
#             quantity[i] -= 1
#             running_total += coin
#             print(running_total)
#             s.add(running_total)
#             recurse(coins, quantity, s, running_total)


# def possibleSums(coins, quantity):
# sums = set()

# for i, coin in enumerate(coins):
#     for q in range(quantity[i]):
#         sums.add(sum([[coins.pop(i)] - [coin] + coins[i] * q]))

# return len(sums)

# unique_sums = set()
# recurse(coins, quantity, unique_sums, 0)

# return len(unique_sums)

# # figure out all of the possible sums
# # loop through the coins list
# for i, coin in enumerate(coins):
#     # check if the current coin still has
#     # any quantity left
#     if quantity[i] > 0:
#         # if it does, add that to a running sum
#         # remove one quantity of that coin from
#         # the quantity list
#         running_total += coin
#         quantity[i] -= 1
#         # check if the resulting sum is in the
#         # set of unique sums
#         unique_sums.add(running_total)

# # return the length of the set
# return len(unique_sums)

# from itertools import combinations

# def possibleSums(coins, quantity):
#     all_coins = sum(quantity)
#     indices = ""

#     for i, num in enumerate(quantity):
#         indices += str(i) * num

#     uniques = set()

#     for r in range(1, all_coins + 1):
#         coms = combinations(indices, r)

#         for com in coms:
#             total = 0

#             for val in com:
#                 total += coins[int(val)]

#             uniques.add(total)

#     return len(uniques)

def possibleSums(coins, quantity):
    unique_sums = {0}

    for coin, quant in zip(coins, quantity):
        new = {}

        for i in range(1, quant+1):
            for sum in unique_sums:
                tmp = sum + i * c

                if tmp not in sums:
                    new[tmp] = tmp

        sums.update(new)

    return len(sums) - 1

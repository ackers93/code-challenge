def all_pairs_that_add_up_to_k(array, k):
    seen_numbers = set()
    pairs = []

    for num in array:
        complement = k - num
        if complement in seen_numbers:
            pairs.append((complement, num))
        seen_numbers.add(num)

    return pairs if pairs else None

# Test the function
#test1
# arr = [10, 15, 3, 7, 7, 10]
# knumber = 17
#test2
arr = [10, 15, 3, 7, 6, 10, 4, 7]
knumber = 14
result = all_pairs_that_add_up_to_k(arr, knumber)
if result:
    print(f"Pairs that add up to {knumber}: {result}")
else:
    print(f"No pairs add up to {knumber}")

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#     ["ate", "eat", "tea"],
#     ["nat", "tan"],
#     ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creates a result dictionary for storing results
        result = {}
    # loop over the passed in string
        for word in strs:
            # for each item in strs, create a sorted version and             #assign to sorted_word
            sorted_word = "".join(sorted(word))
        # checks if the sorted word is in the results array
            if sorted_word in result:
                # if it is, it appends it to the results array and the index of the sroted word
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]
        return list(result.values())

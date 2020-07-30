# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# first_not_repeating_character(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# first_not_repeating_character(s) = '_'.

# There are no characters in this string that do not repeat.

# [execution time limit] 4 seconds(py3)

# [input] string s

# A string that contains only lowercase English letters.

# [output] char

# The first non-repeating character in s of '_' if there are no characters that do not repeat.


def first_not_repeating_character(s):
    # Create a dict to store each character
    char_dict = {}
    unique_chars = set()
    unique_indexes = set()

    # loop over and count occurence of each character
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    # for characters with an occurence of 1
    for key in char_dict:
        if char_dict[key] == 1:
            # if theres only one occurence, it's added to the unique_char
            unique_chars.add(key)
    # if nothing is unique, return our edge case of '_'
    if len(unique_chars) == 0:
        return '_'

    for index, char in enumerate(s):
        if char in unique_chars:
            unique_indexes.add(index)
    # order dictionary by index so we can grab the first one added
    sorted_by_index = sorted(unique_indexes)
    # result is set to the first index, thus the first added to the
    # unique_index, which is what we want.
    result = s[sorted_by_index[0]]

    return result

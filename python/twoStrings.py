def twoStrings(s1, s2):

    # function expects return output in the form of a string "YES" or "NO"
​
   # What's a common substring? Any character that is present in both strings.
    # How can we find characters that are present in both strings?
​
    # Iterate through both strings and compare them to each other
        # How exactly would we perform this iteration?
       # Iterating through both strings in unison
       # Would this be guaranteed to find a common substring?

   # Runtime: O(n + m) ~ O(2n)
   # Space: O(n)
​
   # s = set() # O(1)
​
   # Using a single set, store all of the characters from one of the
    # strings in the set
   # for char in s1:  # O(n)
   #     s.add(char)  # O(1)

    # then iterate through the other string, checking each character
    # to see if the set contains the current character
   # for char in s2:  # O(m)
   #     if char in s:  # O(1)
   #         return "YES"
​
   # return "NO"
​
   # Runtime: O(n * m) ~ O(n^2)
    # Space: O(1) since we aren't using any extra data structures
   # for char in s1:  # O(n)
   #     if char in s2:  # O(m)
   #         return "YES"

   # return "NO"
​
    # if one of the sets contains an element in the other set
   if len(set(s1) & set(s2)) > 0:
        return "YES"

    return "NO"

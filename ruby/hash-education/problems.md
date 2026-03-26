# Hash Study Problems

A collection of problems to solve using Ruby hashes, ranging from simple to advanced.

## Beginner Problems

### Problem 1: Basic Hash Creation
Create a hash that stores the names and ages of 5 people. Write a method that returns the name of the oldest person.

### Problem 2: Counting Characters
Given a string, create a hash that counts the frequency of each character. For example, "hello" should return `{ 'h' => 1, 'e' => 1, 'l' => 2, 'o' => 1 }`.

### Problem 3: Key Existence Check
Write a method that takes a hash and an array of keys. Return a new hash containing only the key-value pairs where the key exists in the given array.

### Problem 4: Value Swapping
Write a method that swaps keys and values in a hash. If there are duplicate values, handle them appropriately (e.g., convert to arrays).

### Problem 5: Hash Merging
Create two hashes with some overlapping keys. Write a method that merges them, with values from the second hash taking precedence.

### Problem 6: Filter by Value
Write a method that filters a hash to only include entries where the value is greater than a given threshold.

### Problem 7: Group by Value
Given an array of hashes, group them by a specific key's value. For example, group people by their age.

### Problem 8: Flatten Nested Hash
Write a method that flattens a nested hash, converting keys like `{ a: { b: 1 } }` to `{ 'a.b' => 1 }`.

## Intermediate Problems

### Problem 9: Word Frequency Counter
Given a paragraph of text, create a hash that counts the frequency of each word (case-insensitive, ignore punctuation).

### Problem 10: Hash Deep Merge
Write a method that performs a deep merge of two nested hashes, combining nested structures recursively.

### Problem 11: Invert Hash with Arrays
Given a hash where values are arrays, create a new hash where each array element becomes a key pointing to the original key. Handle duplicates appropriately.

### Problem 12: Hash Difference
Write a method that returns the difference between two hashes - keys that exist in the first but not the second, and vice versa.

### Problem 13: Sort by Value
Write a method that sorts a hash by its values (ascending or descending) and returns an array of `[key, value]` pairs.

### Problem 14: Hash Transformation
Write a method that transforms all values in a hash using a block, but preserves the original hash structure.

### Problem 15: Nested Hash Access
Create a method that safely accesses nested hash values using dot notation (e.g., `hash['user.profile.name']`), returning `nil` if any key doesn't exist.

### Problem 16: Hash to Array of Hashes
Given a hash like `{ a: [1, 2], b: [3, 4] }`, convert it to an array of hashes: `[{ a: 1, b: 3 }, { a: 2, b: 4 }]`.

### Problem 17: Remove Empty Values
Write a method that removes all keys from a hash where the value is `nil`, empty string, empty array, or empty hash.

### Problem 18: Hash Intersection
Write a method that finds the intersection of two hashes - keys that exist in both with the same values.

## Advanced Problems

### Problem 19: LRU Cache Implementation
Implement a Least Recently Used (LRU) cache using a hash. It should have `get(key)` and `put(key, value)` methods with O(1) time complexity.

### Problem 20: Anagram Groups
Given an array of strings, group them into anagrams. Return a hash where keys are sorted characters and values are arrays of anagram words.

### Problem 21: Hash Path Traversal
Write a method that can set and get values in a nested hash using a path array (e.g., `[:user, :profile, :name]`). Handle creation of intermediate hashes.

### Problem 22: Frequency Analysis
Given a hash of word frequencies, find the top N most frequent words, handling ties appropriately.

### Problem 23: Hash Diff with Deep Comparison
Write a method that compares two nested hashes and returns a hash showing what changed: added keys, removed keys, and modified values (with old and new values).

### Problem 24: Hash Serialization
Write methods to serialize a hash (including nested hashes and arrays) to a string format and deserialize it back. Handle edge cases like symbols, numbers, booleans, and nil.

### Problem 25: Two Sum with Hash
Given an array of integers and a target sum, use a hash to find two numbers that add up to the target in O(n) time.

### Problem 26: Hash-based Graph Representation
Implement a graph using a hash (adjacency list). Include methods to add vertices, add edges, find neighbors, and check if two vertices are connected.

### Problem 27: Substring with Unique Characters
Given a string, find the longest substring with all unique characters. Use a hash to track character positions for O(n) solution.

### Problem 28: Hash-based Trie
Implement a Trie (prefix tree) data structure using nested hashes. Include insert, search, and prefix search methods.

## Expert Problems

### Problem 29: Hash-based Database Index
Design a simple in-memory database index using hashes. Support multiple indexes on different fields, range queries, and efficient updates.

### Problem 30: Consistent Hashing
Implement a consistent hashing algorithm for distributed systems. Use a hash to map keys to nodes in a ring structure.

### Problem 31: Hash-based Bloom Filter
Implement a Bloom Filter using hash functions. Use multiple hash functions to set bits in a bit array for probabilistic membership testing.

### Problem 32: Hash-based Rate Limiter
Implement a rate limiter that tracks requests per user/IP using a hash. Support sliding window or token bucket algorithms.

### Problem 33: Hash-based Session Store
Create a session store using hashes that supports expiration, serialization, and thread-safe operations.

### Problem 34: Hash-based Memoization Framework
Build a memoization framework that caches function results using hashes. Support cache expiration, size limits, and cache statistics.

### Problem 35: Hash-based Event System
Implement an event emitter/subscriber system using hashes to track event listeners. Support event namespaces, wildcards, and priority ordering.

### Problem 36: Hash-based Configuration Manager
Create a configuration manager that loads settings from multiple sources (files, environment variables) into a hash. Support nested keys, type coercion, validation, and hot-reloading.

## Tips for Solving

1. **Start Simple**: Begin with basic hash operations and build up complexity
2. **Test Edge Cases**: Consider empty hashes, nil values, duplicate keys/values
3. **Performance**: Think about time and space complexity
4. **Use HashStudy**: You can extend the `HashStudy` class or use it as a reference
5. **Write Tests**: Create test cases for each problem you solve
6. **Documentation**: Comment your solutions explaining your approach

## How to Use

1. Pick a problem that matches your skill level
2. Implement a solution (you can add methods to `HashStudy` or create new classes)
3. Write tests for your solution
4. Run `ruby hash_study_test.rb` or your test file
5. Move on to the next problem!

Good luck! 🚀

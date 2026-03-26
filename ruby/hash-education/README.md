# Hash Education

A simple Ruby setup for studying hash operations.

## Files

- `hash_study.rb` - The main class with hash methods
- `hash_study_test.rb` - Test suite using Test::Unit (Ruby's built-in testing framework)
- `problems.md` - A collection of hash problems to solve, ranging from beginner to expert level

## Running Tests

```bash
ruby hash_study_test.rb
```

## Class Methods

The `HashStudy` class provides methods for common hash operations:

- `add(key, value)` - Add a key-value pair
- `get(key)` - Get a value by key
- `has_key?(key)` - Check if key exists
- `has_value?(value)` - Check if value exists
- `remove(key)` - Remove a key-value pair
- `keys` - Get all keys
- `values` - Get all values
- `size` - Get hash size
- `empty?` - Check if hash is empty
- `merge(other_hash)` - Merge another hash (non-destructive)
- `merge!(other_hash)` - Merge another hash (destructive)
- `clear` - Clear all entries
- `each(&block)` - Iterate over pairs
- `transform_values(&block)` - Transform values
- `select(&block)` - Select pairs based on condition
- `reject(&block)` - Reject pairs based on condition

## Adding Your Own Tests

Add new test methods to `hash_study_test.rb` following the pattern:

```ruby
def test_your_test_name
  # Your test code here
  assert_equal(expected, actual)
end
```

## Adding Your Own Methods

Add new methods to `hash_study.rb` and then write tests for them!

## Practice Problems

Check out `problems.md` for a curated list of hash-related problems to solve, from simple exercises to complex algorithms. Perfect for practicing and improving your hash manipulation skills!

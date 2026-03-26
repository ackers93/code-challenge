class HashStudy
  attr_reader :data

  def initialize(initial_data = {})
    @data = initial_data.dup
  end

  # Add a key-value pair to the hash
  def add(key, value)
    @data[key] = value
  end

  # Get a value by key
  def get(key)
    @data[key]
  end

  # Check if a key exists
  def has_key?(key)
    @data.key?(key)
  end

  # Check if a value exists
  def has_value?(value)
    @data.value?(value)
  end

  # Remove a key-value pair
  def remove(key)
    @data.delete(key)
  end

  # Get all keys
  def keys
    @data.keys
  end

  # Get all values
  def values
    @data.values
  end

  # Get the size of the hash
  def size
    @data.size
  end

  # Check if hash is empty
  def empty?
    @data.empty?
  end

  # Merge another hash into this one
  def merge(other_hash)
    @data.merge(other_hash)
  end

  # Merge another hash into this one (destructive)
  def merge!(other_hash)
    @data.merge!(other_hash)
  end

  # Clear all entries
  def clear
    @data.clear
  end

  # Iterate over each key-value pair
  def each(&block)
    @data.each(&block)
  end

  # Transform values (returns new hash)
  def transform_values(&block)
    @data.transform_values(&block)
  end

  # Select key-value pairs based on condition
  def select(&block)
    @data.select(&block)
  end

  # Reject key-value pairs based on condition
  def reject(&block)
    @data.reject(&block)
  end

  ### Problem 1: Basic Hash Creation 
  #Create a hash that stores the names and ages of 5 people. Write a method that returns the name of the oldest person.
  def return_eldest_person()
    oldest_person = @data.max_by { |_, age| age }
    oldest_person ? oldest_person.first : nil
  end
end


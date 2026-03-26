require 'test/unit'
require_relative 'hash_study'

class HashStudyTest < Test::Unit::TestCase
  def setup
    @hash_study = HashStudy.new
  end

  def test_initialization_with_empty_hash
    assert_equal({}, @hash_study.data)
  end

  def test_initialization_with_data
    initial_data = { name: 'Alice', age: 30 }
    hash_study = HashStudy.new(initial_data)
    assert_equal(initial_data, hash_study.data)
  end

  def test_add_and_get
    @hash_study.add(:name, 'Bob')
    assert_equal('Bob', @hash_study.get(:name))
  end

  def test_has_key
    @hash_study.add(:city, 'New York')
    assert_equal(true, @hash_study.has_key?(:city))
    assert_equal(false, @hash_study.has_key?(:country))
  end

  def test_has_value
    @hash_study.add(:color, 'blue')
    assert_equal(true, @hash_study.has_value?('blue'))
    assert_equal(false, @hash_study.has_value?('red'))
  end

  def test_remove
    @hash_study.add(:temp, 'value')
    assert_equal(true, @hash_study.has_key?(:temp))
    @hash_study.remove(:temp)
    assert_equal(false, @hash_study.has_key?(:temp))
  end

  def test_keys
    @hash_study.add(:a, 1)
    @hash_study.add(:b, 2)
    @hash_study.add(:c, 3)
    assert_equal([:a, :b, :c], @hash_study.keys.sort)
  end

  def test_values
    @hash_study.add(:x, 'first')
    @hash_study.add(:y, 'second')
    assert_equal(['first', 'second'], @hash_study.values.sort)
  end

  def test_size
    assert_equal(0, @hash_study.size)
    @hash_study.add(:one, 1)
    assert_equal(1, @hash_study.size)
    @hash_study.add(:two, 2)
    assert_equal(2, @hash_study.size)
  end

  def test_empty
    assert_equal(true, @hash_study.empty?)
    @hash_study.add(:something, 'value')
    assert_equal(false, @hash_study.empty?)
  end

  def test_merge
    @hash_study.add(:a, 1)
    other = { b: 2, c: 3 }
    merged = @hash_study.merge(other)
    assert_equal({ a: 1, b: 2, c: 3 }, merged)
    # Original should not be modified
    assert_equal({ a: 1 }, @hash_study.data)
  end

  def test_merge_bang
    @hash_study.add(:a, 1)
    other = { b: 2, c: 3 }
    @hash_study.merge!(other)
    assert_equal({ a: 1, b: 2, c: 3 }, @hash_study.data)
  end

  def test_clear
    @hash_study.add(:a, 1)
    @hash_study.add(:b, 2)
    assert_equal(false, @hash_study.empty?)
    @hash_study.clear
    assert_equal(true, @hash_study.empty?)
  end

  def test_each
    @hash_study.add(:first, 1)
    @hash_study.add(:second, 2)
    result = []
    @hash_study.each { |k, v| result << [k, v] }
    assert_equal(2, result.length)
  end

  def test_transform_values
    @hash_study.add(:a, 1)
    @hash_study.add(:b, 2)
    transformed = @hash_study.transform_values { |v| v * 2 }
    assert_equal({ a: 2, b: 4 }, transformed)
    # Original should not be modified
    assert_equal({ a: 1, b: 2 }, @hash_study.data)
  end

  def test_select
    @hash_study.add(:a, 1)
    @hash_study.add(:b, 2)
    @hash_study.add(:c, 3)
    selected = @hash_study.select { |k, v| v > 1 }
    assert_equal({ b: 2, c: 3 }, selected)
  end

  def test_reject
    @hash_study.add(:a, 1)
    @hash_study.add(:b, 2)
    @hash_study.add(:c, 3)
    rejected = @hash_study.reject { |k, v| v > 1 }
    assert_equal({ a: 1 }, rejected)
  end

  # TODO: Add your own tests here!
  # Example:
  # def test_your_custom_method
  #   # Your test code here
  # end
end

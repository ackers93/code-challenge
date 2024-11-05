# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

arr = "[(1, 3), (5, 8), (4, 10), (20, 25)]"

def overlappingIntervals(array)
	# Convert to Ruby format
	intervals = array.scan(/\((\d+),\s*(\d+)\)/).map { |start, end_| [start.to_i, end_.to_i] }
	# Step 1: Sort intervals by their starting points
	sorted_intervals = intervals.sort_by { |interval| interval[0] }
	# Step 2: Initialize the result with the first interval
	merged = [sorted_intervals[0]]

	sorted_intervals[1..].each do |current_start, current_end|
		# puts "CURS #{current_start} CURE #{current_end}"
    # Get the last interval in the merged list
    last_start, last_end = merged[-1]


    # If there is an overlap, merge intervals
    if current_start <= last_end
      # Update the end of the last interval to the max end
      merged[-1] = [last_start, [last_end, current_end].max]
    else
      # No overlap, so add the current interval to merged
      merged << [current_start, current_end]
    end
  end
  return merged
end

print overlappingIntervals(arr)
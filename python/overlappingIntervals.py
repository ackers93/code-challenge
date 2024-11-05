# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

arr = [(1, 3), (5, 8), (4, 10), (20, 25)]

def overlappingIntervals(intervals):
    # Step 1: Sort intervals based on the starting point
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the list to store merged intervals
    merged = []
    
    for interval in intervals:
        # If merged list is empty or there is no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # When the intervals overlap, merge them
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    
    return merged

print(overlappingIntervals(arr))
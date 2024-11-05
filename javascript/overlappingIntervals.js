// This problem was asked by Snapchat.

// Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

// The input list is not necessarily ordered in any way.

// For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].


function mergeIntervals(intervals) {
    // Step 1: Sort intervals by the start time
    intervals.sort((a, b) => a[0] - b[0]);

    // Step 2: Initialize an array to store merged intervals
    const merged = [];

    for (let interval of intervals) {
        // If merged is empty or there is no overlap, add the interval
        if (merged.length === 0 || merged[merged.length - 1][1] < interval[0]) {
            merged.push(interval);
        } else {
            // Overlapping intervals, merge them
            merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
        }
    }

    return merged;
}

// Example usage
const intervals = [[1, 3], [5, 8], [4, 10], [20, 25]];
console.log(mergeIntervals(intervals));

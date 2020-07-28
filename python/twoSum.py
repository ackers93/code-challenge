# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     pair = {}
    #     #can check to see if the number is less than the target
    #     for idx, num in enumerate(nums):
    #         if num < target:
    #     #subtract the number from target
    #             diff = target - num
    #     #find difference in list
    #             if diff in nums:
    #                 pair[idx] = num
    #     #return both indices of complementary pair
    #     return pair.keys()

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        # can check to see if the number is less than the target
        for idx, num in enumerate(nums):
            if target-num in pair and idx != pair[target-num]:
                return [idx, pair[target-num]]
            else:
                pair[num] = idx

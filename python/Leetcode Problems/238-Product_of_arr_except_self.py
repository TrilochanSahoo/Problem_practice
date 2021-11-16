# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        if 0 in nums:
            for i in range(len(nums)):
                temp = nums[:i]+nums[i+1:]
                if 0 in temp:
                    res.append(0)
                else:
                    res.append(math.prod(temp))
        else:
            total_prod=math.prod(nums)
            for i in range(len(nums)):
                temp = total_prod//nums[i]
                res.append(temp)
        return res
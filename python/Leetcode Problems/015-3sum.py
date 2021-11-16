# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 

# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums)<3):
            return []
        nums.sort()
        print(nums)
        l = []
        for i in range(len(nums)-1):
            num_map ={}
            for j in range(i+1,len(nums)):
                num = nums[j]
                if(0-(nums[i]+num)) in num_map:
                    if [nums[i],(0-(nums[i]+num)),num] in l:
                        continue
                    l.append([nums[i],(0-(nums[i]+num)),num])
                    # print(nums[i],(0-(nums[i]+num)),num)
                num_map[num]=j
        return l
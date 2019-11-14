# 2sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# e.g, nums = [2, 7, 11, 15], target = 9, then return [0, 1] (ASC)

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

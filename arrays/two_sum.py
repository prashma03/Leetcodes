#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums): 
          diff = target - num 
          if diff in hashmap:
            return [hashmap[diff], i] 
          hashmap[num] = i

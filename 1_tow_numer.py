#-*- coding: utf-8 -*-
#时间复杂度O(n^2)
class Solution(object):
   def twoSum(self, nums, target):
       """
       :type nums: List[int]
       :type target: int
       :rtype: List[int]
       """
       for i in range(len(nums)):
           for j in range(i+1, len(nums)):
               if nums[i] + nums[j] == target:
                   return [i, j]
solu = Solution()
a = [4,2,4]
b = 8
print(solu.twoSum(a, b))

#时间复杂度 O(n)
class Solution(object):
   def twoSum(self, nums, target):
       """
       :type nums: List[int]
       :type target: int
       :rtype: List[int]
       """
       maps = {}
       for i,j in enumerate(nums):
           if target - j in maps:
               return [i, maps[target - j]]
           maps[j] = i

solution = Solution()
a = [3, 2, 4]
print(solution.twoSum(a, 6))
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle
            else:
                left = middle + 1
        return left + 1 if target > nums[left] else left

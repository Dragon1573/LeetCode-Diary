from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            if target == nums[index]:
                return index
            elif target < nums[index]:
                right = index - 1
            else:
                left = index + 1
        return -1

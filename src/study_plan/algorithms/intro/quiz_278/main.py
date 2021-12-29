from .provided import isBadVersion


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            middle = left + (right - left) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
        return left

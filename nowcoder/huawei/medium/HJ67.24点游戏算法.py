""" HJ67 - 24点游戏算法

https://www.nowcoder.com/practice/fbc417f314f745b1978fc751a54ac8cb

题解：Python3 @CoodeBoy
"""
from sys import stdin
from typing import List

def func(nums: List[int], tar: int):
    if len(nums) == 1:
        return nums[0] == tar
    # 注意各种计算顺序都要考虑
    flag = False
    for i in range(len(nums)):
        nums = nums[1:] + [nums[0]]
        flag = flag or func(nums[1:], tar + nums[0])
        flag = flag or func(nums[1:], tar - nums[0])
        flag = flag or func(nums[1:], tar * nums[0])
        flag = flag or func(nums[1:], tar / nums[0])
    return flag

for line in stdin:
    nums = [int(_) for _ in line.split()]
    print(str(func(nums, 24)).lower())

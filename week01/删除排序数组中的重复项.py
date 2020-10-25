"""
coding: utf8
@time: 2020/10/25 20:31
@author: cjr
@file: 删除排序数组中的重复项.py
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 0
        nums[j] = nums[0]
        j += 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1
        return len(nums[0:j])

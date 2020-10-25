"""
coding: utf8
@time: 2020/10/25 22:42
@author: cjr
@file: 接雨水.py
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left <= right:
            # 小的最大值决定能装多少雨水
            if left_max < right_max:
                ans += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                ans += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return ans


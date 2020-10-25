"""
coding: utf8
@time: 2020/10/25 21:05
@author: cjr
@file: 旋转数组.py
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = (nums[len(nums)-k:] + nums[:len(nums)-k])


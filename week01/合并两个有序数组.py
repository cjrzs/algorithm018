"""
coding: utf8
@time: 2020/10/25 22:34
@author: cjr
@file: 合并两个有序数组.py
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从末尾获取两个指针,并为合并后的新的num1数组设置指针
        p1 = m-1
        p2 = n-1
        p = m+n-1
        # 当两个指针都大于等于0时候进行比较
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]


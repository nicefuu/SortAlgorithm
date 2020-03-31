#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 21:25
# @Author  : Fhh
# @File    : CountingSort.py
# Good good study,day day up!

class CountingSort:
    def counting_sort(self, nums):  # 0<=nums[i]<=10000
        counts = [0 for _ in range(10001)]
        for i in nums:
            counts[i] += 1
        res = []
        for i in range(len(nums)):
            res += [i] * counts[i]
        return res


s = CountingSort()
print(s.counting_sort(nums=[7,5,4,3,7,5,5,7,8,8,9,9]))
"""
1095. 山脉数组中查找目标值
（这是一个 交互式问题 ）
给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。
如果不存在这样的下标 index，就请返回 -1。
何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：
首先，A.length >= 3
其次，在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 
你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：
MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度
注意：对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

"""
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = left, right = 0, mountain_arr.length() - 1
        maxh = 0
        while left < right:
            if mountain_arr.get(left) == target:
                return left
            mid = int((left + right) / 2)
            mid_v = mountain_arr.get(mid)
            if left < mid < right:
                mid_1v = mountain_arr.get(mid - 1)
                mid_v1 = mountain_arr.get(mid + 1)
                if mid_v > mid_1v and mid_v > mid_v1:
                    # 最高点
                    maxh = mid
                    break
                elif mid_1v < mid_v < mid_v1:
                    if mid_1v == target:
                        return mid - 1
                    if mid_v1 == target:
                        return mid + 1
                    left = mid
                elif mid_1v > mid_v > mid_v1:
                    right = mid
                else:
                    left += 1
            else:
                break
        print(maxh)
        if maxh == 0:
            return -1
        else:
            l, r = 0, maxh
            while l < r:
                if mountain_arr.get(l) == target:
                    return l
                if mountain_arr.get(r) == target:
                    return r
                mid = int((l + r) / 2)
                mid_v = mountain_arr.get(mid)
                if l < mid < r:
                    if mid_v == target:
                        return mid
                    if mid_v > target:
                        r = mid
                    elif mid_v < target:
                        l = mid
                else:
                    break
            l, r = maxh, mountain_arr.length() - 1
            while l < r:
                if mountain_arr.get(l) == target:
                    return l
                if mountain_arr.get(r) == target:
                    return r
                mid = int((l + r) / 2)
                mid_v = mountain_arr.get(mid)
                if l < mid < r:
                    if mid_v == target:
                        return mid
                    if mid_v > target:
                        l = mid
                    elif mid_v < target:
                        r = mid
                else:
                    break
            return -1
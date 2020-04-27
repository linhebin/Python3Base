"""
33. 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

"""


class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[mid] < target:
                # 当target大于中值时，当且仅当target大于左值、且左值大于中值时，则仅可能位于左半侧
                if nums[mid] < nums[left] < target:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] > target:
                # 当target小于中值时，当且仅当target小于左值、且左值小于中值时，则仅可能位于右半侧
                if nums[mid] > nums[left] > target:
                    left = mid + 1
                else:
                    right = mid

        return -1


if __name__ == "__main__":
    S = Solution()
    print(S.search([4,5,6,7,0,1,2], 7))
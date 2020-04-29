"""
15. 三数之和
你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        ls = []
        for i in range(n-2):
            print(i)
            for j in range(i+1, n-1):
                print(i, j)
                for k in range(j+1, n):
                    print(i, j, k)
                    if nums[i] + nums[j] + nums[k] == 0:
                        new_ls = sorted([nums[i], nums[j], nums[k]])
                        print(new_ls)
                        if new_ls not in ls:
                            ls.append(new_ls)
        return ls

if __name__ == "__main__":
    S = Solution()
    print(S.threeSum([0,0,0]))
"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) > 0:
            first = strs[0]
            if len(strs) == 1:
                return first
            for i in range(len(first), 0, -1):
                flag = False
                for j, str in enumerate(strs):
                    if len(str) < i or str[0:i] != first[0:i]:
                        flag = False
                        break
                    else:
                        flag = True
                if flag:
                    return first[0:i]
        return ""


if __name__ == "__main__":
    S = Solution()
    print(S.longestCommonPrefix(["c", "c"]))



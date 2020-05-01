"""
202. 快乐数

编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        li = []
        while n > 1:
            m = str(n)
            sum = 0
            for _, v in enumerate(m):
                sum += int(v)*int(v)
            if sum == 1:
                return True
            if sum in li:
                return False
            else:
                li.append(sum)
            n = sum
        return True


if __name__ == "__main__":
    S = Solution()
    print(S.isHappy(20))
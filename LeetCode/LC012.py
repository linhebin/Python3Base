"""
12. 整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        # N = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        # n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        if num not in range(1, 4000):
            return ""
        ls = []
        while num > 0:
            if num in range(1000, 4000):
                ls.append("M")
                num -= 1000
            elif num in range(900, 1000):
                ls.append("CM")
                num -= 900
            elif num in range(500, 900):
                ls.append("D")
                num -= 500
            elif num in range(400, 500):
                ls.append("CD")
                num -= 400
            elif num in range(100, 400):
                ls.append("C")
                num -= 100
            elif num in range(90, 100):
                ls.append("XC")
                num -= 90
            elif num in range(50, 90):
                ls.append("L")
                num -= 50
            elif num in range(40, 50):
                ls.append("XL")
                num -= 40
            elif num in range(10, 40):
                ls.append("X")
                num -= 10
            elif num in range(9, 10):
                ls.append("IX")
                num -= 9
            elif num in range(5, 9):
                ls.append("V")
                num -= 5
            elif num in range(4, 5):
                ls.append("IV")
                num -= 4
            elif num in range(1, 4):
                ls.append("I")
                num -= 1
        return "".join(ls)


if __name__ == "__main__":
    S = Solution()
    print(S.intToRoman(3994))
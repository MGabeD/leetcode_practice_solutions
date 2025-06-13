class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        cur = ""
        rem = columnNumber
        while rem > 0:
            if rem % 26 ==0:
                cur = "Z" + cur
                rem = rem // 26 -1
                continue
            else:
                cur = chr(ord('A') + rem % 26 - 1) + cur
            rem = rem // 26
        return cur

# sol = Solution()
# sol.convertToTitle(26)
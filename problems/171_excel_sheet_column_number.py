class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        cur = 0
        for i in columnTitle:
            cur *= 26
            pres = ord(i) - ord('A') + 1
            cur += pres
        return cur

sol = Solution()
print(sol.titleToNumber("ZY"))
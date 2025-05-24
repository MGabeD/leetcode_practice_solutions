class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left = 0
        right = x
        while right-left > 1:
            mid = (left + right) / 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid
        return (left + right) // 2

sol = Solution()
print(sol.mySqrt(4))
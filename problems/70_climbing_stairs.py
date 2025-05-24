class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        data = [0]*n
        data[0] = 1
        data[1] = 2
        for i in range(2,n):
            data[i] = data[i-1] + data[i-2]
        return data[-1]

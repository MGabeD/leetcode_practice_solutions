class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # def track(cur):
        #     if cur >= len(s):
        #         return 0
        #     if s[cur] == "0":
        #         return -1
        #     if cur < len(s)-1:
        #         if s[cur] == "1":
        #             return 1 + track(cur+1) + track(cur+2)
        #         elif s[cur] == "2" and int(s[cur+1]) < 7:
        #             return 1 + track(cur+1) + track(cur+2)
        #         else:
        #             return track(cur+1)
        #     else:
        #         return 0
        #
        # if s[0] == "0":
        #     return 0
        # return track(0) + 1
#         This was too slow
        if s[0] == "0":
            return 0
        n = len(s)
        one_back, two_back = 1,1
        for i in range(1, n):
            cur = 0
            if s[i] != "0":
                cur =one_back
            two_digit = int(s[i-1:i+1])
            if two_digit >= 10 and two_digit <= 26:
                cur+= two_back
            two_back = one_back
            one_back = cur
        return one_back

sol = Solution()
print(sol.numDecodings("123"))
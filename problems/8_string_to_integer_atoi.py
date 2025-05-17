class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # first = True
        # invert = False
        # cur = 0
        # for i in range(0, len(s)):
        #     if s[i].isdigit():
        #         first = False
        #         if cur > tmp or cur == tmp and int(s[i]) >= 7+invert:
        #             if invert:
        #                 return -2**31
        #             else:
        #                 return tmp*10 + 7
        #         cur = cur*10 + int(s[i])
        #     elif first:
        #         if s[i] == " ":
        #             continue
        #         if s[i] == "-":
        #             invert = True
        #             first = False
        #         elif s[i] == "+":
        #             first =False
        #         else:
        #             break
        #     else:
        #         break
        # return cur if not invert else -1*cur
#         works but can be ~faster~ even though same space by eliminating a bunch of the stupid ifs
        i = 0
        len_s = len(s)
        while i < len_s and s[i] == " ":
            i += 1
        if len_s == i:
            return 0
        factor = 1
        cur = 0
        if s[i].isdigit():
            cur = int(s[i])
        elif s[i] == "-":
            factor = -1
        elif s[i] != "+":
            return 0
        i += 1
        mx = 2 ** 31
        while i < len_s and s[i].isdigit():
            cur = cur * 10 + int(s[i])
            if cur >= mx:
                return 2 ** 31 - 1 if factor == 1 else -2 ** 31
            i += 1
        return cur * factor

#     I hate that this is getting so picky that assigning len -> a val actually makes the difference between fastest and
# not
sol = Solution()
print(sol.myAtoi("1337c0d3"))



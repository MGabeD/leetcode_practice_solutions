class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # if a == "0":
        #     return b
        # if b == "0":
        #     return a
        #
        # cur = []
        # i = 0
        # carry = 0
        # upper = max(len(a), len(b))
        # while upper > i:
        #     if i < len(a):
        #         if a[-(i+1)] == "1":
        #             carry +=1
        #     if i < len(b):
        #         if b[-(i+1)] == "1":
        #             carry +=1
        #     cur.append(str(carry%2))
        #     carry //= 2
        #     i += 1
        # if carry != 0:
        #     cur.append(str(carry))
        # return "".join(cur[::-1])

#     disgusting that python is so slow this is faster...
        res = ""
        if len(a) > len(b):
            if b == "0":
                return a
            n = len(a)
            b = "0" * (len(a) - len(b)) + b
        else:
            if a == "0":
                return b
            n = len(b)
            a = "0" * (len(b) - len(a)) + a
        cur = 0
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                cur += 1
            if b[i] == '1':
                cur += 1
            if cur % 2 == 0:
                res = "0" + res
            else:
                res = "1" + res
            cur //= 2
        if cur == 1:
            res = "1" + res
        return res
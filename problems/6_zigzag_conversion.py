# this is my problem for today 5/5

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if len(s) < numRows or numRows==1:
        #     return s
        # arrs = []
        #
        # for i in range(0,numRows):
        #     arrs.append(s[i])
        # pattern_size = (numRows-1)*2
        # for i in range(numRows, len(s)):
        #     tmp = i % pattern_size
        #     if tmp < numRows:
        #         arrs[tmp] += s[i]
        #     else:
        #         arrs[pattern_size-tmp] += s[i]
        # output= ""
        # for i in arrs:
        #     output += ''.join(i)
        #
        # return output
#         This works but there is an easier way o do this - by adding a bunch of extra filtering I am doing extra work
#         I am in the same big O but slow compared to optimal
        if numRows == 1 or len(s) <= numRows:
            return s
        arrs = [''] * numRows
        cur = 0
        pattern_size = (numRows-1)*2
        for i in range(0, len(s)):
            if i % pattern_size < numRows-1:
                arrs[cur] += s[i]
                cur += 1
            else:
                arrs[cur] += s[i]
                cur -= 1
        return ''.join(arrs)

    # 90% beat good enough for now


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))






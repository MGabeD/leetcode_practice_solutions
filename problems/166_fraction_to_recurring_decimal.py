class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if (numerator >= 0 and denominator >= 0) or (numerator <0 and denominator <0) or numerator == 0:
            cur = ""
        else:
            cur = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        carry = (numerator % denominator) * 10
        cur += str(numerator // denominator)
        if carry == 0:
            return cur
        cur += "."
        prev_positions = dict()
        while True:
            if carry in prev_positions:
                return cur[:prev_positions[carry]] + "(" + cur[prev_positions[carry]:] + ")"
            prev_positions[carry] = len(cur)
            cur += str(carry // denominator)
            carry = (carry % denominator) *10
            if carry == 0:
                return cur

# sol = Solution()
# sol.fractionToDecimal(4, 333)
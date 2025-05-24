class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # quotient = 0
        # invert = False
        # if (dividend > 0 and divisor < 0) or (divisor > 0 and dividend <0):
        #     invert = True
        # dividend = abs(dividend)
        # divisor = abs(divisor)
        # while dividend-divisor >= 0:
        #     dividend -= divisor
        #     quotient +=1 if not invert else -1
        #
        # if quotient > 2**31-1:
        #     return 2**31-1
        # if quotient < -2**31:
        #     return -2**31
        # return quotient
        # Two slow - runs at O(N) where n is dividend / divisor -> we can be faster if we hit multiples
        # quotient = 0
        # invert = False
        # if (dividend > 0 and divisor < 0) or (divisor > 0 and dividend <0):
        #     invert = True
        # dividend = abs(dividend)
        # divisor = abs(divisor)
        # for power in reversed(range(32)):
        #     if (dividend >> power) >= divisor:
        #         quotient += 1 << power
        #         dividend -= divisor << power
        #
        # if quotient > 2 ** 31 - 1:
        #     return 2**31-1
        # if quotient < -2**31:
        #     return -2**31
        # return -quotient if invert else quotient
#         I Have the slowest accepted variation. lets speed it up
#         quotient can only be outside the abs of maxes if the input is a max and it is abs 1
#         since both are already pre-gated in the conditions at the bottom I only need to check if divs = -1 && min
#         int_min = -2**31
#         if int_min == dividend and divisor == -1:
#             return 2**31-1
#         quotient = 0
#         invert = (dividend < 0 ) != (divisor <0)
#         dividend = abs(dividend)
#         divisor = abs(divisor)
#         for power in reversed(range(32)):
#             if (dividend >> power) >= divisor:
#                 quotient += 1 << power
#                 dividend -= divisor << power
#
#         return -quotient if invert else quotient
        # There must be a faster way to do the loop part..... this onbly made me 1 ms faster
        int_min = -2**31
        if int_min == dividend and divisor == -1:
            return 2**31-1
        quotient = 0
        invert = (dividend < 0 ) != (divisor <0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            tmp = divisor
            multi = 1
            while dividend >= (tmp <<1):
                tmp <<=1
                multi <<= 1
            dividend -= tmp
            quotient += multi

        return -quotient if invert else quotient
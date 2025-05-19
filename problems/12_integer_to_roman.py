class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = "M" * (num // 1000)
        num = num % 1000
        maximal_sets = [(100,"C", "D", "M"), (10, "X","L","C"), (1,"I","V","X")]
        for [number_to_mod, one, five, ten] in maximal_sets:
            v = num // number_to_mod
            if v == 9:
                res += one + ten
            elif v == 4:
                res += one + five
            elif v >= 5:
                res += five + v%5 * one
            else:
                res += v * one
            num = num % number_to_mod
        return res

# BAHAHAH 100% 1 shot - I am getting better at these
sol = Solution()
print(sol.intToRoman(3749))
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
# not efficient but really fast to write
        x = s.split()
        return len(x[-1])
    # can also go back until you see first non space char then count length till you see space again will be faster
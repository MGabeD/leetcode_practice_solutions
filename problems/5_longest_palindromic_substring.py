
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""
        elif len(s) == 1:
            return s

        bottom = 0
        top = 0
        mx= len(s)-1
        for i in range(1, len(s)):
            odd = True
            even = (s[i-1] == s[i])
            for j in range(i, len(s)):
                if even:
                    if i-1-(j-i) < 0 or s[i-1-(j-i)] != s[j]:
                        if top - bottom < j-1 - (i-1-(j-i-1)):
                            top = j-1
                            bottom = i-1-(j-1-i)
                        even=False
                        if not odd:
                            break
                if odd:
                    if i-(j-i) < 0 or s[i-(j-i)] != s[j]:
                        if top - bottom < j-1 - (i-(j-i-1)):
                            top = j-1
                            bottom = i-(j-i-1)
                        odd = False
                        if not even:
                            break
            if even:
                if mx - (i-1-(mx-i)) > top-bottom:
                    top = mx
                    bottom = i - 1 - (mx - i)
            if odd:
                if mx - (i-(mx-i)) >top-bottom:
                    top = mx
                    bottom = i - (mx - i)
        return s[bottom:top+1]

# the other methods are same time frame just minldy more efficient not really feeling doing the over optimizaiton today

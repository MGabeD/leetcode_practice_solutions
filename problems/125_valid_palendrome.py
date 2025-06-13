class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = 0
        back = len(s)-1

        while True:
            while front < len(s) and not s[front].isalnum():
                front += 1
            while back >= 0 and not s[back].isalnum():
                back -= 1
            if back < front:
                return True
            if s[front].lower() != s[back].lower():
                return False
            else:
                front += 1
                back -= 1

sol = Solution()
sol.isPalindrome("A man, a plan, a canal: Panama")
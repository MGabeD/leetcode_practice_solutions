class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        data = {
            "[":"]",
            "{":"}",
            "(":")"
        }
        stack = []
        for i in s:
            if i in data:
                stack.append(i)
            elif len(stack) == 0 or i != data[stack.pop()]:
                return False
        return len(stack) == 0

# Beats 100
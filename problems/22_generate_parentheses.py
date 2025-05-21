class Solution(object):
    def generateParenthesis(self, n):
        """
        :type ctr: int
        :rtype: List[str]
        """
        def recurse(cur, open, close):
            if open == n:
                return [cur + ")"*(open-close)]
            if open > close:
                return recurse(cur+"(", open+1, close) + recurse(cur+")", open, close+1)
            else:
                return recurse(cur+"(", open+1, close)

        return recurse("", 0,0)

sol = Solution()
print(sol.generateParenthesis(4))

# beat 100% so yippee
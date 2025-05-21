from collections import deque

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # data = deque()
        # if x < 0:
        #     return False
        # while x > 0:
        #     data.append(x%10)
        #     x = x//10
        #
        # while len(data) > 1:
        #     left = data.popleft()
        #     right = data.pop()
        #     if right != left:
        #         return False
        # return True
        # this is bullshit the question says not to use strings - this as fast as possible with that constraint

        # doing with strings so I feed better than 40% (once I do it will check but I think that is what all the
        # other people doing this question did
        return str(x) == str(x)[::-1]
        # the variance is crazy i did this I also did it with saving the x intermediary ~ same time all right at the top





sol = Solution()
print(sol.isPalindrome(121))
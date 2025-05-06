# problem for 5/6
from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # This is very clearly dynamic programming question
        # I am thinking to cut down with a like greedy get as close as possible then go up and try to solve for diff
        # sub problems.

        # maybe its smarter to count up cause then I can check optimal sub problem for each step
        # if amount == 0:
        #     return 0
        # coins.sort()
        #
        # save = {}
        # alive_heads = deque()
        #
        # for i in coins:
        #     save[i] = 1
        #
        #     alive_heads.append((i,1))
        #
        # amount_found = -1
        # while alive_heads:
        #     cur = alive_heads.popleft()
        #     for i in coins:
        #         cur_ptr = cur[0] + i
        #         try:
        #             foo = cur[1] + 1 < save[cur_ptr]
        #         except:
        #             foo = False
        #         foo1 = save.get(cur_ptr, None) is None
        #         if cur_ptr <= amount and (save.get(cur_ptr, None) is None or cur[1] + 1 < save[cur_ptr]):
        #             if amount_found < 0 or amount_found > cur[1]+1:
        #                 alive_heads.append((cur_ptr, cur[1]+1))
        #             save[cur_ptr] = cur[1]+1
        #             if cur_ptr == amount:
        #                 amount_found = cur_ptr
        # return save.get(amount, -1)
#     This works but I can be smarter

        # a stack makes this a depth frist approach. still nt much faster though so lets try somehting different

        max_val = amount // min(coins) +1
        dp = [0]+[max_val]*amount

        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i-c] +1)
        return dp[amount] if dp[amount] != max_val else -1

#         better logic here since you don't need heads - don;'t need to do extra traversals.






# print(Solution().coinChange([3,7,405,436], 8839))
print(Solution().coinChange([1,2,5], 11))

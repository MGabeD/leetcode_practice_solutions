class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        biggest_after = [0] * len(prices)
        cur_max = prices[len(prices) - 1]
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > cur_max:
                cur_max = prices[i]
            biggest_after[i] = cur_max
        active_min = prices[0]
        cur_max_delta = 0
        compete_with_target = 0
        for i in range(0, len(prices)):
            if prices[i] - active_min > cur_max_delta:
                cur_max_delta = prices[i] - active_min
            elif prices[i] < active_min:
                active_min = prices[i]
            if cur_max_delta + biggest_after[i] - prices[i] > compete_with_target:
                compete_with_target = cur_max_delta + biggest_after[i] - prices[i]

        return compete_with_target
# wow -  i literally 1 shotted 99.15 % beat on first attempt... I am happy with myself! this should also not be a
# leetcode hard - was too easy

sol = Solution()
print(sol.maxProfit([3,3,5,0,0,3,1,4]))
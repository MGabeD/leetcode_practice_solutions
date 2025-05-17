# this is only being done because the random button gave it to me - will do two today
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def dfs(val, cur_xor):
        #     if val == len(nums):
        #         return cur_xor
        #
        #     return dfs(val +1, cur_xor ^ nums[val]) + dfs(val +1, cur_xor)
        # return dfs(0,0)

        # I MISSED IT UNLUCKY
        a = 0
        for i in nums:
            a |= i

        return a*(2**(len(nums)-1))



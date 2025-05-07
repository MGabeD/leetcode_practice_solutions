# backfill for 5/3
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        ctr = 0
        for s in stones:
            if s in jewels:
                ctr += 1
        return ctr
#     Obviously tis is faster if you make jewels a set (assuming it is large) but considering the bounds of leetcode
# I think doing this is a waste of time as long as I know hashmap/dict lookup is 0(1) while char in str is O(n) where n
# is length of str. However, there is an overhead of compute time for making a hashmap so not necessarily worth it. In
# amore complicated question it would be smart ot make this a set.

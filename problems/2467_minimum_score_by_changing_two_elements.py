# Backfill question for 4/20
from collections import deque


# Wow i only have 6 more backfill to go! then I can start predoing for this upcoming weekend if I need....
class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # I am kind of confused where this one gets being a medium from. it seems pretty aparent to me that you want to
        # take the smallest 2 values and the two largest values. Whichever has the largest diff you replace both with
        # some value in the middle then return
        # Oh i see it we have massive space for optimizations.... - getting something working is easy lets do that first
        if len(nums) <= 3:
            return 0

        # While having a lot of code to write for a hardcoded biggest and smallest 3 dumb for actual code I think it is
        # the fastest for this use case
        min_3, max_3 = find_top3_min3(nums=nums)
        # Now we need to find the deltas and find the best case
        return min(max_3[2] - min_3[0],max_3[0] - min_3[2],max_3[1] - min_3[1])


def find_top3_min3(nums):
    min1 = min2 = min3 = float('inf')
    max1 = max2 = max3 = float('-inf')

    for num in nums:
        if num < min1:
            min3, min2, min1 = min2, min1, num
        elif num < min2:
            min3, min2 = min2, num
        elif num < min3:
            min3 = num

        if num > max1:
            max3, max2, max1 = max2, max1, num
        elif num > max2:
            max3, max2 = max2, num
        elif num > max3:
            max3 = num

    return (min1, min2, min3), (max1, max2, max3)


# HAHHAHAHAHAHAH i beat 100% on first attempt. My idea to build take a second step by step for optimizations from my
# last problem before this really seems like a good call. I should start doing this for every problem.
class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # if k == 1 and len(nums) <=1:
        #     return -1

        # I MISSED AN EDGE CASE FOR THE FIRST TIME SINCE I STARTED DOING THESE DAILY (the one below... I got the harder
        # one though) I need to be better about thinking about this... super easy one to get if I just took a sec to
        # think
        # if k == 1:
        #     return nums[1]

        # quick refactor of it to be prettier
        # if k==1:
        #     if len(nums) <=1:
        #         return -1
        #     return nums[1]

        # looking on that change I realize I need some more checking before i try to submit again - i think there are
        # more edge cases

        if k == 0:
            return nums[0]

        if len(nums) < 2:
            if k%2 == 1:
                return -1
            return nums[0]
        if k == 1:
            return nums[1]

        # This was good to think back on - I caught another edge case I had missed... went too hard on solving and
        # not reflecting on the edge cases...
        if k > len(nums):
            return max(nums)
        elif k == len(nums):
            return max(nums[0:k-1])
        else:
            # possible_top_values = max(nums[0:k-1])
            # possible_if_all_removed = nums[k]
            # if possible_top_values > possible_if_all_removed:
            #     return possible_top_values
            # else:
            #     return possible_if_all_removed
            return max(max(nums[0:k-1]),nums[k])
            # Optimization once I passed all the tests - cutting all the saving of values and if else made this 2x
            # faster on the test set leet code gave. There is a bit more optimization like this that can be done
            # but we are down to beating 94% of people's solutions on speed so i am going to take one quick shot at it
            # but in reality it is prob not worth the time


    def maximumTopFaster(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # since I am literally chasing 1-2 ms the order of these actually really matters
        # K-> 0 first drops an if call after a len() on one of the edge cases but adds a conditional to check
        # for 0 for all cases where len(nums) < 2 both of these are unlikely os I don't think it matters,
        if k == 0:
            return nums[0]
        # technically this might be faster but should be literally unmeasurable by even ns ... only would matter for
        # 10^9+ actions... still going to have it for fun though
        if len(nums) == 1:
            if k%2 != 0: # cmp x, 0 faster than cmp x, 1
                return -1
            return nums[0]
        # this one needs to go after since it is being protected by

        if k > len(nums):
            # this is more likely so should go first
            return max(nums)
        if k == len(nums):
            return max(nums[0:k-1])
        # above cases more common can guard this - gets called less in the process flow
        if k == 1:
            return nums[1]
        return max(max(nums[0:k-1]),nums[k])

# SUCCESS 1 ms faster for too much implementation work =)

# What i did well => identified the problem well and optimally took on the major cases and flow of the program

# What i need to do better on in the future - for some reason today I did not think about edge cases and because of that
# I missed 2 of them before i event decided to check (I submitted a failure 1x) which was lazy and dumb. I need to do
# better on validating edges before I submit. Even if it is an easy problem think about the cases so @myself you don't
# stupid submissions - this could ruin an interview you could rock

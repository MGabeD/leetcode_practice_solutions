# The shuffle gave me an easy I willprob do two tdoay
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) <= 2:
        #     return 0
        # ctr_top = 1
        # ctr_bottom = 1
        # min_val = nums[0]
        # max_val = nums[0]
        #
        # for i in nums[1:]:
        #     if min_val > i:
        #         ctr_bottom = 1
        #         min_val = i
        #     elif min_val == i:
        #         ctr_bottom +=1
        #     if max_val < i:
        #         ctr_top = 1
        #         max_val = i
        #     elif max_val == i:
        #         ctr_top +=1
        # return min(len(nums) - ctr_top - ctr_bottom, 0)

    # I am doing enough work here to get throught his at 1 pass that I don;t think it is actually faster
    # I can literally get the exact same thing by just doing min & max and counting when true
        min_val = min(nums)
        max_val = max(nums)
        ctr = 0
        for i in nums:
            if max_val > i > min_val:
                ctr +=1

        return ctr

    # this one was super easy - having the commented out version makes it look like I don't think that or I struggled -
    # but I am leaving it more as a thought that I was thinking I could go faster than juyst in builts was trying to
    # beat 3n * if ten increment and did n * 4ifs *1.5 increments - just not faster
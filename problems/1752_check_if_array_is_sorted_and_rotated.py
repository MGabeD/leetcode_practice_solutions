

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possible_rotation = nums[0] >= nums[len(nums)-1]
        prev = nums[0]
        for i in nums:
            if possible_rotation:
                if prev > i:
                    possible_rotation = False
                    if i > nums[0]:
                        return False

                prev = i
            else:
                if prev > i:
                    return False
                prev = i
        return True

# this one is very easy...
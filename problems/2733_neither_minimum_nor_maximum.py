# This one is the fill in for 4/17

class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        max_val = max(nums[0],nums[1])
        min_val = min(nums[0],nums[1])
        for i in range(2,len(nums)):
            if min_val < nums[i] < max_val:
                return nums[i]
            elif min_val == max_val:
                if min_val > nums[i]:
                    min_val = nums[i]
                elif max_val < nums[i]:
                    max_val = nums[i]
                continue
            elif max_val < nums[i]:
                return max_val
            else:
                return min_val

# no point in improving. First run worked and beat 98%. Can speed it up a little since I am doing an extra comparison with
# lines 11 & 12 but no point in wasting the time I see the speed up.
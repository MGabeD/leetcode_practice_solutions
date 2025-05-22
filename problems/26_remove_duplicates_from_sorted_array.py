class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[idx]:
                nums[idx+1] = nums[i]
                idx += 1
        return idx +1

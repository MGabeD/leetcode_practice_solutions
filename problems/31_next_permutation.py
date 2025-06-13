class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # this problem goes like this
        # 1,2,3,4,5 -> 1,2,3,5,4 -> 1,2,4,3,5 -> 1,2,4,5,3 -> 1,3,2,4,5 -> 1,3,2,5,4 -> 1,3,4,2,5 -> 1,3,4,5,2 ...
        # idx = len(nums)-1
        # while idx > 0:
        #     if nums[idx] < nums[idx-1]:
        #         idx -= 1
        #         break
        #     idx -= 1
        # if idx == 0:
        #     front = 0
        #     back = len(nums)-1
        #     nums[front], nums[back] = nums[back], nums[front]
        #     front += 1
        #     back -= 1
        #     return
        #
        # cur = nums[idx]
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

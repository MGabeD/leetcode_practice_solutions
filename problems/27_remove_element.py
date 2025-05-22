class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx +=1
        return idx

sol = Solution()
tmp = [3,2,2,3]
print(sol.removeElement(tmp,3))
print(tmp)
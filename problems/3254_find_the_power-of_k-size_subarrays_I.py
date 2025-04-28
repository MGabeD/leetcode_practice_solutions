
# problem for 4/28/2025
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ctr = 0
        lst = nums[0]
        for i in range(1, k):
            if nums[i] != lst +1:
                ctr = k-1
            else:
                ctr -= 1
            lst = nums[i]

        res_data = []
        if ctr <= 0:
            res_data.append(nums[k-1])
        else:
            res_data.append(-1)

        for i in range(k, len(nums)):
            if nums[i] != lst +1:
                ctr = k

            ctr -= 1
            if ctr <= 0:
                res_data.append(nums[i])
            else:
                res_data.append(-1)
            lst = nums[i]
        return res_data

a = Solution()
nums = [1,2,3,4,3,2,5]
nums1 = [3,2,3,2,3,2]
print(a.resultsArray(nums, 3))
print(a.resultsArray(nums1, 2))
nums2 = [1,1,33,34]
print(a.resultsArray(nums2,2))

# Works well submitted and beating 92% there are some MILD optimizations with the amounts of calls I am doing but since
# we're looking at less than 2 ms on a spread of 200 for accepted answers to get to 4 ms I am not going to worry about it
# it feels like cheating to do this but I want to catch up for all the ones I missed in the next day or so before I have
# to go home for some family shit so I am going to use this as a catch up for 4/18
# If i feel up to it I will throw in an extra
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

# I hit the next button and got the same questions just with faster optimization requirements. Since I already did it
# for the first one I just copy pasted
# Feel like cheating but means I did good work ig?
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] > nums[right]:
                if nums[mid] > nums[right]:
                    if target > nums[mid] or target <= nums[right]:
                        left = mid +1
                    else:
                        right = mid -1
                else:
                    if nums[mid] < target:
                        if nums[right] < target:
                            right = mid -1
                        else:
                            left = mid +1
                    else:
                        right = mid - 1
            else:
                if nums[mid] < target:
                    left = mid +1
                else:
                    right = mid - 1
        return -1

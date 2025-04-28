# this is my stand in replacement for 4/16

class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        # This looks like a two loop question with an optimization for hashing for back checking. IE I should be pushing
        # to a set for O(1) recall and validation if I have already made the
        seen = set()
        n = len(nums)

        for i in range(n):
            count = 0
            subarray = []
            for j in range(i, n):
                subarray.append(nums[j])
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                seen.add(tuple(subarray))

        return len(seen)
        # Average speed but is for a catch up question so I don't want to go to hard in on myself here
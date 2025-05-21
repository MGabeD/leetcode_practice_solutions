class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # data = {}
        # for idx, i in enumerate(nums):
        #     if i in data:
        #         data[i].add(idx)
        #     else:
        #         data[i] = {idx}
        # for k in data.keys():
        #     if target-k in data:
        #         if target-k == k and len(data[k]) == 1:
        #             continue
        #         return [data[k].pop(), data[target-k].pop()]
        # return []

        # I am stupid I cna do this in one pass so n instead of 2n... (atleast I didn't submit yet :))
        data ={}
        for i, val in enumerate(nums):
            if target-val in data:
                return [data[target-val], i]
            data[val] = i
        # btw this literally never happens due to constraints in the question but here for fun!
        return []
        # submitted beats 100%


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
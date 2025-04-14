from collections import defaultdict
from operator import index


class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # my first run through will be slow-ish -> sort both arrays find where their values are closest to overlapping
        # take the

        # nums1.sort()
        # data = defaultdict(list)
        # for i in range(0,len(nums2)):
        #     data[nums2[i]].append(i)
        # nums2.sort()
        # top_safe = len(nums2)
        # ret_data = [-1]*len(nums1)
        # idx_to_fill = []
        # for i in range(len(nums1)-1,-1,-1):
        #     added = False
        #     for j in range(top_safe-1, -1, -1):
        #         if nums1[i] > nums2[j]:
        #             ret_data[data[nums2[j]].pop()] = nums1[i]
        #             top_safe = j
        #             added = True
        #             break
        #         else:
        #             idx_to_fill.append(data[nums2[j]].pop())
        #             top_safe = j
        #
        #     if top_safe == 0 and not added:
        #         ret_data[idx_to_fill.pop()] = nums1[i]
        # return ret_data

#         This was too slow so lets try optimizing a little bit
        sort1 = sorted(nums1)
        sort2 = sorted(nums2)

        data = {b: [] for b in sort2}
        idx_to_add = []
        j = 0
        for i in sort1:
            if i > sort2[j]:
                data[sort2[j]].append(i)
                j+=1
            else:
                idx_to_add.append(i)

        return [data[i].pop() if data[i] else idx_to_add.pop() for i in nums2]
#         By doing this greedily I am not having to do a bunch of the iteration from my going backwards approach above
# my time complexity should be NlogN now

# feedback for self for future. THis took me way to long for a medium and I took 3 shots at it to speed up. Maybe I am
# just super off today but I need to be thinking forward further and planning better 40 min for this is way way way to
# slow - feeling kind of distracted though so maybe just a fluke day

sol = Solution()
nums1 = [2,7,11,15]
nums2 = [1,10,4,11]
# nums1 = [0]
# nums2 = [0]
print(nums1)
print(nums2)
print(sol.advantageCount(nums1,nums2 ))

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # going to do the dmb version first just to show I can
        # res_data = set()
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 print(f"cur = {nums[i], nums[j], nums[k]} & {i,j,k}")
                        # cur = frozenset([nums[i],nums[j],nums[k]])
                        # if cur not in res_data:
                        #     res_data.add(cur)
                        #     res.append([nums[i],nums[j],nums[k]])
        # return res
        # took 8 min so maybe not worth doing...

        # intermed = {}
        # inputs = {}
        # for i in range(0, len(nums)):
        #     if nums[i] not in inputs:
        #         inputs[nums[i]] = [i]
        #     elif len(inputs[nums[i]]) < 3:
        #         inputs[nums[i]].append(i)
        #
        #     for j in range(i+1, len(nums)):
        #         cur = nums[i] + nums[j]
        #         if cur not in intermed:
        #             intermed[cur] = set()
        #         if nums[i] < nums[j]:
        #             intermed[cur].add((nums[i],nums[j]))
        #         else:
        #             intermed[cur].add((nums[j],nums[i]))
        #
        # res = set()
        # for k,v in inputs.items():
        #     if -k not in intermed:
        #         continue
        #     for (lower,upper) in intermed[-k]:
        #         escape = False
        #         for i in v:
        #             if escape: break
        #             for j in inputs[lower]:
        #                 if escape: break
        #                 for m in inputs[upper]:
        #                     if i != j and j != m and i != m:
        #                         if k < lower:
        #                             res.add((k,lower,upper))
        #                         elif k > upper:
        #                             res.add((lower,upper,k))
        #                         else:
        #                             res.add((lower, k, upper))
        #                         escape = True
        #                         break
        # return [list(a) for a in res]

        res = []
        data = {}
        # nums.sort()
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        sort_data = sorted(data)
        for i, num in enumerate(sort_data):
            if data[num] > 1:
                if num == 0:
                    if data[num] >= 3:
                        res.append([0, 0, 0])
                elif -2 * num in data:
                    res.append([num, num, -2 * num])
            if num < 0:
                target = -num
                # so my target is -num for 2 values to add to it. I can't go before i because then I double count.
                # I can iterate from i up but that has to be inefficient.. So i need some way to get to my min max range
                # and just search through that for the big ones. I think the bottom of the range can be effectively
                if target - sort_data[-1] < i:
                    left = i + 1
                else:
                    left = bisect.bisect_left(sort_data, (target - sort_data[-1]), i + 1)
                right = bisect.bisect_right(sort_data, (target // 2), left)
                for j in sort_data[left:right]:
                    k = target - j
                    if k in data and k != j:
                        res.append([num, j, k])

        return res


sol = Solution()
print(sol.threeSum([-1,0,1,0]))
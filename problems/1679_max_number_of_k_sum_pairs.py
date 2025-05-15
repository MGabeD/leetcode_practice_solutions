# Todays problem 5/15

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # so this question seems to me to have a nice little trick where since there are only 2 numbers being added
        # together I can just sort then ptr to top ptr to button and be assured to get all the correct options on a full
        # loop through it

        # nums.sort()
        # btm = 0
        # tp = len(nums)-1
        # ctr = 0
        # while tp - btm > 0:
        #     cur = nums[btm] + nums[tp]
        #     if cur == k:
        #         ctr += 1
        #         btm += 1
        #         tp -= 1
        #     elif cur > k:
        #         tp -= 1
        #     else:
        #         btm += 1
        # return ctr

        # cool this works and only took like 2 min, def the right idea. Now lets make it faster => the sort is not
        # needed - I can get the same rough behavior I want with a dict -  chekc how i do it below
        # ctr = 0
        # data = {}
        # for i in nums:
        #     if i in data:
        #         data[i] += 1
        #     else:
        #         data[i] = 1
        #
        # for key in data.keys():
        #     occurances = min(data.get(key,0), data.get(k-key,0))
        #     if occurances > 0:
        #         if k - key == key:
        #             ctr += occurances // 2
        #             # minor optimization will never revisit this from the other side in this exploration so can just
        #             # not track it and be fine
        #             continue
        #         data[key] -= occurances
        #         data[k-key] -= occurances
        #         ctr += occurances
        # return ctr
        # This one beats 94% - i think I can eeek out a little more performance
        # ctr = 0
        # data = {}
        # for i in nums:
        #     if i in data:
        #         data[i] += 1
        #     else:
        #         data[i] = 1
        # while len(data) > 0:
        #     key, value = data.popitem()
        #     if k - key == key:
        #         ctr += value // 2
        #         continue
        #     occurances = min(value, data.get(k - key, 0))
        #     if occurances > 0:
        #         ctr += occurances
        #         del data[k - key]
        # return ctr
#         kind of suprised that doing the del made it the same speed since it is now ~.5 the looping IG the extra req
# of the additional if and len made up for it - I can try only looping once when building data to see if that is faster?
#         it could be and conceptiually would be valid is a few ifs more for no for k in keys / the while
        ctr = 0
        data = {}
        for i in nums:
            # if data.get(k - i, 0) > 0:
            if k-i in data and data[k-i] > 0:
                ctr += 1
                data[k-i] -= 1
            elif i in data:
                data[i] += 1
            else:
                data[i] = 1
        return ctr
#     This beats 98%? the rest must just be variance from their backend - I am even getting rid of get for an
#     optimization

# Self analysis
# I think I did this one really well. i started and instantly grasped the problem built a slow version in less than 5
# min -> saw the next efficiency boost -> built that less than 5 min. Then saw I wasn't the fastest so I ideated, tried
# another approach and got 98%
# n is len(nums) m is len(set(nums))
# 1st) nlogn from the sort
# GETTING A LOT MORE GRANULAR FOR THESE ONES NOT O()
# 2nd) n + 4m
# 3rd) n + 6m/2 (same speed though because of extra system calls in filtering (kind of surprised by this tbh)
# ^ to identify why this was literally the exact same i would need to go through the actual system calls to see what
# popitem is doing & what not
# 4th) 2n



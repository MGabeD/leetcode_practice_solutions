from collections import defaultdict


# The first thing I am seeing with this problem is that it is going to be pretty difficult - but has an elegant pattern
# This pattern is you can approach it greedily from the first index and track for each height what the last active x is
# The problem with this is the massive overhead of recomputing every time it changes - there is going to be a nice way
# to fill this in with assumptions since as you decrement down (as needed) then you will see assumed empty values and
# what not -> thus solving some of that - but this is brutally hard for me to instantly invision so I am not going to
# implement the easy (slow) version first since the core implementation will be the same. Not worth chasing it right now

# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         max_active = 0
#         vals = {}
#         max_square = 0
#         for i in range(0, len(heights)):
#             if heights[i] > max_active:
#                 for j in range(max_active+1, heights[i]+1):
#                     vals[j] = i
#                 max_active = heights[i]
#             elif heights[i] < max_active:
#                 for j in range(heights[i]+1, max_active+1):
#                     print(f"popped max: {(i-vals[j])*j}, new height: {heights[i]}, max_active: {max_active}, index: {i}, cur_height_closing: {j}")
#                     max_square = max((i-vals[j])*j, max_square)
#                 max_active = heights[i]
#         for i in range(1, max_active+1):
#             print((len(heights)-vals[i])*i)
#             max_square = max(max_square, (len(heights)-vals[i])*i)
#         return max_square
#
# sol = Solution()
# print(f"solution : {sol.largestRectangleArea([1,3,2,3,1])}")

# This version works but now its time to find that optimization I was talking about above

# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         max_active = 0
#         vals = {}
#         max_square = 0
#         for i in range(0, len(heights)):
#             if heights[i] > max_active:
#                 vals[heights[i]] = i
#                 max_active = heights[i]
#             elif heights[i] < max_active:
#                 prev_max = i
#                 for j in range(heights[i]+1, max_active+1):
#                     # Leet code is older than python 3.8 apparently ...
#                     val = vals.get(j)
#                     if val is not None:
#                         prev_max = min(prev_max, val)
#                         print(f"popped max: {(i-val)*j}, new height: {heights[i]}, max_active: {max_active}, index: {i}, cur_height_closing: {j}")
#                         max_square = max((i-val)*j, max_square)
#                     # print(f"popped max: {(i-vals[j])*j}, new height: {heights[i]}, max_active: {max_active}, index: {i}, cur_height_closing: {j}")
#                     # max_square = max((i-vals[j])*j, max_square)
#                 max_active = heights[i]
#                 vals[heights[i]] = prev_max
#         for i in range(1, max_active+1):
#             if vals.get(i) is None:
#                 continue
#             print((len(heights)-vals[i])*i)
#             max_square = max(max_square, (len(heights)-vals[i])*i)
#         return max_square
#
#
# sol = Solution()
# print(f"solution : {sol.largestRectangleArea([1,3,2,3,1])}")

# This is quite a bit faster but can still be better, the iteration in the dictionary is tooo slow. I can prob do this
# faster by controlling an array instead and holding a tuple and doing bin search - lets skip the bin search for now
# and do the next iteration with a stack (list) and get that optimization first since it alone is significant


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_active = 0
        vals = []
        max_square = 0
        for i in range(0, len(heights)):
            if heights[i] > max_active:
                vals.append([heights[i], i])
                max_active = heights[i]
            elif heights[i] < max_active:
                prev_max = i
                while vals and vals[len(vals)-1][0] >= heights[i]:
                    height, index = vals.pop()
                    prev_max = min(prev_max, index)
                    max_square = max((i-index)*height, max_square)
                max_active = heights[i]
                vals.append([heights[i], prev_max])
        for height, idx in vals:
            max_square = max(max_square, (len(heights) - idx) * height)
        return max_square


sol = Solution()
print(f"solution : {sol.largestRectangleArea([1,3,2,3,1])}")

# This is pretty quick as I am decrementing down -> this while loop actually might be the fastest way as I have
# none of the extra iterations down - the binary search idea to get the range is actually prob unneccesarry and just
# adding time since the sub problem is solved by the while loop -> each of the ones I am checking need to be checked
# the prev case catches the edge case where I either == or am under, the end loop solves all unclosed ones. Seems to be
# efficient. There could be minor optimizations I am missing with how much I am accessing the vars, some of this is
# unnecessary especially with the max since I can just check the top of the vals -> this is likely smarter and faster
# but since I am in the best O() space I am not sure I want to do these optimizations ~ prob can only extract ab 20% of
# a speed increase 1 extra loop for the == case can be changed and a bunch of var setting and indexing can be removed
# not going to do this since this is for leet code.


# Post submission - the exact optimizations ge tot the fastest answer but this one is beating 99.56% of answers so
# I am feeling good enough with it :)

# My thought process and how I can work on this better / what to emphasize for future similar problems. I saw the base
# problem right of the bat and got the forward iteration and back looking instantly. This was very good. I also saw
# how the optimization would work at the top of this file - this was good as it kept my brain churning over the issue
# while I was implementing this. That was a great path that I should repeat whenever I do these hard problems again
# start by looking for the optimization -> if same base structure then implement the easy one while letting myself churn
# on the harder one and think about how to do. This will speed me up like it did here ~20 min for this problem isn't as
# fast as I want to be but its quick enough I think most interviewers would be happy with it. I was typing way way to
# slow for this one though and have been recently. I think I need to start doing a bit of typing practice (unironically)
# every day since my left ring finger keeps misbehaving and isn't hitting the right keys...
# Outside of typing I should practice explaining my thoughts a bit more since I could've realized the end optimizations
# I didn't want to go back and fix much earlier. This would've been good for me since I would've gotten ab ~30ms faster
# on the test set from leetcode - these optimizations weren't all of them but most of them
# this is really nitpicky though if I do all the ones of this difficulty like this I will be doing great. I just need
# to work on getting a bit quicker for the iterations. I got caught for ~4min when implementing the while loop since I
# forgot about the empty case. This is solveable if I just did while true poped and checked there or changed conditions
# doing two checks on every while is a lot slower than one and I could've just done list[-1]'s height > height[i]
# ^ faster also makes it so I don't need to store both vals in the list. This optimization is so insignificant it isn't
# necessary but I should jump to looking at the edge case sooner. I spent to long to find an empty case, especially
# since I missed the optimization hanging right infront of my eyes. I feel like that is the equivalent to walking into a
# tree while texting while walking. I needed to do both but got pulled into one and lost my awareness/context of what
# else I could be finding

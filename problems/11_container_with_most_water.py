
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # biggest_before = []
        # biggest_after = []
        # walking_up = 0
        # size = len(height)
        # walking_down = 0
        # for i in range(0,size):
        #     if height[i] > walking_up:
        #         biggest_before.append(i)
        #         walking_up = height[i]
        #     if height[size-i-1] > walking_down:
        #         biggest_after.append(size-i-1)
        #         walking_down = height[size-i-1]
        #
        # cur_max = 0
        # for i in biggest_before:
        #     for j in biggest_after:
        #         if j < i:
        #             break
        #         if (j-i) * min(height[i],height[j]) > cur_max:
        #             cur_max = (j-i) * min(height[i],height[j])
        # return cur_max
#         I am over computing  - lets make it faster (this was me speeding to a solution
        # THe thing I just realized is that the side which is lower is always constraining so you can do this in a
        # single pass
        # front = 0
        # back = len(height)-1
        # res = 0
        # while front < back:
        #     res = max(res, min(height[front], height[back]) * (back-front))
        #     if height[front] > height[back]:
        #         back -= 1
        #     else:
        #         front += 1
        #
        # return res
#         Cool we got it right lets be faster - doing max(..., min(...)) is slow 2fn overhead when not necessary
#         front = 0
#         back = len(height)-1
#         res = 0
#         while front < back:
#             if height[front] > height[back]:
#                 cur = height[back] * (back - front)
#                 if res < cur:
#                     res = cur
#                 back -= 1
#             else:
#                 cur = height[front] * (back - front)
#                 if res < cur:
#                     res = cur
#                 front += 1
#         return res
#         This beats 98% but i already know how to do better.. the extra if checks ar unnecessary overhead
        front = 0
        back = len(height) - 1
        res = 0
        while front < back:

            if height[front] > height[back]:
                cur = height[back] * (back - front)
                if res < cur:
                    res = cur
                h2 = height[back]
                while height[back] <= h2 and front < back:
                    back -= 1
            else:
                cur = height[front] * (back - front)
                if res < cur:
                    res = cur
                h1 = height[front]
                while height[front] <= h1 and front < back:
                    front += 1
        return res
#     That one did even better... there is certainnly an early exit I can add a filter for to make up and catch
# the remaining .5 % of ppl but I have beend oing this for 25 min now so I don't want to waste any more time

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
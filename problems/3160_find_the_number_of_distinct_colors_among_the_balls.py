# problem for 5/7 (not backfill)
from collections import defaultdict

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
    #     data = {}
    #     colors = []
    #     balls = defaultdict(lambda: -1)
    #     for [ball, color] in queries:
    #         if balls[ball] == -1:
    #             balls[ball] = color
    #         else:
    #             data[balls[ball]].remove(ball)
    #             if len(data[balls[ball]]) == 0:
    #                 del data[balls[ball]]
    #             balls[ball] = color
    #         data[color] = data.get(color, set())
    #         data[color].add(ball)
    #         colors.append(len(data))
    #     return colors
        # This worked but is near as slow as is possible for this question to pass i think that this is likely from
        # adding an extra set creation, lookup, and len lookup for each pull i am doing a bunch of extra work that isn't
        # necessary - would account for being 142 instead of 80ms - I am keeping extra data I just don't need
        # colors = defaultdict(int)
        # res = []
        # balls = defaultdict(lambda: -1)
        # color_count = 0
        # for [ball, color] in queries:
        #     if balls[ball] == -1:
        #         balls[ball] = color
        #     else:
        #         colors[balls[ball]] -= 1
        #         if colors[balls[ball]] == 0:
        #             del colors[balls[ball]]
        #             color_count -= 1
        #         balls[ball] = color
        #     colors[color] += 1
        #     if colors[color] == 1:
        #         color_count += 1
        #     res.append(color_count)
        # return res
        # Faster but not enough

        # colors = defaultdict(int)
        # res = []
        # balls = {}
        # color_count = 0
        # for [ball, color] in queries:
        #     if ball in balls:
        #         colors[balls[ball]] -= 1
        #         if colors[balls[ball]] == 0:
        #             del colors[balls[ball]]
        #             color_count -= 1
        #     balls[ball] = color
        #
        #     colors[color] += 1
        #     if colors[color] == 1:
        #         color_count += 1
        #     res.append(color_count)
        # return res
        # faster again - maybe will be faster to drop the default dict a failed __get_item__ -> factory is slow - might
        # be the difference here - will be less total calls
        colors = {}
        res = []
        balls = {}
        color_count = 0
        for [ball, color] in queries:
            if ball in balls:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    del colors[balls[ball]]
                    color_count -= 1
            balls[ball] = color
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1
                color_count += 1
            res.append(color_count)
        return res

# self reflection: I managed to catch the right solution right off the bat and didn't get pulled into the trap the prob
# setup with the max vals based on the int. These were clearly going to be memory intensive and I am not even sure if
# the declaration time will account for the hash time when writing into a dict. I think that this was a good assumption
# to jump to and am happy I got it. I also managed to realize whatmy major flaws were in terms of speed. While I did
# not initially get it I did some thinking on the default dicts and jumped fromm beatin 50-60% depending on the run to
# 100% with the uncommented version above. I think that this was a good jump to understand that while they are inbuilt
# if you write good code it still compiles to less instructions and thus will be faster. I should've thought of this
# faster and am dissapointed I relied on it. I was just lazy to use inbuilts. I should do better int he future.

sol = Solution()
print(sol.queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))
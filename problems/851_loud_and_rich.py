# 5/14 question

class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        # only going to do one today cause I want to mkae my other project actually work since I broke ground on it yst


        # precompute set relationships for each person - once done for each set translate it to the quietest with more
        # more_money = {}
        # for more, less in richer:
        #     if less in more_money:
        #         more_money[less].append(more)
        #     else:
        #         more_money[less] = [more]
        #
        # def helper_to_collapse(cur_check):
        #     if isinstance(more_money.get(cur_check, []), int):
        #         return more_money[cur_check]
        #
        #     quietest_above = cur_check
        #     for richer_index in more_money.get(cur_check, []):
        #         if richer_index in more_money:
        #             if isinstance(more_money[richer_index], list):
        #                 tmp = helper_to_collapse(richer_index)
        #             else:
        #                 tmp = more_money[richer_index]
        #         else:
        #             tmp = richer_index
        #         print(f"EVAL {cur_check} currently: tmp from parent = {tmp} with value {quiet[tmp]}, quietest above {quietest_above} with value {quiet[quietest_above]}")
        #         if quiet[tmp] < quiet[quietest_above]:
        #             quietest_above = tmp
        #     more_money[cur_check] = quietest_above
        #     return quietest_above
        #
        # # Generate the correct dict
        # res_data = []
        # for i in range(0, len(quiet)):
        #     res_data.append(helper_to_collapse(i))
        # return res_data
#         Well that works but its slow... how else can i effectively do this? I can do a search instead of trying to do
#  some weird fucking precompute... it adds some needless overhead. I can make it all a bit faster that way prob ~40%
#  but someone beat what I did by a lot more ~70% - lets try the search and validate my assumption maybe i am doing
#  even more calls than I thought - I just realized I made an inefficient dfs kinda...

        # I want to do a depth first search to get minimal requests to requery the shared nodes - will be faster here
        # than bfs
        data = {}
        for more, less in richer:
            if less in data:
                data[less].append(more)
            else:
                data[less] = [more]

        ans = [-1] * len(quiet)

        def helper_dfs(node):
            if ans[node] != -1:
                return ans[node]
            cur = node
            for check_idx in data.get(node,[]):
                tmp = helper_dfs(check_idx)
                if quiet[tmp] < quiet[cur]:
                    cur = tmp
            ans[node] = cur
            return cur

        for i in range(0, len(quiet)):
            helper_dfs(i)

        return ans

# Welp. I was wrong - turns out just doing dfs was the fastest way to do this. I beat 100% with that try.

sol = Solution()
print(sol.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]))

# looking back I should've spent mroe time ideating on the benefits of diffeent approachs I just jumped into the problem
# without much thought and made an algorithm. This was pretty clearly a dfs / bfs approach question looking back and
# just hcooseing which one is right. I wish I saw that sooner. If you see the random shit I came up with at the top i am
# approaching this solution without realizing I am trying to re-invent the wheel. Leetcode is mostly pattern matching
# and I didn't even try to do any pattern matching this time. i need to do better looking forward. Its easy to see for
# this question... this is the first one in a while where I am real dissapointed in myself for missing it.
# LIKE i literally recreated dfs randomly from an apparation without thinking and didn't optimize for it so it was slow.
# my brain instinctively grabbed it which is good but I didn't take the time to actually think through what I was doing
# SMH
# today's question 5/8
from collections import defaultdict

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        # This question doesn't have a clear answer to me - I am seeing a few different routes. Maybe something greedy
        # which could find the possible combinations of helpful swaps - one thing that is clear is that any (0,1), (1,2)
        # makes a series of swaps which can have (0,2) as a straight away swap

        # I think a good way to start this is to do the following start with finding all the real possible swaps IE
        # distinct combinations to have a,b swapped.
        # With this information I can then make a dict of swaps and loop over my str
        # This results in the compute time of all options of pairs (admittedly inefficient) + n
        # But i think it is a good starting point

        # I changed my mind. I can do this like a graph problem instead. I can just traverse to find beneficial trades
        # Wait since this is an undiected graph I can effectivley just do a unionfind and get all the clusters which
        # share an edge. This could have massive edge cases on compute time. assuming a sparse graph vs dense would
        # want very different algos.... unless I have some dict -> to commpunites. if in the same one union them -> what
        # do i do for memory overhead - what datatype for this... list -> constant reshuffling causes len(list) -> worst
        # case O(n) for ever run. linkL -> up to n for lookup - instant addition but lookup is slow. I don't need lookup
        # unless uioning though... lets build the links before getting deeper

        # parent = {}
        # size = {}
        #
        # def find(x):
        #     if x not in parent:
        #         parent[x] = x
        #         size[x] = 1
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        #
        # def union(x, y):
        #     px, py = find(x), find(y)
        #     if px == py:
        #         return
        #     if size[px] < size[py]:
        #         px, py = py, px
        #     parent[py] = px
        #     size[px] += size[py]
        #
        # for [a,b] in pairs:
        #     union(a,b)
        #
        # groups = defaultdict(set)
        # for x in parent:
        #     groups[find(x)].add(x)
        #
        #
        # data = {}
        # for i in range(0, len(s)):
        #     if s[i] in data:
        #         data[s[i]].add(i)
        #     else:
        #         data[s[i]] = {i}
        # sorted_keys = sorted(data.keys())
        # idx_keys = {sorted_keys[i]: i for i in range(0, len(sorted_keys))}
        #
        # str_list = list(s)
        # for current_location_in_str in range(0, len(s)):
        #     for sorted_idx in range(0, idx_keys[str_list[current_location_in_str]]):
        #         cur = groups[find(current_location_in_str)]
        #         swap = False
        #         for swap_idx in data[sorted_keys[sorted_idx]]:
        #
        #             if swap_idx in cur and swap_idx > current_location_in_str:
        #                 tmp = str_list[swap_idx]
        #                 swap = True
        #                 print(f"before swap: {''.join(str_list)}")
        #                 print(f"cur_list_value: {str_list[current_location_in_str]}, current_location: {current_location_in_str}, "
        #                       f"sorted_idx {sorted_idx}, swap_idx: {swap_idx}, sorted_keys: {sorted_keys}, sorted_key value:{sorted_keys[sorted_idx]} ")
        #                 data[str_list[current_location_in_str]].remove(current_location_in_str)
        #                 data[str_list[current_location_in_str]].add(swap_idx)
        #                 data[sorted_keys[sorted_idx]].remove(swap_idx)
        #                 data[sorted_keys[sorted_idx]].add(current_location_in_str)
        #                 str_list[swap_idx] = str_list[current_location_in_str]
        #                 str_list[current_location_in_str] = tmp
        #                 print(f"after swap: {''.join(str_list)} \n\n")
        #                 break
        #         if swap:
        #             break
        # return "".join(str_list)

#         This is too slow lets try to redesign
        # I think the collapsing into sets is smart. But I think there is prob a way to allocate those indexes for the
        # min value in each of those indexes. Right now I am indexing over each one each time. This can be smarter.
        # since I am working with indepenant sets I can go

        # parent = {}
        # size = {}
        #
        # def find(x):
        #     if x not in parent:
        #         parent[x] = x
        #         size[x] = 1
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        #
        # def union(x, y):
        #     px, py = find(x), find(y)
        #     if px == py:
        #         return
        #     if size[px] < size[py]:
        #         px, py = py, px
        #     parent[py] = px
        #     size[px] += size[py]
        #
        # for [a,b] in pairs:
        #     union(a,b)
        #
        # groups = defaultdict(list)
        # for i in range(len(s)):
        #     groups[find(i)].append(i)
        #
        # str_list= list(s)
        #
        # for group in groups.values():
        #     grouping = [s[i] for i in group]
        #     grouping.sort()
        #     for i in range(0, len(group)):
        #         str_list[group[i]] = grouping[i]
        # return ''.join(str_list)

        #   This can be made faster still somewhere - I am only beating 83%. I feel like how I am unioning and finding
        #    my sets is ~ineffective~ since I hand roled it from what I remember from a few years ago. just an exta call
        #    or two will change this radically - maybe memory overhead of list > then the hash time.

        # ^ was marginally faster but not enough to get to beating 90%
        parent = list(range(len(s)))
        size = [0]*len(s)
        # parent = {}
        # size = {}

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]

        for [a,b] in pairs:
            union(a,b)

        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)

        str_list= list(s)

        for group in groups.values():
            grouping = [s[i] for i in group]
            grouping.sort()
            for i in range(0, len(group)):
                str_list[group[i]] = grouping[i]
        return ''.join(str_list)
# I was struggling t find how to make this faster. I looked at the correct answers so its not really fair to copy them
# and call it my own work - I got stuck at around 89-87% beat depending on the attempt.

sol = Solution()
print(sol.smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))
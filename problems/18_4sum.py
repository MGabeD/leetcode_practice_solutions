class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # clearly massive optimizations are available somewhere
        data = {}
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        keys = sorted(data.keys())
        two_sums = dict()
        for i in range(len(keys)):
            iter1 = i+1 if data[keys[i]] < 2 else i
            for j in range(iter1, len(keys)):
                if keys[i] + keys[j] in two_sums:
                    two_sums[keys[i] + keys[j]].add((keys[i], keys[j]))
                else:
                    two_sums[keys[i] + keys[j]]= {(keys[i], keys[j])}
                    # two_sums[i + j].add((i,j))

        res = set()
        for k,v in two_sums.items():
            if target - k in two_sums:
                for (first, second) in v:
                    for (third, fourth) in two_sums[target-k]:
                        if first != third and second != third and first != fourth and second != fourth:

                            res.add(tuple(sorted([first,second,third,fourth])))
                        else:
                            if first == second:
                                if data[first] -1 < (1 if first == second else 0) + (1 if first == third else 0) + (1 if first == fourth else 0):
                                    continue
                            else:
                                if data[first]-1 < (1 if first == third else 0) + (1 if first == fourth else 0):
                                    continue
                                if data[second] -1 < (1 if second == third else 0) + (1 if second == fourth else 0):
                                    continue
                            res.add(tuple(sorted([first, second,third,fourth])))
        return [list(i) for i in res]

        # ROFL I thought I was brute forcing it and was going to run in it back after getting it in to do something
        # faster - I beat 95% -  the tuple and sorted is slower than it needs to be I cna make this faster - not worth
#     the time though

sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))
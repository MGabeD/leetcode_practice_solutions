class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        if len(queries) == 0:
            return []

        data = {}
        for i in words:
            cur = lexi_min(i)
            if cur in data:
                data[cur] += 1
            else:
                data[cur] = 1


        upper_bound = max(data.keys())
        above_me = [0] * (upper_bound+1)
        for i in range(upper_bound-1, -1, -1):
            above_me[i] = above_me[i+1] + data.get(i+1,0)

        res = []
        for i in queries:
            cur = lexi_min(i)
            if cur > upper_bound:
                res.append(0)
            else:
                res.append(above_me[lexi_min(i)])
        return res


def lexi_min(s):
    min_char = "z"
    ctr = 0
    for i in s:
        if i < min_char:
            ctr = 1
            min_char = i
        elif i == min_char:
            ctr+=1
    return ctr

#         This is def the right approach but building the intermediary array is going ot be slow due to the size of the
# testing samples... I am not getting any efficiency gains since I am still iterating over upperbound 1x per run with
# the pre-computing... This is kind of annoying since it should be a good optimization their testing cases are favoring
# doing sort then binsearch for each rather than prebuild and index with instant access. this is a fair take for the use
# case so I am not worried about it all - since I am doing another version that is same O() and this is just tuning it
# for the test cases. Its not like I have the same base algo and am making more efficent jumps it is a design choice on
# pre-compute or use sort then binsearch... Mild optimizations available above but its not worth it for this question to
# chase them all

# Summary beats 40% so slow but on principle don't want to switch to the faster version since they have bad boundaries
# I don't like that there is no scaling since we have <2000 chars and only length max => 10 for queries and words. This
# is a better problem if there are len -> thousands - now which one pays off - what cases to chase.

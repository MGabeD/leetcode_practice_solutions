# backfill for 5/4
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Yes I am doing a bunch of leetcode easy questions. I am making sure I can do them in like <5min each. so will
        # do so0me extra qestios for fun (note even with me falling behind I have more questions completed then days
        # doing this)
        w1 = s1.split(' ')
        w2 = s2.split(' ')
        data = set()
        cur = set()
        for i in w1:
            if i in data:
                cur.discard(i)
            else:
                cur.add(i)
                data.add(i)
        for i in w2:
            if i in data:
                cur.discard(i)
            else:
                cur.add(i)
                data.add(i)
        return list(cur)

sol = Solution()
sol.uncommonFromSentences("apple apple", "banana")

# THis can prob be made marginally aster but its fine for now. beat 100% so all G
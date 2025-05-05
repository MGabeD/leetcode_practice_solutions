# back fill for 4/30

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        data = ['']*len(s)
        for i in range(0, len(s)):
            data[indices[i]] = s[i]
        return ''.join(data)

        # This solution beats 100% - this was an easy so I will likely throw ane xtra on once done filling the backlog
        # this may be faster with bit array logic but since I am 0ms on leetcode it can't validate that and I am
        # practically doibng the same exact logic so it may actually be the exact same. I just don't 100% know so
        # I don't want to waste the effort

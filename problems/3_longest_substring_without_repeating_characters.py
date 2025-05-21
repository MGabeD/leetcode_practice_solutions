class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = dict()
        cur_max = 0
        cur_start = 0
        for i in range(len(s)):
            if s[i] in data:
                if i - cur_start > cur_max:
                    cur_max = i - cur_start
                if data[s[i]] + 1 > cur_start:
                    cur_start = data[s[i]] + 1
            data[s[i]] = i
        if len(s) - cur_start > cur_max:
            return len(s) - cur_start
        return cur_max

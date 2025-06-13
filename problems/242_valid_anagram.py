class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        data = {}
        for i in s:
            if i in data:
                data[i]+=1
            else:
                data[i] = 1
        for i in t:
            if i in data:
                data[i]-=1
                if data[i] == 0:
                    del data[i]
            else:
                return False
        if len(data) > 0:
            return False
        return True

sol = Solution()
sol.isAnagram("anagram", "nagaram")
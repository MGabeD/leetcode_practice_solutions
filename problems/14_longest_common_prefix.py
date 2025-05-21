class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        idx = 0
        while idx < len(strs[0]):
            common_prefix = strs[0][idx]
            for i in strs:
                if len(i) <= idx or i[idx] != common_prefix:
                    return strs[0][:idx]
            idx += 1
        return strs[0]
    #beats 100%
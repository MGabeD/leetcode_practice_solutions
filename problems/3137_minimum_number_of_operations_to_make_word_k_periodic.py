class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        strs = {}
        max_idx = 1
        max_str = word[:k]
        for i in range(0, len(word), k):
            strs[word[i:i + k]] = strs.get(word[i:i + k], 0) + 1
            if strs[word[i:i + k]] > max_idx:
                max_str = word[i:i + k]
                max_idx = strs[max_str]
        total = len(word) // k
        return total - max_idx

#     This can be faster with a default dict and just by doing max(of the values in the dict) and but not worth
# implementing since it is the same big O



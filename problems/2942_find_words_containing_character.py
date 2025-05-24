class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        arrs_idx = []
        for i in range(len(words)):
            for j in words[i]:
                if j==x:
                    arrs_idx.append(i)
                    break

        return arrs_idx
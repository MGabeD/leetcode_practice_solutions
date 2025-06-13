class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        mapping = {}
        claimed = set()
        iter_word = 0
        for i in pattern:
            if iter_word >= len(words):
                return False
            while not words[iter_word]:
                iter_word += 1
                if iter_word > len(words):
                    return False

            if i in mapping:
                if mapping[i] != words[iter_word]:
                    return False
            else:
                if words[iter_word] in claimed:
                    return False
                claimed.add(words[iter_word])
                mapping[i] = words[iter_word]
            iter_word += 1

        if iter_word < len(words):
            for i in range(iter_word, len(words)):
                if words[iter_word]:
                    return False
        return True

sol = Solution()
sol.wordPattern("jquery", "jquery")
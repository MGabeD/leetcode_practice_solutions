class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keys = {
            "2": ["a","b","c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r","s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y","z"],
        }
        def combine(idx):
            cur = []
            if idx < len(digits)-1:
                nxt = combine(idx+1)
                for i in keys[digits[idx]]:
                    cur.extend(i+j for j in nxt)
                return cur
            elif idx < len(digits):
                return keys[digits[idx]]
            return []
        return combine(0)
    # beats 100%
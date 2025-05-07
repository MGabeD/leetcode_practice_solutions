# Extra one sine I am done with backfill
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        w1 = set()
        valid_words = set(words1)
        w2 = set()
        for w in words1:
            if w in w1:
                valid_words.discard(w)
            else:
                w1.add(w)
        for w in words2:
            if w in w2:
                valid_words.discard(w)
            else:
                w2.add(w)
        return len(valid_words & w2)
        # 2 min solution but can be faster hypothetically depending on the test cases
#     submitted the same one twice once beats 100% one beat 60% not worth doing more work


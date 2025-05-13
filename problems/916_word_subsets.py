# Backfill for friday =)


# class Solution(object):
#     def wordSubsets(self, words1, words2):
#         """
#         :type words1: List[str]
#         :type words2: List[str]
#         :rtype: List[str]
#         """
#         # This is a dumb pattern... I would skip this one if I wasn't doing the random selector...
#         words_data = []
#
#         for word in words1:
#             cur = {}
#             for ltr in word:
#                 if ltr in cur:
#                     cur[ltr] += 1
#                 else:
#                     cur[ltr] = 1
#             words_data.append(cur)
#
#         # this part is the jump ppl will miss - i can pre-compute the requirement to be universal and thus not have
#         # the massive double looping len(w1) * len(w2) for comparison
#
#         universal_req = {}
#         for word in words2:
#             cur = {}
#             for c in word:
#                 if c in cur:
#                     cur[c] +=1
#                 else:
#                     cur[c] = 1
#             for k,v in cur.items():
#                 if universal_req.get(k, 0) < v:
#                     universal_req[k] = v
#
#         valid_words = []
#         for i in range(0, len(words_data)):
#             add = True
#             for k,v in universal_req.items():
#                 if v > words_data[i].get(k,0):
#                     add = False
#                     break
#             if add:
#                 valid_words.append(words1[i])
#
#         return valid_words

#     One shotted the right algo :) there are mild optimizations I can do to eek out around 40% faster according to
#  leetcode -  this beats 86% right now - I am going to do enough to beat 90% then keep going

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # I can prob be faster if I use different data types => less iteration on words if I just do a set - don't have
        # to add can just remove when false - faster marginally for large sets of words which I think the test set has
        valid_words = set(words1)
        universal_req = {}
        # As wordlength < 10^4 i think looping over this up to 26 times using count is slower... if super small words
        # then not a given - i think the looping may be faster for this case - time to make dict max hashes 26 should
        # be faster
        for word in words2:
            cur = {}
            for c in word:
                if c in cur:
                    cur[c] +=1
                else:
                    cur[c] = 1
            for k,v in cur.items():
                if k not in universal_req or universal_req[k] < v:
                    universal_req[k] = v
        for word in words1:
            cur = {}
            for c in word:
                if c in cur:
                    cur[c] += 1
                else:
                    cur[c] = 1
            for k,v in universal_req.items():
                if k not in cur or cur[k] < v:
                    valid_words.remove(word)
                    break
        return list(valid_words)

    # This beats 90.23 % so I am going to stop trying to get little bits of optimization out of it now. I can still
    # almost half its runtime but I think most of that is the eq of reward hacking - ppl fitting the algo to the test
    # cases... I am happy with a mostly efficient best algo structure for this.

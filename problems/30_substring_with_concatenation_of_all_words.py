
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # ws = {}
        # for i in words:
        #     if i in ws:
        #         ws[i] += 1
        #     else:
        #         ws[i] = 1
        #
        # word_length = len(words[0])
        # res = []
        # for i in range(len(s)-word_length*len(words)+1):
        #     cur_substr = s[i:i+word_length*len(words)]
        #     valid = {}
        #     to_add = True
        #     for j in range(0, len(cur_substr), word_length):
        #         chunk = cur_substr[j:j+word_length]
        #         if chunk not in ws:
        #             to_add = False
        #             break
        #         if chunk in valid:
        #             if ws[chunk] > valid[chunk]:
        #                 valid[chunk] += 1
        #                 continue
        #             to_add = False
        #             break
        #         valid[chunk] = 1
        #     if to_add:
        #         res.append(i)
        # return res
#         OK so I didn't do any DP strategy here and because of that i am only beating 13% lets do a bit better
#         ws = {}
#         for i in words:
#             if i in ws:
#                 ws[i] += 1
#             else:
#                 ws[i] = 1
#
#         word_length = len(words[0])
#         res = []
#         invalid = set()
#         full_chunk_valid = set()
#         for i in range(len(s)-word_length*len(words)+1):
#             cur_substr = s[i:i+word_length*len(words)]
#             # I added this stupidly thinking it would be helpful - it cut the time in half but it requires
#             # in baked assumptions about what the strings will look like - this highly favors repetative strings
#             if cur_substr in full_chunk_valid:
#                 res.append(i)
#                 continue
#             if cur_substr in invalid:
#                 continue
#             cur_chunk_words = {}
#             to_add = True
#             j=0
#             while j < len(cur_substr):
#                 chunk = cur_substr[j:j+word_length]
#                 j += word_length
#                 if chunk not in ws:
#                     to_add = False
#                     invalid.add(cur_substr)
#                     break
#                 if chunk in cur_chunk_words:
#                     if ws[chunk] > cur_chunk_words[chunk]:
#                         cur_chunk_words[chunk] += 1
#                         continue
#                     to_add = False
#                     invalid.add(cur_substr)
#                     break
#                 cur_chunk_words[chunk] = 1
#             if to_add:
#                 full_chunk_valid.add(cur_substr)
#                 res.append(i)
#         return res
#         This beats 50% I see a way of keeping it all dynamic and thus faster - maybe worth doing
        wl = len(words[0])
        wsl = len(words) * wl
        words_dict = {}
        for w in words:
            if w in words_dict:
                words_dict[w] +=1
            else:
                words_dict[w] =1

        invalid = set()
        valid = set()
        locs = dict()
        res = []
        for i in range(len(s)-wsl+1):
            if i%wl in locs:
                cursor = i%wl
                cur_active = locs[cursor]
                tmp = s[i + wsl-wl:i+wsl]
                if tmp in words_dict:
                    if tmp in cur_active:
                        cur_active[tmp] +=1
                    else:
                        cur_active[tmp] = 1

                    if words_dict[tmp] > cur_active[tmp]:
                        invalid.add(s[i:i+wsl])
                        del locs[cursor]
                    else:
                        valid.add(s[i:i+wsl])
                        res.append(i)
                        locs[cursor][s[i:i+wl]] -= 1
            else:
                cur_substr = s[i:i+wl*len(words)]

                if cur_substr in valid:
                    res.append(i)
                    continue
                if cur_substr in invalid:
                    continue
                cur_chunk_words = {}
                to_add = True
                j=0
                while j < len(cur_substr):
                    chunk = cur_substr[j:j+wl]
                    j += wl
                    if chunk not in words_dict:
                        to_add = False
                        invalid.add(cur_substr)
                        break
                    if chunk in cur_chunk_words:
                        if words_dict[chunk] > cur_chunk_words[chunk]:
                            cur_chunk_words[chunk] += 1
                            continue
                        to_add = False
                        invalid.add(cur_substr)
                        break
                    cur_chunk_words[chunk] = 1
                if to_add:
                    valid.add(cur_substr)
                    res.append(i)
        return res
#     People are reward hacking this I was looking at the faster solutions and they have specific edge cases written
# in like 5000x a to get faster. i alrready have osme that are kind of hhacky i don't feel the need to go further.



#
# sol = Solution()
# sol.findSubstring("barfoothefoobarman", ["foo","bar"])
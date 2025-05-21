class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        simplified = ""
        cur = ""
        for i in range(0,len(p)):
            if p[i] == "*":
                if cur == "":
                    return False
                elif p[i-1] == "*":
                    return False
                continue
            if i+1 < len(p) and p[i+1] == "*":
                if cur != "":
                    if cur[0] == p[i] or cur[0] == ".":
                        continue
                cur = p[i:i+2]
                simplified += cur
            else:
                simplified += p[i]
                cur = ""

        def recurse(sidx, pidx):
            if sidx < len(s):
                if len(simplified) == pidx:
                    return False
                if len(simplified) - pidx >= 2 and simplified[pidx + 1] == "*":
                        if s[sidx] == simplified[pidx] or simplified[pidx] =='.':
                            return recurse(sidx, pidx+2) or recurse(sidx+1, pidx)
                        else:
                            return recurse(sidx, pidx+2)

                else:
                    if simplified[pidx] != s[sidx] and simplified[pidx] != ".":
                        return False
                sidx +=1
                pidx +=1
            if sidx == len(s):
                if len(simplified)-pidx >= 2 and simplified[pidx+1]=="*":
                    return recurse(sidx,pidx+2)
                if len(simplified) != pidx:
                    return False
                return True
            return recurse(sidx,pidx)
        return recurse(0,0)

# beat 98% i'll take it... simpler was ebtter here I tried to over optimize in the beinging and kept getting caught on
# weird edge cases... need to remember to just wrie out the simple version first


sol = Solution()
# print(sol.isMatch("mississippi", "mis*is*ip*."))
# print(sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*b"))
# print(sol.isMatch("aaa", "a*a"))
print(sol.isMatch("bbaa", "a..."))

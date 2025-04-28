# backfill for 4/22

class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        # This feels greedy to me... there is no world where not throwing away the biggest one first is not better.
        # This could literally just be a sort array then empty from bottom until you can't then top and repeat...
        # tokens.sort()
        # bottom = 0
        # top = len(tokens)-1
        # if len(tokens) == 0 or power < tokens[0]:
        #     return 0
        # max_score = 0
        # score = 0
        # while bottom <= top:
        #     if tokens[bottom] <= power:
        #         power -= tokens[bottom]
        #         score += 1
        #         bottom += 1
        #     elif score > 0:
        #         power += tokens[top]
        #         top -= 1
        #         score -= 1
        #     if score > max_score:
        #         max_score = score
        #
        # return max_score

        # ONLY got mid 80s with above. Clearly the correct algo but inefficient in its execution lets improve it
        tokens.sort()
        score, max_score = 0,0
        bottom, top = 0, len(tokens)-1
        # guarding was unnecesary and extra overhead. THis wya that is gone - stil sicne since top is len()-1 so empty
        # is protected
        while bottom <= top:
            if power >= tokens[bottom]:
                power -= tokens[bottom]
                score += 1
                bottom += 1
                if max_score < score:
                    max_score = score
            elif score > 0:
                power += tokens[top]
                top -= 1
                score -= 1
            else:
                return max_score

        # Ok so the problem was literally the filtering at the top and the extra if being hit on each iteration in the
        # while loop. This is now bets 100%. For the future remember this - no need to check if a condition is
        # impossible will just make everything slows

        return max_score

sol = Solution()
sol.bagOfTokensScore([100,200,300,400], 200)
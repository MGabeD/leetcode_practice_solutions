# My backfill question for 4/19
from pkgutil import resolve_name


# You know its kinda weird that the only reason I open pycharm now-days is for leetcode.
# I only code using IDEs with native llm auto complete now, but that is truely cheating for these. I also have noticed
# in some of my work that the tab auto completes destroys my ability to self optimize in ~write~ time and thus make me
# faster -> solution but if it gives a mid answer getting from that to something better is harder (still faster though)
# even if I thought up the algo - kind of like how notes are better if you by hand summarize them into a study guide
# rather than just re-reading. Thus in my other projects I have to split between read and write time for my own work now
# its kind of fascinating how it changes development
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        # I am feeling like starting to write out my thinking so i can go back to iterating and I am in a yappy mood
        # My solution here from looking at it is to instantly deque -> instant access forward and back keep len 4 all in
        # constant time avg each call takes len(deque) so we will be doing O(k*n) which is pretty quick.

        # However, I thought about how to make this event faster. I don;t need to be constantly grabbing the avg - I can
        # just hold the moving sum. This also makes the deque kind of useless since I can just index directly on the
        # array in constant time.
        # Now I am looking at this [initing loop] -> for k, len(arr) -> wking_sum = (wking_sum - arr[i-k] +arr[i]) -> if
        # ... and thsi should be the fastest it can be
        # walking_sum = 0
        # ctr = 0
        # for i in range(0, k):
        #     walking_sum += arr[i]
        # if walking_sum/k >= threshold:
        #     ctr+= 1
        # for i in range(k, len(arr)):
        #     walking_sum += arr[i] - arr[i-k]
        #     if walking_sum/k >= threshold:
        #         ctr+= 1
        # return ctr
        # Hmm i didn't even get beats 90th with this and it seems quite possible to going to take a shot at being faster
        # That being said I def got the right solution - we're in call optimization land now

        # I believe looping is slower than the inbuilts in python even though the core is the same
        walking_sum = sum(arr[:k])
        ctr = 0
        # I was doing and extra division for each step - this is an extra operation which while lightning fast is an
        # unnecessary and additive step
        threshold *= k
        if walking_sum >= threshold:
            ctr+= 1
        for i in range(k, len(arr)):
            walking_sum += arr[i] - arr[i-k]
            if walking_sum >= threshold:
                ctr+= 1
        return ctr

        # Ok still a bit more to pull out according to leetcode bit I don't see where to take it out and I am happy
        # with beating 97%,  it was the extra division step which was putting me in 80th. I didn't see it first attempt.
        #I should have seen it since it was clearly un-needed and added overhead. I like how i went for algo and getting
        # it crystalized firs though then in code, then optimization. I don't like how i missed this before entering it
        # so i can still do better but the process was good. I should add a step to my workflow where I try to look for
        # stupid things like this even on the first attempt thouhg - I think it will help in actual interviews as well

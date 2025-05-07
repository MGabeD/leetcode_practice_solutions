# Backfill for 5/2
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        # This is mean.. I don't know the days per month lmfao
        # going to look it up sice this is impossible without it
        # days_per_month = {
        #     1: 31,
        #     2: 28,
        #     3: 31,
        #     4: 30,
        #     5: 31,
        #     6: 30,
        #     7: 31,
        #     8: 31,
        #     9: 30,
        #     10: 31,
        #     11: 30,
        #     12: 31,
        # }
        # Now lets pre-compute what we actually want to know
        # days_pre_dating_month = {
        #     1: 0,
        #     2: 31,
        #     3: 59,
        #     4: 90,
        #     5: 120,
        #     6: 151,
        #     7: 181,
        #     8: 212,
        #     9: 243,
        #     10: 273,
        #     11: 304,
        #     12: 334,
        # }
        # cur = days_pre_dating_month[int(date[5:7])] + int(date[8:])
        # year = int(date[0:4])
        # print(year%400 == 0)
        # print(year%100 != 0)
        # if int(date[5:7]) > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        #     cur += 1
        #
        # return cur
#     Weirdly this is slow.... lts switch this up a little
        days_pre_dating_month = [ 0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        [y,m,d] = [int(s) for s in date.split('-')]

        if m > 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            return days_pre_dating_month[m] + d + 1

        return days_pre_dating_month[m] + d
#     this is showing as slower. i do't trust leetcode on this honestly. It is saying this is faster

# [y, m, d] = [int(s) for s in date.split('-')]
# c = 0
# md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if (y % 4 == 0):
#     md[2] = 29
# if (y % 100 == 0 and y % 400 != 0):
#     md[2] = 28
#
# return sum(md[:m]) + d

# Note that this is the exact same thing BUT with extra calls c = 0 (instantiation before setting. Slower than straight
# returning the value. Also pre-computing w/ an array then indexing is 0(1) rather than O(m) so something is wrong
# with their test cases. The only way this can truely be THAT much faster is if they have a heavy bias towards low
# months in their test cases (which makes sense for edge cases) as the if m>2 is an extra call which is slower than sum
# of a single value.
sol = Solution()


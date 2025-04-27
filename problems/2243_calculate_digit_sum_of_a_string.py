# class Solution(object):
#     def digitSum(self, s, k): 
#         """
#         :type s: str
#         :type k: int
#         :rtype: str
#         """
#         while len(s) > k:
#             cur = ""
#             for i in range(0, len(s), k):
#                 if i + k > len(s):
#                     cur += str(self.sum_of_digits(s[i:]))
#                 else:
#                     cur += str(self.sum_of_digits(s[i:i+k]))
#             s = cur
#         return s

#     def sum_of_digits(self, s):
#         sum = 0
#         for i in range(0, len(s)):
#             sum += int(s[i])
#         return sum

# solution = Solution()
# print(solution.digitSum("1111122222", 3))

#  This was the first run through - doing it this way is not efficient lets do it without having the overhead of another function and jsut do the while loop - will be faster
# Also my if condition is unneccesary as we can just do the sum of the digits in the while loop

class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            cur = ""
            for i in range(0, len(s), k):
                grp = s[i:i+k]
                grp_sum = sum(int(digit) for digit in grp)
                cur += str(grp_sum)
            s = cur
        return s

# class Solution(object):
#     def findFarmland(self, land):
#         """
#         :type land: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         # so instantly I am seeing a super slow but working algorithm but I think that it is a waste of time to actually
#         # implement the iterative solution of going box by box. The fact that he groups are rectangular means that I have
#         # a bunch of assumptions which can decrease my complexity. I need to think about these possible solutions. This
#         # seems like a search question to me so i am going to try to think of how to implement something with a search
#         if len(land) == 0 or land[0] == []:
#             return []
#         answers = []
#         max_n = len(land[0]) - 1
#         max_m = len(land) - 1
#         cur_stack = [(0,0)]
#         while len(cur_stack) > 0:
#             cur_m, cur_n = cur_stack.pop()
#             if land[cur_m][cur_n] == 2:
#                 continue
#             elif land[cur_m][cur_n] == 0:
#                 if cur_m < max_m and land[cur_m+1][cur_n] != 2:
#                     cur_stack.append((cur_m+1, cur_n))
#                 if cur_n < max_n and land[cur_m][cur_n+1] != 2:
#                     cur_stack.append((cur_m,cur_n+1))
#             else:
#                 top_left = []
#                 if (cur_n == 0 or land[cur_m][cur_n-1] != 1) and (cur_m == 0 or land[cur_m-1][cur_n] != 1):
#                     top_left = [cur_m, cur_n]
#                 if (cur_n == max_n or land[cur_m][cur_n+1] != 1) and (cur_m == max_m or land[cur_m+1][cur_n] != 1):
#                     bottom_right = [cur_m, cur_n]
#                 else:
#                     bottom_right = []
#                 while len(top_left) == 0:
#                     if cur_m > 0 and land[cur_m-1][cur_n] == 1:
#                         # rush to the top first
#                         cur_m -= 1
#                     elif cur_n > 0 and land[cur_m][cur_n-1] == 1:
#                         cur_n -= 1
#                     else:
#                         top_left = [cur_m, cur_n]
#                 while len(bottom_right) == 0:
#                     if cur_m < max_m and land[cur_m+1][cur_n] == 1:
#                         cur_m += 1
#                     elif cur_n < max_n and land[cur_m][cur_n+1] == 1:
#                         cur_n += 1
#                     else:
#                         bottom_right = [cur_m, cur_n]
#                 for i in range(top_left[0], bottom_right[0]+1):
#                     land[i][top_left[1]] = 2
#                     land[i][bottom_right[1]] = 2
#                 for i in range(top_left[1], bottom_right[1]):
#                     land[top_left[0]][i] = 2
#                     land[bottom_right[0]][i] = 2
#                 answers.append(top_left + bottom_right)
#                 if bottom_right[0] < max_m:
#                     cur_stack.append((bottom_right[0]+1, top_left[1]))
#                 if bottom_right[1] < max_n:
#                     cur_stack.append((top_left[0], bottom_right[1]+1))
#         return answers

# I was trying to get some marginal advancement in the speed by doing some smart finding of the top left top right but
# this just actually added a ton of complexity for understanding my solution, a bunch more manual work for figuring out
# cases and my own stack management and was unfortunately not actually more efficient.
# I was hoping skipping to blockingout the rectangles would befaster but it isn't

# here is a typical DFS approach that I wanted to avoid but is just hte necessary approach

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(land), len(land[0])
        res= []
        def dfs(i, j):
            bottom_i, bottom_j = i, j
            while bottom_i + 1 < m and land[bottom_i +1][j] == 1:
                bottom_i += 1
            while bottom_j + 1 < n and land[i][bottom_j+1] == 1:
                bottom_j += 1
            for x in range(i, bottom_i + 1):
                for y in range(j, bottom_j +1):
                    land[x][y] = 0
            res.append([i,j,bottom_i,bottom_j])

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    dfs(i,j)

        return res






a = Solution()
b = a.findFarmland([[1,0], [1,0]])
print(b)



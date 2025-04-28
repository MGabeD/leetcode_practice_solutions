# Backfill for 4/25

class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # This one is very different but a fun question. lets think on what it is asking for a bit

        # Can minimize the iterations by pre-computing a half step then iterating on it - saves nk

        # Can make the addition of this o(n) for ech col instead of nk by tracking before after on the itermediary
#         med_data = []
#         for i in range(0, len(mat)):
#             cur = 0
#             for j in range(0,k+1):
#                 if j >= len(mat[i]):
#                     continue
#                 cur += mat[i][j]
#             med_data.append([cur])
#
#         for i in range(0, len(mat)):
#             for j in range(1,len(mat[i])):
#                 cur = med_data[i][j-1]
#                 if j-k-1 >= 0:
#                     cur -= mat[i][j-k-1]
#                 if j+k < len(mat[i]):
#                     cur += mat[i][j+k]
#                 med_data[i].append(cur)
#         out_data = []
#         for i in range(0, len(mat)):
#             cur_row = []
#             for j in range(0, len(mat[1])):
#                 val = med_data[i][j]
#                 for l in range(1,k+1):
#                     if i+l < len(mat):
#                         val += med_data[i+l][j]
#                     if i-l >= 0:
#                         val += med_data[i-l][j]
#                 cur_row.append(val)
#             out_data.append(cur_row)
#         return out_data
#         This works but I think I missed something rather significant... I am seeing another pattern with maybe being
#         able to get any box by delta a top left vs bottom right & inclusion
#         n = len(mat)
#         m = len(mat[0])
#         out = [[0] * m for _ in range(n)]
#         prefix = [[0]*m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 prefix[i][j] = mat[i][j]
#                 if i > 0:
#                     prefix[i][j] += prefix[i-1][j]
#                 if j > 0:
#                     prefix[i][j] += prefix[i][j-1]
#                 if i > 0 and j > 0:
#                     prefix[i][j] -= prefix[i-1][j-1]
#
#         for i in range(n):
#             for j in range(m):
#                 r1 = max(0, i-k)
#                 c1 = max(0, j-k)
#                 r2 = min(n-1, i+k)
#                 c2 = min(m-1, j+k)
#
#                 val = prefix[r2][c2]
#                 if r1 > 0:
#                     val -= prefix[r1-1][c2]
#                 if c1 > 0:
#                     val -= prefix[r2][c1-1]
#                 if r1 > 0 and c1 > 0:
#                     val += prefix[r1-1][c1-1]
#
#                 out[i][j] = val
#         return out
#     I am still below average in speed damn... I need to think of something better. I have a lot of if conditions which
# are slow. maybe I should try padding... will keep my loops easier *faster* will also be
        n = len(mat)
        m = len(mat[0])

        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = (
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )

        out = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(n - 1, i + k)
                c2 = min(m - 1, j + k)

                val = (
                    prefix[r2 + 1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    - prefix[r1][c2 + 1]
                    + prefix[r1][c1]
                )

                out[i][j] = val

        return out
# Beats 92% I ma happy enough with this. from the delta between me and best there is still a good amount I could
# optimize ~50% of runtime 7 ms vs 15ms but this isn't worth chasing here I dont think



sol = Solution()
print(sol.matrixBlockSum(mat =[[1,2,3],[4,5,6],[7,8,9]], k=1 ))

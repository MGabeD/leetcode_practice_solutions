# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def largestValues(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         if root is None:
#             return []
#         return recurse_down(root)
#
# def recurse_down(root):
#     l = recurse_down(root.left) if root.left is not None else []
#     r = recurse_down(root.right) if root.right is not None else []
#     cur = [root.val]
#     for i in range(0, max(len(l), len(r))):
#         if len(l) > i:
#             if len(r) > i:
#                 cur.append(max(l[i],r[i]))
#             else:
#                 cur.append(l[i])
#         else:
#             cur.append(r[i])
#     return cur
# 1 shotted the slow solution with recursion. Now lets speed i up via looping instead.

from collections import deque

class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = deque([root])
        data = []
        while queue:
            biggest = -float('inf')
            for _ in range(len(queue)):
                cur = queue.popleft()
                if biggest < cur.val:
                    biggest = cur.val
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            data.append(biggest)
        return data

# Pretty sure this is the fastest possible but leetcode is down for maintanence for the rest of todya so cna't test it

# Went back and ran it had some simple obv issues. I am for some reason not in th efastest bucket. I looked at the best
# examples and they are functionally the same... If not slower. using max(x,y) adds a funciton overhead rather than the
# if to straight setting - minor higher overhead. The other dif is with if cur.left vs cur.left is not None - Need to
# check what this actually compiles into to tell which is better but optimizations at this level are a waste. Not sure
# I trust leetcode on this one since each tim I hit sumbitwith the same answer my runtime has a wild variance



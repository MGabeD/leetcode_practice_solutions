# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        data = recurse_to_find(root, k, 0)
        return data[1]


def recurse_to_find(cur, k, ctr):
    if cur.left is not None:
        left = recurse_to_find(cur.left, k, ctr)
        if left[0] is k:
            return left
        ctr = left[0]
    ctr += 1
    if ctr == k:
        return [ctr, cur.val]
    if cur.right is not None:
        val = recurse_to_find(cur.right, k, ctr)
        return val
    return [ctr, None]

# This can be done so that it is prettier but its the fastest method on leetcode (eq to the one with sub data structure)
# which can self recurse down
# not a very ~pythonic~ way of solving this problem but it is fast
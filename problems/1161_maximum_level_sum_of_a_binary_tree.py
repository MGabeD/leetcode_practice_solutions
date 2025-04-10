# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        data = {}
        self.recursively_sum(root=root, data=data, level=1)
        maximal_vals = data[1]
        idx = 1
        for k, v in data.items():
            if v > maximal_vals:
                maximal_vals = v
                idx = k
        return idx

    def recursively_sum(self, root, data, level):
        if root is None:
            return
        data[level] = data.get(level, 0) + root.val

        self.recursively_sum(root.left, data, level + 1)
        self.recursively_sum(root.right, data, level + 1)


# This can be made quite a bit faster by getting rid of the recursion overhead and doing this with a loop -> also don't
# have the overhead of the for loop with k,v on top of the descending down the recursive part I wrote

# These solutions are the exact same O() so I don't feel the need to implement it today
# to make this faster I could do
# for queue add left right
# sum everything in
# if > maximal sum -> set idx and maximal -> continue until at leafs


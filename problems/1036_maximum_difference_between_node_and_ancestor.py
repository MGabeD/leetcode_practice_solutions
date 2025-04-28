# back fill for 4/23

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # This question is cruel it shows a binary search tree in the first example so i started envisioning that algo
        # which is  alot faster and I was all happy

        # this will just be recursion... And slow.
        if root.right is not None:
            if root.left is not None:
                return max(recurse_down(root.right, root.val, root.val), recurse_down(root.left, root.val, root.val))
            else:
                return recurse_down(root.right, root.val, root.val)
        else:
            return recurse_down(root.left, root.val, root.val)

def recurse_down(root, min_value, max_value):
    self_max = 0
    if root.val > max_value:
        self_max = root.val - min_value
        max_value = root.val
    elif root.val < min_value:
        self_max = max_value - root.val
        min_value = root.val
    if root.left is not None:
        self_max = max(self_max, recurse_down(root.left, min_value, max_value))
    if root.right is not None:
        self_max = max(self_max, recurse_down(root.right, min_value, max_value))
    return self_max


# Ugly code but here is why - doing the if trees is faster than max() I should realisticallly fix the other two to go
# from beating 96% to 100% - reason -> max() has the overhead of creating another function call. This is tiny but is
# where the ms between me and the fastest is coming from. I did it in the root funciton because I know it is faster and
# was not locked inot fixing my base case. I also need to de-recursionize this function for this to be worth anything.
# It can be internal and do less passes just use a queue to get rid of the compilers overhead for creating a function
# I know of this optmization and that is enough for me to be happy here. I don't want to nitpick myself that much

# FIXME: if i want to go from 96% beaten to 100% get rid of recursion and max function calls to decrease that fn overhead
#  not going to do cause to much work rn...
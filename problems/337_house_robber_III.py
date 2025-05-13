# Back fill for saturday

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # This problem could be quite ~ complex
        # I see each recurse down as having two cases where the branches are active or not active. Maybe recursing and
        # selecting max going down that way for both would be the effective route? will give me a subproblem where I can
        # drop extra data on each recurse - elegant - maybe overcomputing though - but I think it is right
        # seems to collapse the problem correctly - just going ot odo it
        if root is None:
            return 0
        return max(recurse(root))

def recurse(root):
    max_unactive = 0
    max_active = root.val
    if root.right is not None:
        right_data = recurse(root.right)
        max_unactive += max(right_data)
        max_active += right_data[1]
    if root.left is not None:
        left_data = recurse(root.left)
        max_unactive += max(left_data)
        max_active += left_data[1]

    return max_active, max_unactive

# Massive variance in each run through. I already tried to over optimize earlier today. Don't want to waste the time to
# do it again. i cna drop the extra if overhead for each run to make one if by checking if none -> return 0,0 - lower
# if over head (1 instead of 2) same base run through as above increments -> 1 max calls still 2 - will be faster.
# Honestly by enough that maybe it is worth doing to show I understand it...

def recurse(root):
    if root is None:
        return 0,0
    left_data = recurse(root.left)
    right_data = recurse(root.right)
    max_unactive = max(left_data) + max(right_data)
    max_active = root.val + right_data[1] + left_data[1]

    return max_active, max_unactive

# yeah ok beats 97.95% worth doing IG
# Backfill for Sunday when I was traveling I think that was 5/11

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def tree2str(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: str
#         """
#         return recurse(root)
#
#
# def recurse(root):
#     left = None
#     right = None
#     if root.left is not None:
#         left = recurse(root.left)
#
#     if root.right is not None:
#         right = recurse(root.right)
#
#     if left is None and right is None:
#         return str(root.val)
#
#     if left is None:
#         left = ""
#
#     if right is not None:
#         return str(root.val) + "(" + left + ")(" + right + ")"
#
#     return str(root.val) + "(" + left + ")"

# No need to isolate the recursion - just done for readability - will be faster without it. Lets write it
# Note the above works and beats over 80% - we are just making it a little bit better

class Solution(object):
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"

# This is still only 90% I don't see any more efficiency I can grab. i think there are not enough test cases to actually
# evaluate the minor gains. I just looked at some of the other answers they are all the same. The thing I did first
# matches solutions faster than mine. The second one I did both ones faster and slower. i think the variance is just
# the test cases. I ran this one a few times and get huge differences.
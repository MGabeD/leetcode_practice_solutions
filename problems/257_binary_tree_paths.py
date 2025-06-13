# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if root is None:
            return []
        children = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.left)
        if len(children) > 0:
            return [str(root.val) + "->" + i for i in children]
        return [str(root.val)]
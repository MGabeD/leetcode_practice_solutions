class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        new_tree, leaf = self.subproblem(root)
        return new_tree

    def subproblem(self, cur_node):
        if cur_node.left is not None:
            root, leaf = self.subproblem(cur_node.left)
            leaf.right = TreeNode(cur_node.val, None, None)
            leaf = leaf.right
        else:
            root = TreeNode(cur_node.val, None, None)
            leaf = root
        if cur_node.right is not None:
            right_root, right_leaf = self.subproblem(cur_node.right)
            leaf.right = right_root
            leaf = right_leaf
        return root, leaf


# This was the optimal solution for runtime - space wise it bee 82% so I prob have somehwere I can cut some data by
# not passing around so much but I am not worried about solving this. It is too easy to waste time on getting space down
# the speed and doing ti quickly is what matters fior this question, there is no major optimzation left


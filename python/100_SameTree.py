# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_list = self.dfs(p)
        q_list = self.dfs(q)
        print p_list, q_list
        if p_list == q_list:
            return True
        else:
            return False
    
    def dfs(self, tree):
        tree_list = []
        if tree:
            tree_list.append(tree.val)
            tree_list.extend(self.dfs(tree.left))
            tree_list.extend(self.dfs(tree.right))
        else:
            tree_list.append(None)
        return tree_list
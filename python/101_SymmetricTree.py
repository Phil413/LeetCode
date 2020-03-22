# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root, root)
    
    def is_mirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left):
            if left.val == right.val:
                return True
            else:
                return False
        else:
            return False

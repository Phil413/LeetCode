# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        递归
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

    def isSymmetric2(self, root):
        """
        迭代
        :type root: TreeNode
        :rtype: bool
        """
        tmp_list = [root, root]
        p = root
        while (tmp_list):
            if len(tmp_list) < 2:
                return False
            left = tmp_list.pop(0)
            right = tmp_list.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                tmp_list.extend([left.left, right.right])
                tmp_list.extend([left.right, right.left])
            else:
                return False
        return True

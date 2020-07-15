"""
空树为二叉搜索树 array[0] = 1
n = 1时，数量为左子树数量*右子树数量，1 * 1 = 1, array[1] = 1
n = 2时，1做根 array[0] * array[1] + 2做根 array[1] * array[0]
n = 3时，1做根 array[0] * array[2] + 2做根 array[1] * array[1] + 3做根 array[2] * array[0]
n = n时，1做根 array[0] * array[2] + ... + j做根 array[j - 1] * array[n - j] + ... + n做跟 array[n-1] * array[0]
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        array = dict()
        for i in range(n+1):
        	array[i] = 0
        array[0] = 1
        for i in range(1, n + 1):
        	for j in range(1, i + 1):
        		array[i] += array[j - 1] * array[i - j]
        return array[n]


if __name__ == "__main__":
	sl = Solution()
	print(sl.numTrees(4))

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len_nums = len(nums)
        i = 0
        while i < len_nums:
        	if nums[i] == val:
        		del nums[i]
        		len_nums -= 1
        	else:
        		i += 1
       	return len(nums)
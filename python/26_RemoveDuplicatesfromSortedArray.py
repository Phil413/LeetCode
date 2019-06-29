class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        i = 1
        while i < len_n:
            if nums[i] == nums[i-1]:
                del nums[i]
                len_n -= 1
            else:
                i += 1
        
        return i

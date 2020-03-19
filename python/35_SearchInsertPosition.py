class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
        	mid = (left + right) // 2
        	if nums[mid] == target:
        		return mid
        	elif target > nums[mid]:
        		left = mid + 1
        	else:
        		right = mid - 1
        if right < 0:
        	right = 0
        mid = (left + right) // 2
        if target > nums[mid]:
        	return mid + 1
        else:
        	return mid


if __name__ == "__main__":
	sl = Solution()
	print(sl.searchInsert([1,3], 2))
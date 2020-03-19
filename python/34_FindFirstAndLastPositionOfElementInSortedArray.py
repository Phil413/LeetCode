class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        start = end = -1
        while left <= right:
        	mid = (left + right) // 2
        	if nums[mid] == target:
        		start = end = mid
        		while start >=0 and nums[start] == target:
        			start -= 1
        		while end < len(nums) and nums[end] == target:
        			end += 1
        		return [start+1, end-1]
        	elif target < nums[mid]:
        		right = mid - 1
        	else:
        		left = mid + 1
       	return [start, end]


if __name__ == "__main__":
	sl = Solution()
	print(sl.searchRange([5,7,7,8,8,10], 6))
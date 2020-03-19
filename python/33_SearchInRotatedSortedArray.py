class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
        	mid = (right + left) // 2
        	if target == nums[mid]: return mid
        	if nums[left] <= nums[mid]:
        		if target >= nums[left] and target < nums[mid]:
        			right = mid
        		else:
        			left = mid + 1
        	else:
        		if target <= nums[right] and target > nums[mid]:
        			left = mid + 1
        		else:
        			right = mid
        return -1
 

if __name__ == "__main__":
	sl = Solution()
	print(sl.search([4,5,6,7,0,1,2], 4))
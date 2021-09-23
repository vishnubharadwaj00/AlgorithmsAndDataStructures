def searchInsert(nums, target):
	left = 0
	right = len(nums)-1
	
	while(left<right):
		mid = (left + right)//2
		if target == nums[mid]:
			return mid
		elif target < nums[mid]:
			right = mid
		else:
			left = mid+1
	if target > nums[-1]:
		return len(nums)
	else:
		return left
nums = [1,3,5,6]
target = 7
print(searchInsert(nums,target))
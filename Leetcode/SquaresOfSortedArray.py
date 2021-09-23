def sortedSquares(nums):
	output = [0]*len(nums)
	write = len(nums) - 1
	left = 0
	right = len(nums) - 1

	left_sq = nums[left]**2
	right_sq = nums[right]**2

	while(write>=0):
		if left_sq > right_sq:
			output[write] = left_sq
			left +=1
			left_sq = nums[left]**2
		else:
			output[write] = right_sq
			right -=1
			right_sq = nums[right]**2
		write-=1
	return output
		
nums = [-4,-4,-3]
x = sortedSquares(nums)
print(x)
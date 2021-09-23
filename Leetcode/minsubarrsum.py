def minsubarraysum(target, nums):
	left = 0 
	result = float('inf')
	valsum = 0

	for i in range(len(nums)):
		valsum += nums[i]
		while valsum >= target:
			result = min(result, i+1-left)
			valsum -= nums[left]
			left+=1

	if result == float('inf'):
		return 0
	return result

	

minsubarraysum(7,[2,3,1,2,4,3])
def rob(nums):
    if len(nums) == 0 or len(nums)==1: 
            return nums[0]
    elif len(nums) == 2:
            return max(nums[0],nums[1])
    else:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return max(dp)
nums = [1,2,3,1]
print(rob(nums))


def maxsuba(nums): #DPSol   
    dp = [None] * len(nums) 
    dp[0] = nums[0]
    maxi = dp[0]

    for i in range(1,len(nums)):
        dp[i] = max(nums[i]+dp[i-1], nums[i])
        maxi = max(maxi, dp[i])

    return maxi 

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsuba(nums))
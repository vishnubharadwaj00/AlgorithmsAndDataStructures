"""
This implementation exceeds time-limit, brute-force approach:

def rotate(nums, k):
    while k>0:
        temp = nums[-1]
        for i in reversed(range(0,len(nums)-1)):
            nums[i+1]=nums[i]
        nums[0]=temp
        k-=1
        print(nums)
"""

def rotate(nums,k):
    k = k % len(nums)
    end = len(nums)-1
    reverse(nums,0,end-k)
    reverse(nums,end-k+1,end)
    reverse(nums,0,end)
    print(nums)

def reverse(nums,start,end):
    while(start<end):
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1

    
nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)
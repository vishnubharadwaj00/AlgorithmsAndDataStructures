nums=[1,3,5,6]
target=7

def searchinsertposition(nums,target):
    for i in range(0,len(nums)):
        if nums[i]==target:
            return i
        elif nums[i]>target:
            return i
    return len(nums)
    
searchinsertposition(nums,target)
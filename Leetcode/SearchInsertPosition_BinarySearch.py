nums=[1,3,5,6]
target=2

def searchinsertposition(nums,target):
    left=0
    right=len(nums)-1
    
    while(left <= right):
        mid=(left+right)//2
        print(left,mid,right)
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            right=mid-1
        else:
            left=mid+1
            
    return left
    
x=searchinsertposition(nums,target)
print(x)
def search(nums, target):
        x = binsearch(nums, 0, len(nums)-1, target)
        print(x)

def binsearch(arr, left, right, target):
    if left <= right:
        mid = (left + right)//2
        if target == arr[mid]:
            return mid 
        elif target < arr[mid]:
            return binsearch(arr, left, mid-1, target)
        else:
            return binsearch(arr, mid+1, right, target)
    else:
        return -1 

nums = [-1,0,3,5,9,12]
target = 2
search(nums,target)


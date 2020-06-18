nums = list(map(int, input().split()))
inverse = len(nums)-2

while(inverse >= 0 and nums[inverse] >= nums[inverse+1]):
    inverse -= 1

if(inverse < 0):
    nums = nums[::-1]
else:
    for i in reversed(range(inverse, len(nums))):
        if(nums[i] > nums[inverse]):
            nums[i], nums[inverse] = nums[inverse], nums[i]
            break

    nums[inverse+1:] = reversed(nums[inverse+1:])

print(nums)

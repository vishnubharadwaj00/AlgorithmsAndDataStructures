def sortcolors(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    print(nums)


lst = [2, 0, 2, 1, 1, 0]
sortcolors(lst)

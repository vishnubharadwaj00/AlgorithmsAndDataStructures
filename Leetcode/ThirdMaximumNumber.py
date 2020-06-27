def thirdmax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return nums[-1]
    for i in range(0, 2):
        nums.remove(max(nums))
    return max(nums)


lst = [-2, 2, 3, 1]
x = thirdmax(lst)
print(x)

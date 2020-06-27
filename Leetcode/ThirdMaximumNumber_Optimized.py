def thirdmax(nums):
    v = [float('-inf'), float('-inf'), float('-inf')]
    for i in nums:
        print(v)
        if i not in v:
            if i > v[0]:
                v = [i, v[0], v[1]]
            elif i > v[1]:
                v = [v[0], i, v[1]]
            elif i > v[2]:
                v = [v[0], v[1], i]
    print(v)
    return max(v) if float('-inf') in v else v[2]


nums = [-2, 2, 3, 1, 4]
x = thirdmax(nums)
print(x)

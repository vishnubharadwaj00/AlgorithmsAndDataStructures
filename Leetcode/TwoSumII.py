def twosum(numbers, target):
    n = len(numbers)
    end = n-1
    while(target < numbers[end] and target > 0):
        end -= 1
    start = end-1
    while(start <= end):
        print(start, end)
        total = numbers[start]+numbers[end]
        if total == target:
            return [start+1, end+1]
        elif start == 0:
            end -= 1
            start = end-1
        else:
            start -= 1


numbers = [-1, 0]
target = -1
x = twosum(numbers, target)
print(x)

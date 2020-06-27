def findmedian(nums1, nums2):
    if len(nums1) > len(nums2):
        findmedian(nums2, nums1)

    x = len(nums1)
    y = len(nums2)
    start = 0
    end = x
    while(start <= end):
        partitionx = (start+end)//2
        partitiony = ((x+y+1)//2)-partitionx

        maxleftx = float('-inf') if partitionx == 0 else nums1[partitionx-1]
        minrightx = max(max(nums1), max(nums2)) + \
            1 if partitionx == x else nums1[partitionx]

        maxlefty = float('inf') if partitiony == 0 else nums2[partitiony-1]
        minrighty = max(max(nums1), max(nums2)) + \
            1 if partitiony == y else nums2[partitiony]

        if(maxleftx <= minrighty and maxlefty <= minrightx):
            if (x+y % 2 == 0):
                print(max(maxleftx, maxlefty))
                print(min(minrightx, minrightx))
                return (max(maxleftx, maxlefty)+min(minrightx, minrighty))/2
            else:
                return max(maxleftx, maxlefty)
        else:
            if(maxleftx > minrighty):  # too far right
                end = partitionx-1
            else:
                start = partitionx+1


nums1 = [1, 2]
nums2 = [3, 4]

x = findmedian(nums1, nums2)
print(x)

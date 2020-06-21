def findmedian(nums1,nums2):
    for i in range(0,len(nums2)):
        nums1.append(nums2[i])
    nums1.sort()
    n=len(nums1)
    if(n%2==0):
        print(nums1[n//2-1],nums1[n//2])
        return (nums1[n//2-1]+nums1[n//2])/2
    else:
        return float(nums1[n//2])
        
    
nums1=[1,3]
nums2=[2]

x=findmedian(nums1,nums2)
x
nums1=[-1,3,0,0,0,0,0]
nums2=[0,0,1,2,3]
n=len(nums2)
m=len(nums1)-n

def mergesorted(nums1, m, nums2, n):
    index=len(nums1)-1
    m-=1
    n-=1
    
    while (index>=0):
        if (m < 0):
            nums1[index]=nums2[n]
            n-=1
        elif (n < 0):
            nums1[index]=nums1[m]
            m-=1
        else:
            if nums1[m] > nums2[n]:
                nums1[index]=nums1[m]
                m-=1
            else:
                nums1[index]=nums2[n]
                n-=1
        index-=1
    print(nums1)

  
mergesorted(nums1,m,nums2,n)    
nums1=[-1,3,0,0,0,0,0]
nums2=[0,0,1,2,3]
n=len(nums2)
m=len(nums1)-n



def mergesorted(nums1, m, nums2, n):
    a=0
    b=0
    
    while(b!=n and a!=m+n):
        print(nums1[a],nums2[b])
        print(a,b)
        if a>=m and nums1[a]==0:
            nums1[a]=nums2[b]
            b+=1
            a=0
            continue
        if nums1[a]<nums2[b]:
            a+=1
        else:
            nums1.insert(a,nums2[b])
            b+=1
            a=0
            del nums1[-1]
    nums1.sort()
    print(nums1)
    
mergesorted(nums1,m,nums2,n)
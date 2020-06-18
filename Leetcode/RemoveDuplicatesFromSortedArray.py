nums=list(map(int,input().split()))
if(len(nums)==0 or len(nums)==1):
    print(l)
tmp=[]
tmp.append(nums[0])
for i in range(1,len(nums)):
    print(i)
    if(nums[i]!=nums[i-1]):
        tmp.append(nums[i])
nums=tmp
for i in range(0,len(tmp)):
    print(nums)
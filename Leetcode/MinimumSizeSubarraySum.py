def minsubarray(s,nums):
    start=end=0
    length=len(nums)
    while(start!=len(nums) and end!=len(nums)):
        print("start:",start,"end",end)
        print(nums[start:end+1])
        print("sum:",sum(nums[start:end+1]))
        print("length",length)
        maximum=sum(nums[start:end+1])
        if(maximum>=s):
            if(end+1-start<length):
                length=len(nums[start:end+1])
            start+=1
        else:
            end+=1
    if(end==len(nums)):
        while(start!=len(nums)):
            print("start:",start,"end",end)
            print(nums[start:end+1])
            print("sum:",sum(nums[start:end+1]))
            print("length",length)
            maximum=sum(nums[start:end+1])
            if(maximum>=s and end+1-start<length):
                length=len(nums[start:end+1])
            start+=1
            
    if(length==len(nums)):
        if(sum(nums)<s):
            return 0
    return length
            
    
s=3
nums=[1,1]

x=minsubarray(s,nums)
x
            
        

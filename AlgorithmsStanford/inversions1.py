def sortandcount(A,left,right):
    invcount=0
    if left<right:
        mid=(left+right)//2
        invcount+=sortandcount(A,left,mid)
        invcount+=sortandcount(A,mid+1,right)
        invcount+=mergesortandcount(A,mid,left,right)
    return invcount
    
def mergesortandcount(A,mid,left,right):
    i=left
    j=mid+1
    inv=0
    while i<=mid and j<=right:
        if A[i]<=A[j]:
            i+=1
        else:
            j+=1
            inv+= (mid-i+1)
    return inv

file="IntegerArray.txt"
a=[]
with open(file) as f:
    for line in f.readlines():
        a.append(int(line))    
n=len(a)
result=sortandcount(a,0,n-1)
print(result)
        
def tempsort(a,n):
    return mergesort(a,0,n-1)

def mergesort(a,left,right):
    inv=0
    if left<right:
        mid=(left+right)//2
        inv+=mergesort(a,left,mid)
        inv+=mergesort(a,mid+1,right)
        inv+=merge(a,left,mid,right)
    return inv

def merge(a,left,mid,right):
    i=left
    j=mid+1
    inv=0
    
    while i<=mid and j<=right:
        if a[i]<=a[j]: #no inversion
            i+=1
        else:
            inv+=(mid-i)+1
            j+=1
    return inv

file="IntegerArray.txt"
a=[]
with open(file) as f:
    for line in f.readlines():
        a.append(int(line))    
n=len(a)
result=tempsort(a,n)
print(result)
def quicksort(A):
    l=0
    r=len(A)-1
    if len(A)<=1:
        return (A,0)
    p=A[l]
    i=j=l+1
    while j< len(A):
        if(A[j]>p):
            j+=1
        else:
            A[j],A[i]=A[i],A[j]
            i+=1
            j+=1
    A[0],A[i-1]=A[i-1],A[0]
    A[:i-1],nleft=quicksort(A[:i-1])
    A[i:],nright=quicksort(A[i:])
    return(A,r+nleft+nright)
    
def quicksort1(A):
    l=0
    r=len(A)-1
    if len(A)<=1:
        return (A,0)
    A[0],A[r]=A[r],A[0]
    p=A[l]
    i=j=l+1
    while j< len(A):
        if(A[j]>p):
            j+=1
        else:
            A[j],A[i]=A[i],A[j]
            i+=1
            j+=1
    A[0],A[i-1]=A[i-1],A[0]
    A[:i-1],nleft=quicksort(A[:i-1])
    A[i:],nright=quicksort(A[i:])
    return(A,r+nleft+nright)    

def quicksort2(A):
    l=0
    r=len(A)-1
    if len(A)<=1:
        return (A,0)
    mid=(l+r)//2
    ps=[a[l],a[r],a[mid]]
    x=ps.index(min(ps))
    y=ps.index(max(ps))
    for z in range(0,len(ps)):
        if z!=x and z!=y:
            sel=z
    A[0],A[sel]=A[sel],A[0]
    p=A[0]
    i=j=l+1
    while j< len(A):
        if(A[j]>p):
            j+=1
        else:
            A[j],A[i]=A[i],A[j]
            i+=1
            j+=1
    A[0],A[i-1]=A[i-1],A[0]
    A[:i-1],nleft=quicksort(A[:i-1])
    A[i:],nright=quicksort(A[i:])
    return(A,r+nleft+nright)     

file="QuickSort.txt"
a=[]
with open(file) as f:
    for line in f.readlines():
        a.append(int(line))  
result=quicksort2(a)
print(result[1])


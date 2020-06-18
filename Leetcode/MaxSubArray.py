nums=list(map(int, input().split()))
sublist=[[]]
sub=[]
for i in range(len(nums)+1):
	for j in range(i+1,len(nums)+1):
		sub=nums[i:j]
		sublist.append(sub)
sublist = sublist[1:]
print(sublist)
sums=[]
for i in sublist:
	sums.append(sum(i))
print(max(sums))
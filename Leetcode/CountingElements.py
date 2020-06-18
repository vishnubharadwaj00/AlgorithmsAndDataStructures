n=list(map(int,input().split()))
dicti={} 
for i in n:
	dicti[i]=1
print(dicti)
result=0
for x in n: 
	if(x+1 in dicti):
		result+=1
print(result)

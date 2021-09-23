def twosum(numbers,target):
	p1 = 0 
	p2 = len(numbers)-1
	while p1<p2:
		if target == numbers[p1] + numbers[p2]:
			return [p1+1,p2+1]
		elif target < numbers[p1] + numbers[p2]:
			p2-=1
		else:
			p1+=1

a = twosum([2,3,4],6)
print(a)
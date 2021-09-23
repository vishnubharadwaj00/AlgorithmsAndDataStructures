def maxprofit(prices):
	index = []
	for i in range(1,len(prices)):
		if prices[i]>prices[i-1]:
			index.append(prices[i-1])
			index.append(prices[i])
	print(index)
	if index == []:
		return 0
	return max(index)-min(index)
	

a = maxprofit([2,1,2,0,1])
print(a)


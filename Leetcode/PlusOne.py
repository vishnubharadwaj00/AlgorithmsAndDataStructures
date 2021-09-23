def plusone(digits):
	for i in reversed(range(1,len(digits))):
		if(digits[i]!=9):
			digits[i]+=1
			return digits
		digits[i]=0
	digits.insert(0,1)

a = plusone([0])
print(a)
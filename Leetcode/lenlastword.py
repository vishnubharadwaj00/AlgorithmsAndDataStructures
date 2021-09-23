def lenlastword(s):	
	point = len(s)-1
	count = 0
	while point>=0:
		if s[point]!=" ":
			count+=1
			point-=1
		else:
			break
	if count!=0:
		return count
	else:
		return 0

s = "Hello World"
print(lenlastword(s))
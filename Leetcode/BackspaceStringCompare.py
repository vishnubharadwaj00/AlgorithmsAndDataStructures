s=str(input())
t=str(input())
def backspace(s,t):
	x=list()
	y=list()
	for i in range(0,len(s)):
		if(s[i]=="#" and len(x)>0):
			x.pop()
		else:
			x.append(s[i])
	if '#' in x:
		x.remove('#')
	print(x)
	for i in range(0,len(t)):
		if(t[i]=="#" and len(y)>0):
			y.pop()
		else:
			y.append(t[i])
	if '#' in y:
		y.remove('#')
	print(y)
	if(x==y):
		return(True)
	else:
		return(False)

x=backspace(s,t)
print(x)

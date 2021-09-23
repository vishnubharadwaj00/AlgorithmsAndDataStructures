def pascal(numrows):
	out = []
	for i in range(numrows):
		lst = []
		for j in range(i+1):
			if j == 0 or j == i:
				lst.append(1)
			else:
				lst.append(out[i-1][j-1] + out[i-1][j])
		out.append(lst)

	print(out)

pascal(0)
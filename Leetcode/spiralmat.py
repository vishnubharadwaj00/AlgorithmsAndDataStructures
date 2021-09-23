def spiral(matrix):
	top = 0 
	bottom = len(matrix)-1
	left = 0 
	right = len(matrix[0]) -1
	size = len(matrix)*len(matrix[0])
	out = []
	
	while top<=bottom and left<=right:
		# TOP section: left to right
		l = left
		while l <= right:  # and left <= right: <-- we will never reach that condition
			out.append(matrix[top][l])
			l += 1
			# move lower
			# because: added all from the top area
		top += 1

			# RIGHT section: top to bottom
		t = top
		while t <= bottom:  # and top <= bottom: <-- we will never reach that condition
			out.append(matrix[t][right])
			t += 1
			# move pointer to the left
			# done with right-most section
		right -= 1

			# BOTTOM section: right to left
			# on the last of the spiral, char: right = left, therefore, r = left
			# so the while loop might run again
		r = right
		while r >= left and top <= bottom:
			out.append(matrix[bottom][r])
			r -= 1
		bottom -= 1

			# LEFT section: bottom to top
			# on the last of the spiral, char: bottom = top, therefore, b = top
			# so the while loop might run again
			# that's why we have the extra condition
		b = bottom
		while b >= top and left <= right:
			out.append(matrix[b][left])
			b -= 1
		left += 1

	return out



out=spiral([[1,2,3],[4,5,6],[7,8,9]])
print(out)
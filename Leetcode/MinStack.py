class MinStack:

	def __init__(self):
		self.stack=[]

	def push(self,x):
		self.stack.append(x)

	def pop(self):
		if len(self.stack)>0:
			self.stack.pop()

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return min(self.stack)

obj = MinStack()
obj.push(-1)
obj.push(0)
obj.push(3)
top1= obj.top()
print("Top1:",top1)
min1= obj.getMin()
print("Min1:",min1)
obj.pop()
top2= obj.top()
print("Top2:",top2)
min2 = obj.getMin()
print("Min2:",min2)
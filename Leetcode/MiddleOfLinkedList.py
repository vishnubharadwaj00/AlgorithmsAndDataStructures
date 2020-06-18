class Node:
	def __init__(self,x):
		self.x=x
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	
	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
	def getCount(self):
		temp=self.head
		count=0
		while(temp):
			count+=1
			temp=temp.next
		return count
	def getnth(self,count):
		current=self.head
		num=1
		while(current):
			print(num,count)
			if(count==num):
				temp=self.head
				temp.head=current.x
			num+=1
			current=current.next
			return temp

#if __name__=='__main__': 
llist = LinkedList() 
llist.push(1) 
llist.push(4) 
llist.push(2) 
llist.push(12) 
llist.push(3) 
x=llist.getCount()  
print(x)
if(x%2==0):
	mid=x+1/2
	mid=int(mid)
else:
	mid=x/2+1
	mid=int(mid)
print(mid)
x=llist.getnth(mid)
current=self.head
while(current):
	print(llist.data)
	current=


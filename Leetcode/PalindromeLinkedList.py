class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        c=head
        stack=[]
        while(c!=None):
            stack.append(c.val)
            c=c.next
        left=0
        right=len(stack)-1
        while(left<=right):
            if (stack[left]!=stack[right]): 
                return False
            else:
                left+=1
                right-=1
        return True
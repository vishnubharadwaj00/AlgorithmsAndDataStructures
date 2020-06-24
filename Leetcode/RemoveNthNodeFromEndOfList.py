class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        c=head
        for i in range(0,n):
            c=c.next
        prev=head
        if c==None:
            return prev.next
        while(c.next!=None):
            c=c.next
            prev=prev.next
        prev.next=prev.next.next
        return head 
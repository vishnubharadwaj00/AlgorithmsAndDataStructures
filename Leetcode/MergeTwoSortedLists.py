class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergetwolists(l1,l2):
        output=c=ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                c.next=(l1.val,None)
                l1=l1.next
            else:
                c.next=(l2.val,None)
                l2=l2.next
            c=c.next
        c.next=l1 or l2 
        return output.next
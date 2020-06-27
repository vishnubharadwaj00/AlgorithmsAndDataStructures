class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a = head
        if a:
            b = a.next
            while(b != None):
                print(a.val, b.val)
                while(b != None and a.val == b.val):
                    a.next = b.next
                    b = b.next
                if(b == None):
                    return head
                a = a.next
                b = b.next
            return head

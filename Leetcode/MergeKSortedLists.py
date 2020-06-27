class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        cur = [0]*k
        for i in range(k):
            cur[i] = lists[i]
        output = ListNode()
        head = output
        while(cur != [None]*k):
            mini = float('inf')
            index = -1
            i = 0
            while i < k:
                if(cur[i] == None):
                    cur.pop(i)
                    k -= 1
                    continue
                if cur[i].val < mini:
                    mini = cur[i].val
                    index = i
                i += 1
            output.next = ListNode(mini)
            output = output.next
            cur[index] = cur[index].next
        return head.next

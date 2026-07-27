# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0, None)

        curr = head
        while curr:
            if new_head.next is None:
                new_head.next = curr
                curr = curr.next
                new_head.next.next = None
            else:
                tmp = curr
                curr = curr.next
                tmp2 = new_head.next
                new_head.next = tmp
                tmp.next = tmp2
        
        return new_head.next
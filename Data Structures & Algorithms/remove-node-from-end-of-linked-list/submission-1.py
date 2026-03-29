# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head
        while dummy:
            count += 1
            dummy = dummy.next
        
        target = count - n

        if target==0:
            return head.next

        dummy = ListNode(0, head)
        
        while target>0:
            target -= 1
            dummy = dummy.next

        dummy.next = dummy.next.next

        return head

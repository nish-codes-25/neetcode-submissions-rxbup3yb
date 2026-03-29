# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break 
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr!=groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp

        return dummy.next

    def getKth(self, node, k):
        while node and k>0:
            node = node.next
            k -=1
        return node
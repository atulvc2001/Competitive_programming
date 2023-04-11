# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        curr = dummy
        l = 0
        while curr:
            l += 1
            curr = curr.next

        print(l - n)
        curr = dummy
        c = 0
        while curr:
            if c == (l-n-1):
                curr.next = curr.next.next
            c += 1
            curr = curr.next

        return dummy.next

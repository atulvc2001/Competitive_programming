# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        dup = head
        while head.next:
            nxt = head.next
            value = nxt.val
            if head.val != value:
                head = nxt
                dup = nxt
            head = nxt.next
            dup = nxt.next
            
        print(dup)
        return head

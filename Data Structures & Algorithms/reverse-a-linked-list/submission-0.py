# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        new=None
        while ptr:
            newnode = ListNode(ptr.val)
            newnode.next = new
            new=newnode
            ptr=ptr.next
        return new
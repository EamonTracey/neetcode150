# Given the head of a singly linked list,
# reverse the list, and return the reversed list.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new = None
        while curr is not None:
            n = curr.next
            curr.next = new
            new = curr
            curr = n

        return new


# You are given the heads of two sorted linked
# lists list1 and list2.
#
# Merge the two lists into one sorted list. The
# list should be made by splicing together the
# nodes of the first two lists.
#
# Return the head of the merged linked list.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head
        while list1 or list2:
            if list1 is None:
                curr.next = list2
                list2 = list2.next
            elif list2 is None:
                curr.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        return head


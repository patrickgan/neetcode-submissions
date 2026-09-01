# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        stack = []
        while head.next is not None:
            stack.append(head)
            head = head.next
        newHead = head
        while len(stack) > 0:
            head.next = stack.pop()
            head = head.next
        head.next = None
        return newHead
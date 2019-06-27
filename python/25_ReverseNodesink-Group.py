# Definition for singly-linked list.
# 25. Reverse Nodes in k-Group
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
      e = head
      i = 0
      if head is None or head.next is None:
        return head
      while i < k-1 and e.next is not None:
        i += 1
        e = e.next
      if i < k - 1:
        return head
      end = e.next
      e.next = None
      new_head = self.reverseList(head)
      if end is not None:
        head.next = self.reverseKGroup(end, k)
      return new_head

    def reverseList(self, head):
      new_head = head
      if head is None or head.next is None:
        return head

      newhead = self.reverseList(head.next)
      head.next.next = head
      head.next = None
      return newhead

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        #get len:
        ctr = 1
        cur = head
        while cur.next is not None:
            ctr += 1
            cur = cur.next

        if n == ctr:
            return head.next

        cur = head
        for _ in range(ctr-n-1):
            cur = cur.next
        if cur.next is not None:
            cur.next = cur.next.next
        return head

    # beats 100
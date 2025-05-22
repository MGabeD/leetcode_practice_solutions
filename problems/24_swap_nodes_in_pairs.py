# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        cur = head
        post_cur = head.next
        new_post_cur = head.next
        while True:
            if post_cur.next is None or post_cur.next.next is None:
                cur.next = post_cur.next
                post_cur.next = cur
                return new_post_cur
            else:
                cur.next = post_cur.next.next
                cp = post_cur.next
                post_cur.next = cur
                post_cur = cur.next
                cur = cp

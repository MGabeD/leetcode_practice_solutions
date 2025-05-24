# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # this feels like an extension of a previous problem. Its a good bit trickier
        # feels liek the same rough approach though

        if head is None or k == 1:
            return head
        cur = head
        ctr = 0
        post_cur = head
        while ctr < k - 1:
            post_cur = post_cur.next
            ctr += 1
            if post_cur is None:
                return head
        new_head = post_cur
        while True:
            tmp = cur
            tmp1 = cur.next
            for _ in range(k - 1):
                foo = tmp1.next
                tmp1.next = tmp
                tmp = tmp1
                tmp1 = foo
            post_cur = tmp1
            ctr = 0
            if post_cur is None:
                cur.next = None
                return new_head
            while ctr < k - 1:
                post_cur = post_cur.next
                ctr += 1
                if post_cur is None:
                    cur.next = tmp1
                    return new_head
            cur.next = post_cur
            cur = tmp1
# I killed this low key - beats 100% got it really really quick
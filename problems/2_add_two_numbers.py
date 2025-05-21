# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = 0
        if l1 is not None:
            cur += l1.val
            l1 = l1.next
        if l2 is not None:
            cur += l2.val
            l2 = l2.next
        head = ListNode(val=cur%10, next=None)
        cur_node = head
        cur = cur // 10
        while l1 is not None or l2 is not None or cur != 0:
            if l1 is not None:
                cur += l1.val
                l1 = l1.next
            if l2 is not None:
                cur += l2.val
                l2 = l2.next
            cur_node.next = ListNode(val=cur % 10, next=None)
            cur_node = cur_node.next
            cur = cur // 10
        return head

        # the submissions ahve massive variance - beating 74 % right now and not worth chasing the lst bit


l1 = l1.next

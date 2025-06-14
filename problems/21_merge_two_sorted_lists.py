# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        cur = head
        while list1 is not None or list2 is not None:
            if list1 is not None:
                if list2 is not None:
                    if list1.val < list2.val:
                        cur.next = list1
                        list1 = list1.next
                        cur = cur.next
                    else:
                        cur.next = list2
                        list2 = list2.next
                        cur = cur.next
                else:
                    cur.next = list1
                    break
            else:
                cur.next = list2
                break
        return head
# beat 100%

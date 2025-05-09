# Another problem for today for fun
from ctypes.wintypes import tagPOINT

from macholib.mach_o import fat_arch


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if head is None:
        #     return head
        # cur = head
        # arr = []
        # while cur.next is not None:
        #     arr.append(cur.val)
        #     cur = cur.next
        # arr.append(cur.val)
        # incrementer = 0
        # for i in range(len(arr) - 1, -1, -1):
        #     if arr[i] > incrementer:
        #         incrementer = arr[i]
        #     else:
        #         arr[i] = incrementer
        # icc = 0
        # new_head = head
        # recreate = None
        # cur = head
        # while cur.next is not None:
        #     if arr[icc] > cur.val:
        #         cur = cur.next
        #     else:
        #         if recreate is not None:
        #             recreate.next = cur
        #             recreate = recreate.next
        #         else:
        #             new_head = cur
        #             recreate = cur
        #         cur = cur.next
        #         recreate.next=None
        #     icc += 1
        # recreate.next = cur
        # return new_head
    # obv the right algo but cna be faster....
    # I didn't want to write a reversal but 3n vs n+2m is faster NOTE WE ARE NOT BIG O notation I am already same on that
    #  speed. Switching to tan array above makes it marginally faster than the while loop but doesn;t make up the 2n vs 2m
    # I am going to do the reversal and see if it is indeed faster
        if head is None or head.next is None:
            return head

        # reverse
        tmp_head = reverse(head)
        tmp = tmp_head
        max_val = 0
        prev = None
        while tmp:
            if tmp.val < max_val:
                # drops node
                after = tmp.next
                prev.next=after
                tmp=after
            else:
                # Keep node
                max_val = tmp.val
                prev=tmp
                tmp=tmp.next
        return reverse(tmp_head)

def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

# I am still not the fastest way posisble. I think this may be fiunctino overheads or comparisons. But i think this is
# fine I am happy with 97% here. I can  be done with this for today. An easy optimization is to drop the reverse
# function and to hard code it. Will drop 2 function call overheads but its not a huge diff...
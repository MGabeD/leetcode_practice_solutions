import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # head = ListNode(0)
        # cur = head
        # while len(lists) > 0:
        #     min_val = None
        #     alive = []
        #     secondary = None
        #     for val in lists:
        #         if val is None:
        #             continue
        #         if min_val is None:
        #             min_val = len(alive)
        #         elif val.val <= alive[min_val].val:
        #             secondary = min_val
        #             min_val = len(alive)
        #         elif secondary is None or val.val < alive[secondary].val:
        #             secondary = len(alive)
        #         alive.append(val)
        #     if min_val is None:
        #         return head.next
        #     cur.next = alive[min_val]
        #     cur = cur.next
        #     while cur.next is not None and (secondary is None or cur.next.val <= alive[secondary].val):
        #         cur = cur.next
        #     alive[min_val] = cur.next
        #     lists = alive
        # return head.next
        # This was slow. realy slow - was niave and didn't really think through solutions

        # maybe minheap
        min_heap = []

        for i,val in enumerate(lists):
            if val:
                min_heap.append((val.val, i, val))
        heapq.heapify(min_heap)

        dummy = prev = ListNode(0)
        while min_heap:
            _,idx, node = heapq.heappop(min_heap)
            prev.next = node
            prev = prev.next
            if node.next is not None:
                heapq.heappush(min_heap,(node.next.val,idx,node.next))
        return dummy.next

# looks like there were two fast enoughsolutions a merge sort using 21's solution or a min heap... I kinda failed this
# one on my first try i am kind of dissapointed in myself... it is what it is but I should do better
# Beats 96%  though :)

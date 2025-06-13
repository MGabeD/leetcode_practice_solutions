class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # i = m-1
        # j = n-1
        # a = m+n -1
        # while j >= 0:
        #     if i >= 0 and nums1[i] > nums2[j]:
        #         nums1[a] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[a] = nums2[j]
        #         j -= 1
        #     a -= 1
        # I actually didn't get fast on an easy ughhhh - minor improvements I can make
        a = m+n-1
        while m > 0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                m -= 1
                nums1[a] = nums1[m]
            else:
                n -= 1
                nums1[a] = nums2[n]
            a -= 1

        while n > 0 :
            nums1[a] = nums2[n-1]
            a -= 1
            n -= 1
        

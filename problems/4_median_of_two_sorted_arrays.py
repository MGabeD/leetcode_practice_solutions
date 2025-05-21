from bisect import bisect_left, bisect_right

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0:
            if len(nums2) == 0:
                return 0
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2-1] + nums2[len(nums2) // 2])/2.0
            return nums2[len(nums2) // 2]

        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2-1] + nums1[len(nums1) // 2])/2.0
            return nums1[len(nums1) // 2]

        two_vals = (len(nums1) + len(nums2))% 2 == 0
        bottom_of_range = (len(nums1) + len(nums2)) //2 + (0 if two_vals else 1)
        bottom = 0
        top = len(nums1)-1
        cur = 0
        middle = 0
        below = 0
        while True:
            while bottom <= top:
                middle = (bottom+top) // 2
                # above = len(nums1)-1 - mid
                below = middle+1
                cur = bisect_left(nums2, nums1[middle])
                below += cur
                # above += len(nums2)-1 -cur
                if below < bottom_of_range:
                    bottom = middle + 1
                elif below > bottom_of_range:
                    top = middle -1
                else:
                    break

            need_to_go_x_deeper = bottom_of_range-below

            if not two_vals:
                if need_to_go_x_deeper == 0:
                    if cur-1 < 0:
                        return nums1[middle]
                    return max(nums1[middle], nums2[cur-1])
                if need_to_go_x_deeper > 0:
                    return nums2[cur+need_to_go_x_deeper-1]
                if need_to_go_x_deeper < 0:
                    return nums2[cur+need_to_go_x_deeper]

            if need_to_go_x_deeper < 0:
                if cur+need_to_go_x_deeper+1 >= len(nums2):
                    return (nums2[cur+need_to_go_x_deeper] + nums1[middle])/2.0
                return (nums2[cur+need_to_go_x_deeper] + min(nums1[middle], nums2[cur+need_to_go_x_deeper+1])) / 2.0
            elif need_to_go_x_deeper > 0:
                if middle + 1 >= len(nums1):
                    return (nums2[cur+need_to_go_x_deeper-1] + nums2[cur+need_to_go_x_deeper]) /2.0
                if cur + need_to_go_x_deeper >= len(nums2):
                    return (nums2[cur + need_to_go_x_deeper - 1] + nums1[middle+1]) / 2.0
                return (nums2[cur+need_to_go_x_deeper-1] + min(nums1[middle+1], nums2[cur+need_to_go_x_deeper])) /2.0
            else:
                if middle+1 >= len(nums1):
                    return (nums1[middle] + nums2[cur]) /2.0
                if cur < len(nums2) and nums1[middle] <= nums2[cur]:
                    return (nums1[middle] +min(nums1[middle+1], nums2[cur])) /2.0
                else:
                    return (nums1[middle] + nums1[middle + 1]) / 2.0

        # I cna totally make this simpler I dove into my habit of if else treeing - kind of bad of me. I beat average on
#        first attempt algo though so I wil take it!

        # I looked at some other answers and missed a major jump to make it a bit fster... i did well enough with my
        # hacky solution to not want to redo it but damn...
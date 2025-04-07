# class MajorityChecker(object):
#
#     def __init__(self, arr):
#         """
#         :type arr: List[int]
#         """
#         self.arr = arr
#
#     def query(self, left, right, threshold):
#         """
#         :type left: int
#         :type right: int
#         :type threshold: int
#         :rtype: int
#         """
#         data = {}
#         for i in range(left, right+1):
#             data[self.arr[i]] = data.get(self.arr[i],0) + 1
#             if data[self.arr[i]] >= threshold:
#                 return self.arr[i]
#         return -1
#

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

# This solution works but is O(n) there is likely something faster with pre-computing - lets try!


# class MajorityChecker(object):
#
#     def __init__(self, arr):
#         """
#         :type arr: List[int]
#         """
#         self.sorted_idx = {}
#         for i in range(0, len(arr)):
#             self.sorted_idx.setdefault(arr[i],[]).append(i)
#
#     def query(self, left, right, threshold):
#         """
#         :type left: int
#         :type right: int
#         :type threshold: int
#         :rtype: int
#         """
#         for k,v in self.sorted_idx.items():
#             if len(v) < threshold:
#                 continue
#             find_left = implementing_binary_search(v, left)
#             find_right = implementing_binary_search(v, right)
#             if find_left[0] == 0:
#                 left_idx = find_left[1]
#             else:
#                 left_idx = find_left[1]+1
#             right_idx = find_right[1]
#             if right_idx - left_idx + 1 >= threshold:
#                 return k
#         return -1
#
#
# def implementing_binary_search(arr, target):
#     top = len(arr) - 1
#     bottom = 0
#     cur = top//2
#     while bottom <= top:
#         if arr[cur] < target:
#             bottom = cur + 1
#         elif arr[cur] > target:
#             top = cur - 1
#         else:
#             return 0, cur
#         cur = (top+bottom)//2
#     return -1, cur
#
#
# tester = MajorityChecker(arr = [1,1,2,2,1,1])
# print(tester.query(0,5,4))

# Somehow this is still too slow for leet code.. need to think O(M*log(n)) still not fast enough - better than O(n)

# I guess I need to shrink the amount of times I am trying this. Limiting to possible answers is not fast enough in
# really large sets so maybe by sampling?

# 0.5^20 ~= 1 in 100 million false negative ~ prob good enough for leetcode - is imperfect but with margin
# can also add a caching for pre-computed values in a dict -> o(1) retrieval - much faster - burns memory space but
# should be a good optimization
# if under 39 might as well iterate through all of them as avg case better since no chance of repetition


import random


class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.arr = arr
        self.sorted_idx = {}
        self.max_reps = 0
        for i in range(0, len(arr)):
            self.sorted_idx.setdefault(arr[i], []).append(i)
        for k, v in self.sorted_idx.items():
            if len(v) > self.max_reps:
                self.max_reps = len(v)
        self.pre_computed = {}

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        result = self.pre_computed.get((left, right, threshold))
        if result is not None:
            return result
        if threshold > self.max_reps:
            return -1
        if right - left < 39:
            seen = set()
            for i in range(left, right + 1):
                if self.arr[i] in seen:
                    continue
                seen.add(self.arr[i])
                find_left = implementing_binary_search(self.sorted_idx[self.arr[i]], left)
                find_right = implementing_binary_search(self.sorted_idx[self.arr[i]], right)
                if find_left[0] == 0:
                    left_idx = find_left[1]
                else:
                    left_idx = find_left[1] + 1
                right_idx = find_right[1]
                if right_idx - left_idx + 1 >= threshold:
                    self.pre_computed[(left, right, threshold)] = self.arr[i]
                    return self.arr[i]
        seen = set()
        for _ in range(0, 20):
            rand_idx = random.randint(left, right)
            if self.arr[rand_idx] in seen:
                continue
            seen.add(self.arr[rand_idx])
            find_left = implementing_binary_search(self.sorted_idx[self.arr[rand_idx]], left)
            find_right = implementing_binary_search(self.sorted_idx[self.arr[rand_idx]], right)
            if find_left[0] == 0:
                left_idx = find_left[1]
            else:
                left_idx = find_left[1] + 1
            right_idx = find_right[1]
            if right_idx - left_idx + 1 >= threshold:
                self.pre_computed[(left, right, threshold)] = self.arr[rand_idx]
                return self.arr[rand_idx]
        return -1


def implementing_binary_search(arr, target):
    top = len(arr) - 1
    bottom = 0
    cur = top // 2
    while bottom <= top:
        if arr[cur] < target:
            bottom = cur + 1
        elif arr[cur] > target:
            top = cur - 1
        else:
            return 0, cur
        cur = (top + bottom) // 2
    return -1, cur


tester = MajorityChecker(arr = [1,1,2,2,1,1])
print(tester.query(0,5,4))



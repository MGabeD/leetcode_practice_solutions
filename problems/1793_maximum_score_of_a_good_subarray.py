
def maximumScore(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # we are given k >= 0 so no need to guard this here

    # so we can approach this with a few quick assumptions we can find some shortcuts
    # start with min(i, ..., k) walking back from k
    # start with min(k, ..., j) walking forward from k

    # what we now want to find is a way to minimize the computations to evaluate min(i,j) * (j-i +1)
    # this gives us a batching where we ALWAYS want the max j when min(k,j) is the same and the min i when min(i,k)
    #
    # current_min_ik = [[nums[k], k]]
    # current_min_ik is value, min idx
    # for i in range(0,k+1):
        # if current_min_ik[-1][0] <= nums[k-i]:
        #     current_min_ik[-1][1] = k-i
        # else:
        #     current_min_ik.append([nums[k-i], k-i])
    #
    # current_min_kj = [[nums[k], k]]
    # for i in range(k, len(nums)):
    #     if current_min_kj[-1][0] <= nums[i]:
    #         current_min_kj[-1][1] = i
    #     else:
    #         current_min_kj.append([nums[i],i])

    # so now i want the largest possible J and the smallest possible I for the biggest min(I->J)
    # I have precomputed the two halves of this problem and can get
    # max_val = 0
    # for cur_i in current_min_ik:
    #     i_value = cur_i[0]
    #     i_idx = cur_i[1]
    #     for cur_j in current_min_kj:
    #         j_val = cur_j[0]
    #         j_idx = cur_j[1]
    #         max_val = max(max_val, min(i_value, j_val) * (j_idx-i_idx+1))
    # return max_val
    # This works but I think I can be more efficient - there will be conditions where we can shortcut this
    # for example when can we just disqualify all future data if cur_max > len(nums) * cur min -> skip all finding of rest
    # max_val = 0
    # for cur_i in current_min_ik:
    #     i_value = cur_i[0]
    #     i_idx = cur_i[1]
    #     if cur_i[0] * (len(nums)-cur_i[1]) <= max_val:
    #         continue
    #     for cur_j in current_min_kj:
    #         j_val = cur_j[0]
    #         j_idx = cur_j[1]
    #         if j_val * (len(nums)-cur_i[1]) <= max_val:
    #             break
    #         max_val = max(max_val, min(i_value, j_val) * (j_idx-i_idx+1))
    # return max_val

    # This is still too slow... there must be something I am missing - lets try seeing if there can be an optimization
    # to skip all of the iterations through -> i am getting an o(n^2) with both of these approaches and while the above
    # approach will drop a ton of time it isn't important in big O and I need something to drop from n^2 to log(n) * n
    # or O(n) so I am looking for something greedy or binary search related

    # attempt at greedy

    # initializing my starting point
    n = len(nums)
    left = right = k
    min_score = nums[k]
    max_score = nums[k]
    while left > 0 or right < n - 1:
        if left == 0:
            right += 1
        elif right == n-1:
            left -= 1
        elif nums[left-1] > nums[right+1]:
            left -= 1
        else:
            right += 1
        min_score = min(min_score, nums[right], nums[left])
        max_score = max(max_score, min_score * (right-left+1))

    return max_score

    # Can't believe I missed an O(n) that wasn't even hard. I should've done better than that. Lesson for the future
    # spend more time expanding on the idea of safe assumptions to find a better way of doing it. I almost made it to
    # this in my writing at the top but was stuck on turning it into two arrays and using the tell tail assumption it
    # was a greedy algo to try to optimize the array to be smaller. I should in the future see if and how my assumptions
    # I am finding can be used for other algorithms




maximumScore(nums=[1,4,3,7,4,5], k=3)


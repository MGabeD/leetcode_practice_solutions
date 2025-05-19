from bisect import bisect_left, bisect_right


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # I am struggling to wrap my brain around this one for some reason
        # so lets just make a slow version first
        # data = {}
        # for i in nums:
        #     if i in data:
        #         data[i] += 1
        #     else:
        #         data[i] =1
        # vals = sorted(data)
        # if data[vals[0]] > 2:
        #     closest = vals[0] * 3
        # elif data[vals[0]] > 1:
        #     closest = vals[0]*2 + vals[1]
        # else:
        #     if data[vals[1]] > 1:
        #         closest =vals[0] + vals[1]*2
        #     else:
        #         closest = vals[0] + vals[1] + vals[2]
        # to_beat = abs(target-closest)
        # for i, num in enumerate(vals):
        #     iter1 = i+1
        #     if data[num] > 1:
        #         iter1 = i
        #     for j, num2 in enumerate(vals[iter1:]):
        #         floor_val = iter1+j if data[num2] > 1 and (num != num2 or data[num2] > 2) else iter1+j+1
        #         if floor_val == len(vals):
        #             break
        #         if target - num - num2 <= vals[floor_val]:
        #             if target - num - num2 == vals[floor_val]:
        #                 return target
        #             elif target - num - num2 < num2 and to_beat <= abs(target-num-num2-vals[floor_val]):
        #                 break
        #         left = bisect.bisect_right(vals, target-(num+num2))
        #         if left < floor_val:
        #             left = floor_val
        #         if left < len(vals):
        #             cur = vals[left] + num + num2
        #             if abs(target-cur) < to_beat:
        #                 if cur == target:
        #                     return target
        #                 to_beat = abs(target-cur)
        #                 closest = cur
        #         if left > 0 and left > floor_val:
        #             cur = vals[left-1] + num + num2
        #             if abs(target - cur) < to_beat:
        #                 if cur == target:
        #                     return target
        #                 to_beat = abs(target - cur)
        #                 closest = cur
        #
        # return closest
        # NOW lets simplify this guy
        data = {}
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        vals = sorted(data)
        if data[vals[0]] > 2:
            closest = vals[0] * 3
        elif data[vals[0]] > 1:
            closest = vals[0] * 2 + vals[1]
        else:
            if data[vals[1]] > 1:
                closest = vals[0] + vals[1] * 2
            else:
                closest = vals[0] + vals[1] + vals[2]
        max_val = (vals[-1] +
                  (vals[-1] if data[vals[-1]] > 1 else vals[-2]) +
                  (vals[-1] if data[vals[-1]] > 2 else vals[-2] if data[vals[-1]] >1 or data[vals[-2]] >1 else vals[-3]))
        if max_val < target:
            return max_val
        min_val = (vals[0] +
                  (vals[0] if data[vals[0]] > 1 else vals[1]) +
                  (vals[0] if data[vals[0]] > 2 else vals[1] if data[vals[0]] >1 or data[vals[1]] >1 else vals[2]))
        if min_val > target:
            return closest
        to_beat = abs(target - closest)
        for i, num in enumerate(vals):
            # How to not infinitely iterate once the problem is known to be imposisble too solve better..
            if target > num + 2*vals[-1]:
                continue
            if target < num + 2*vals[0]:
                continue


            #How can I find the bottom and top of the range I wnat ot query with this value. since I only get 2 more
            # values I need to make my left most point the bisect left of target-num-vals[-1]
            # whereas the right value needs to be target-num-vals[iter]
            left = bisect_left(vals, target-(num+vals[-1]))-1
            if left < i+1:
                if data[num] > 1:
                    if left < i:
                        left =i
                else:
                    left = i+1
            right = bisect_right(vals, target-(num+vals[0]))
            for j, num2 in enumerate(vals[left:right]):
                floor_val = left +j if data[num2] > 1 and (num != num2 or data[num2] > 2) else left+j+1
                if floor_val == len(vals):
                    break
                internal_left = bisect_right(vals, target-num-num2)
                if internal_left < floor_val:
                    internal_left = floor_val
                if internal_left < len(vals):
                    cur = vals[internal_left] + num + num2
                    if abs(target - cur) < to_beat:
                        if cur == target:
                            return target
                        to_beat = abs(target - cur)
                        closest = cur
                if internal_left > 0 and internal_left> floor_val:
                    cur = vals[internal_left- 1] + num + num2
                    if abs(target - cur) < to_beat:
                        if cur == target:
                            return target
                        to_beat = abs(target - cur)
                        closest = cur


        return closest

    # I simplified it then added every fast escape. I unfortunately took forever to get them all working right but did
#     get an interation beating ~60% in ~30 min then this version ^ 99.65% in ~hr - I kept making typos




sol = Solution()
# print(sol.threeSumClosest([558,316,-411,160,801,568,-124,-589,32,897,-33,-767,-528,-180,916,813,351,642,-373,-919,666,973,-165,831,-67,-934,-659,-18,273,201,728,988,-926,409,-573,575,-502,745,724,989,-464,903,975,980,824,-197,-261,-761,966,799,-379,96,9,-680,-15,476,220,-647,365,518,-479,-443,337,-364,968,-617,862,-281,-936,-526,196,829,-191,643,-473,557,-870,553,-506,774,784,-344,-452,510,219,-785,-1,711,-759,-830,10,612,-450,-784,53,976,-314,-908,463,-408,-846,261,689,-856,-687,-949,-163,-621,-233,847,-682,-805,-711,286,40,-831,-12,952,-878,-226,739,11,-342,74,-933,-770,-840,265,702,572,-453,-295,704,-249,-835,191,404,984,-820,321,632,-689,285,-877,-643,-451,-625,84,889,620,-658,861,-397,-952,695,-386,31,827,-539,-350,588,846,-142,314,909,937,625,-230,-553,403,-763,413,904,-994,272,-426,104,-715,-159,-270,716,819,806,891,-47,-100,440,-339,918,-577,508,-554,-478,120,-943,25,-600,-626,336,-567,473,531,195,-259,-267,-883,450,170,733,491,602], -8224))
# print(sol.threeSumClosest([-1,2,1,-4],1))
# print(sol.threeSumClosest([1,1,1,0],100))
# print(sol.threeSumClosest([2,3,8,9,10],16))
print(sol.threeSumClosest([40,-53,36,89,-38,-51,80,11,-10,76,-30,46,-39,-15,4,72,83,-25,33,-69,-73,-100,-23,-37,-13,-62,-26,-54,36,-84,-65,-51,11,98,-21,49,51,78,-58,-40,95,-81,41,-17,-70,83,-88,-14,-75,-10,-44,-21,6,68,-81,-1,41,-61,-82,-24,45,19,6,-98,11,9,-66,50,-97,-2,58,17,51,-13,88,-16,-77,31,35,98,-2,0,-70,6,-34,-8,78,22,-1,-93,-39,-88,-77,-65,80,91,35,-15,7,-37,-96,65,3,33,-22,60,1,76,-32,22], 292))
# print(sol.threeSumClosest([-100,-98,-2,-1], -101))
# print(sol.threeSumClosest([1,1,1,5,5,5,5,5,5,5,5],14))

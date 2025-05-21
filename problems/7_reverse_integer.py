

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        data = []
        inv = x < 0
        x = abs(x)
        while x > 0:
            data.append(x%10)
            x = x //10

        if len(data) == 10:
            safe = False
            if inv:
                mx = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
            else:
                mx = [2,1,4,7,4,8,3,6,4,7]
            ret = 0
            for i in range(0, len(data)):
                if not safe:
                    if data[i] > mx[i]:
                        return 0
                    elif data[i] < mx[i]:
                        safe = True
                ret *= 10
                ret += data[i]
            return ret * (-1 if inv else 1)
        elif len(data) >= 10:
            return 0
        else:
            ret = 0
            for i in data:
                ret *= 10
                ret += i
            return ret * (-1 if inv else 1)
#         beat 60% happy enoough for now
#
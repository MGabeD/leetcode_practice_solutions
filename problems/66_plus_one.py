class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]+= 1
        carry = digits[-1]//10
        digits[-1] = digits[-1]%10
        cur = 1
        size = len(digits)
        while carry > 0:
            cur += 1
            if cur > size:
                return [carry]+digits
            digits[-cur] += carry
            carry = digits[-cur]//10
            digits[-cur] = digits[-cur]%10
        return digits

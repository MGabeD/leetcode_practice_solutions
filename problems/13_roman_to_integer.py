class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {
            "I":1,
            "V":5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ctr = 0
        ptr = 0
        while ptr < len(s)-1:
            if romans[s[ptr]] < romans[s[ptr+1]]:
                ctr += romans[s[ptr+1]]-romans[s[ptr]]
                ptr +=2
            else:
                ctr += romans[s[ptr]]
                ptr += 1
        if ptr != len(s):
            ctr += romans[s[ptr]]
        return ctr

    # beats 93% going to leave it for now
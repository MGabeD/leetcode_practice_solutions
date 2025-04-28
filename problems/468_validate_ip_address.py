# Backfill question for 4/21

class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        # Hmm this one is more fun than the last one. Lets start with thinking about the flow. if it contains a : its
        # IPV6 if a . then IPv4. Thus checking for ipv4 is faster then splitting. IPv4 only need to check the first 3

        dist_substr = queryIP[0:4]
        if "." not in dist_substr:
            return solve_IPv6(queryIP)
        else:
            return solve_IPv4(queryIP)


def solve_IPv4(queryIP):
    pts = queryIP.split(".")
    if len(pts) != 4:
        return "Neither"
    for i in pts:
        if not i or not i.isdigit():
            return "Neither"
        if len(i) > 1 and i[0] == "0":
            return "Neither"
        if int(i) > 255 or int(i) < 0:
            return "Neither"
    return "IPv4"


def solve_IPv6(queryIP):
    pts = queryIP.split(":")
    if len(pts) != 8:
        return "Neither"
    hex_chars = set('0123456789abcdefABCDEF')
    for i in pts:
        if not i or len(i) > 4:
            return "Neither"
        for j in i:
            if j not in hex_chars:
                return "Neither"
    return "IPv6"

sol =Solution()
print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))

# I over optimized... all of these are 0ms on leetcode so I have no idea if I actually did good optimizations. Kind
# of dissapointed in leetcode for not having better testing.... Got it right though and I like my method. I bet I did
# inefficient things though...
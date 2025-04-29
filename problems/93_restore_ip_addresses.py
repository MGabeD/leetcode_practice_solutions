class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        return recurse_down(0, s)

def recurse_down(loc, remaining_str):
    ips = []
    if loc == 3:
        if 3 >= len(remaining_str) >= 1:
            if len(remaining_str) > 1 and (remaining_str[0] == "0" or int(remaining_str) > 255):
                return []
            return [remaining_str]
        else:
            print("THIS SHOULD NEVER HAPPEN")
            return [remaining_str]
    start = max(len(remaining_str)-3*(3-loc), 1)
    top = min(4, len(remaining_str)-(3-loc)+1)
    for i in range(max(len(remaining_str)-3*(3-loc), 1), min(4, len(remaining_str)-(3-loc)+1)):
        intermed = remaining_str[:i]
        if len(intermed) > 1 and (intermed[0] == "0" or int(intermed) > 255):
            continue

        for j in recurse_down(loc+1, remaining_str[i:]):
            ips.append(intermed+"."+j)

    return ips


sol = Solution()
print(sol.restoreIpAddresses("25525511135"))
print(sol.restoreIpAddresses("0000"))
print(sol.restoreIpAddresses("101023"))

# This already beats 100% but can be alittle more efficient. I don;t think it will matter for since leetcode thinks 0ms
# already. TO make faster cut the extra ifs with the guards (they never happen so why check) - mild improvement - I feel
# like the way I am doing the j in recurse ... can also be faster with an inbuilt something - prob a join... again not
# going to do any of this since I already am beating 100%



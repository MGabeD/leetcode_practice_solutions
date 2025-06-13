class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        data = path.split('/')
        cur_path = []
        for i in data:
            if i:
                if i == ".":
                    continue
                elif i == "..":
                    if cur_path:
                        cur_path.pop()
                else:
                    cur_path.append(i)

        return "/"+'/'.join(cur_path)


sol = Solution()
print(sol.simplifyPath("/foo/foo//bar///"))
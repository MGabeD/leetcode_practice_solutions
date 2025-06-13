class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        def search(i,j,target):
            if target == len(word):
                return True
            if 0 > i or i >= len(board) or 0 > j or j >= len(board[0]) or (i,j) in visited:
                return False
            if board[i][j] != word[target]:
                return False
            visited.add((i,j))
            solutions = search(i,j+1,target+1) or search(i,j-1,target+1) or search(i-1,j,target+1) or search(i+1,j,target+1)
            visited.remove((i,j))
            return solutions

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i,j, 0):
                        return True
        return False

sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
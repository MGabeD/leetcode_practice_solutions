class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # I can get this through a single interation, each continuation x will be coming from left or up. So if
        # for condition v == 0 and not v' - 1 if v'>0 =='x' then true
        # count_ships = 0
        # for i in range(0,len(board)):
        #     for j in range(0, len(board[0])):
        #         if board[i][j] == "X":
        #             if j > 0 and board[i][j-1] == "X":
        #                 continue
        #             if i > 0 and board[i-1][j] == "X":
        #                 continue
        #             count_ships +=1
        #
        #
        # return count_ships

    # Somehow this can be faster? maybe a better if structure??? is worse for readability but may be more performant

        count_ships = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == "X" and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count_ships += 1
        return count_ships

        # pretty sure it was actually just randomness fo their testing. Ran this bottom version 2x got two different
        # times - beating 100% but ehh I think the first approach is prob worse on runtime but nicer to read (for me)

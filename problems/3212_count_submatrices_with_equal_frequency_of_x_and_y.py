class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ctr= 0
        data = [[0,0] for _ in range(len(grid[0]))]
        for i in range(0, len(grid)):
            cur_row = [0,0]
            for j in range(0, len(grid[0])):
                if grid[i][j] == "X":
                    cur_row[0] +=1
                if grid[i][j] == "Y":
                    cur_row[1] +=1

                data[j][0] = data[j][0] + cur_row[0]
                data[j][1] = data[j][1] + cur_row[1]
                if data[j][0] == data[j][1] and data[j][0] > 0:
                    ctr += 1

        return ctr

# FFS I am low key cracked lmfao - I did two versions 1) stored all the grid as cached prev data - passed my tests -
# didnt submit -> cut to just storign the last row since it was all i needed -> beat 100% :)


sol = Solution()
print(sol.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))

# reflection -> things I did well - i thought of the subproblem quite quickly and well. I am proud of building this
# instinct out since it is making these problems easier and faster. I am also seeing this have good reflections in my
# actual code as well (even if it isn't publiicly visible) | outside of that I think that me jumping into making the
# quick solution before trying to optimize is quite helpful as it lets me churn without realizing I am doing that work
# to have the simple version faster -> helps scope the problem by seeing what I am actually interacting with. This is
# something that I should work on getting better at in the first pass but this behavior is solving the major issue with
# this. I have also noticed this is easier to do without writing a easy solution is easier to do without having
# distractions (IE I was listening to youtube while doing this one...)

# things I can improve on - i love if trees as my brain spits out deep conditionals - I should spend more time
# simplifying these before my first run - sometimes they are unnecessary - I don't have evidence of this above since I
# only did one submisison but I did 2 rounds of simplifications before this submission - these should be istant so I
# don't build up this "debt" of these

# Also holy ***** i need to fix my typing - my right hand is jumping around again and missing keys and tilting in- I \
# think i need a different keyboard / fix my posture / get a split one since my wrists are turning in and my right hand
# is compensating by giving y & u & 7 & 6 to my middle finger... it is really slowing me down and making it harder to
# code since it is breaking flow now tthat I have realized it. I have been getting these weird cramps in my palm and
# this morning looked into why - found this and now I can't unsee it. when did I develop this.
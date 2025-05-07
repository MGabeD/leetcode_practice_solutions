# backfill for 5/1
from collections import defaultdict

class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # The first thing I did was too look for different methods for doing this - then I relized that this is locked
        # to a 3x3 grid. And that the amount of stones will always b 9. Thus, I am seeing two routes I need to evaluate
        # for each spot with > 1 find the closest ones to fill and create a list of them for each one.
        # the other route I instantly see is to find the closest one that can fill each of the locations.
        # In general since we are using a 3x3 we have three real cases to consider
        # x 1 2
        # 1 2 3
        # 2 3 4

        # 1 2 3
        # x 1 2
        # 1 2 3

        # 2 1 2
        # 1 x 1
        # 2 1 2

        # Seeing these cases I am seeing something which could work with a greedy algorithm where I start with corner
        # locations and focus on filling my edges first since I have a favorable access to them in comparison to other
        # donors. not sure if this is optimal but would make each decision of where to go in o(1) for each donor per
        # turn which is fantastic for me - but will it always find the minimal turn amount?

        # imagine the case
        # x 0 0
        # 0 0 0
        # 0 y 0
        # if i prioritize the corner target to fill sides I run to
        # x 1 0
        # 1 0 0
        # 0 y 0
        # before y gets a role, if I then target
        # I see the problem - there is no fast way for y to decide what to fill if it has less than 2 values. its obv
        # it should target the bottom left corner but that requires a compute of who is closest. If I fill the wrong one
        # I am in big trouble. I think the way to do this is actually to get the turn by turn closest and second closest
        # fill with that priority
        #
        # def compute_best_options(take, give):
        #     givers = defaultdict(list)
        #     acc_data = {}
        #     for k, v in take.items():
        #         min_val = 0
        #         for i in v:
        #             if i[1] in give:
        #                 min_val = i[0]
        #                 break
        #         ctr = 0
        #         ctr2 = 0
        #         delta = 0
        #         total_fallback = 0
        #         for i in v:
        #             if i[1] in give and i[0] == min_val:
        #                 givers[i[1]].append(k)
        #                 ctr += 1
        #             if i[1] in give and i[0] != min_val:
        #                 if delta == 0:
        #                     total_fallback += grid[i[1][0]][i[1][1]]
        #                     ctr2 += 1
        #                     delta = abs(min_val - i[0])
        #                 elif abs(min_val - i[0]) == delta:
        #                     total_fallback += grid[i[1][0]][i[1][1]]
        #                     ctr2 += 1
        #                 else:
        #                     break
        #         acc_data[k] = [ctr, delta, min_val, ctr2, total_fallback]
        #     return givers, acc_data
        #
        # turns = 0
        # acceptors = {}
        # donors = set()
        # for i in range(0, len(grid)):
        #     for j in range(0, len(grid[i])):
        #         if grid[i][j] > 1:
        #             donors.add((i, j))
        #         elif grid[i][j] == 0:
        #             acceptors[(i,j)] = []
        #
        # for key in acceptors.keys():
        #     data = sorted(
        #         ((abs(key[0] - donor[0]) + abs(key[1] - donor[1]), donor) for donor in donors),
        #         key=lambda x: x[0]
        #     )
        #     acceptors[key] = data
        #
        # while len(acceptors) > 0:
        #     donor_data, accept_data =compute_best_options(acceptors, donors)
        #     sorted_donor_data = sorted(
        #         donor_data.items(),
        #         key=lambda x: (
        #             len(x[1]),
        #             min(accept_data[acceptor][0] for acceptor in x[1]),
        #             max(accept_data[acceptor][1] for acceptor in x[1])
        #         )
        #     )
        #
        #     sorted_donor_data = [
        #         (
        #             donor,
        #             sorted(need_increments, key=lambda a: (accept_data[a][0], -accept_data[a][1], accept_data[a][3], accept_data[a][4]))
        #         )
        #         for donor, need_increments in sorted_donor_data
        #     ]
        #     escape = False
        #     for i in sorted_donor_data:
        #         if escape:
        #             break
        #         for k in i[1]:
        #             if k not in acceptors:
        #                 continue
        #             turns += accept_data[k][2]
        #             grid[i[0][0]][i[0][1]] -= 1
        #             grid[k[0]][k[1]] +=1
        #             print(grid)
        #             if k in acceptors:
        #                 del acceptors[k]
        #             if grid[i[0][0]][i[0][1]] == 1:
        #                 donors.remove(i[0])
        #                 escape = True
        #                 break
        # return turns

#     This workks but has a ston of inbuilt assumptions so i htink I should try to simplify a little since i
# overcomplicated it 100%

    # This clearly screams bfs or dp or back tracking w/ recursion lets try to be a little more elgant to be faster
        donors = {}
        min_moves = [4*8]
        acceptors = set()
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] == 0:
                    acceptors.add((i,j))
                elif grid[i][j] > 1:
                    donors[(i,j)] = grid[i][j]
        def backtrack(min_moves, walking_sum = 0):
            if len(acceptors) == 0:
                if walking_sum < min_moves[0]:
                    min_moves[0] = walking_sum
                return
            for i, j in acceptors.copy():
                for k,v in donors.items():
                    if v > 1:
                        tmp = abs(i-k[0])+abs(j-k[1])
                        walking_sum += tmp
                        acceptors.remove((i,j))
                        donors[k] -= 1
                        if walking_sum < min_moves[0]:
                            backtrack(walking_sum=walking_sum, min_moves=min_moves)
                        donors[k] += 1
                        walking_sum -= tmp
                        acceptors.add((i,j))
                break
        backtrack(min_moves=min_moves)
        return min_moves[0]
    # Got beats 100% - after looking througha bunch of other solutions the major optimization that it seems others
    # missed was a (trying to hard code in assumptions like I did in my first attempt before seeing it was a ton slower
    # then there were a bunch of other submissions with the backtracking style I did here - which makes a lot of sense
    # since it matches the problem really well and I am dissapointed I didn't see it before dumping all my time into
    # trying to logic te problem space to be smaller - but the optimizations to make this version faster ppl were missing
    # was to use a array to have pass by reference & an if on the min_moves before backtracking - effectively pruning
    # the bad trees of options as soon as possible rather than diving down inefficient routes.


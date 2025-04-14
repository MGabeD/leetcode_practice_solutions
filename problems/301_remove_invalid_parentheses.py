class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Instant thought - this is a brutally complex problem if we don't start with precomputing some stats...
        # my idea is create a few pieces of data in a first iterations [count open left by idx] [count open right by idx]
        # then to also create a set of two arrays with all fo there locations,  whenever I hit a sub-problem 2 left
        # three right i can recusively break down and do a choose function to get a set of options => assuming I have
        # pre computed data
#         I ended up going an entirely different route once I saw the sub-problems - not sure how efficient this is
# but I think its close to optimal will try again if i realize otherwise
        ret_data = set()
        left_fixed = solve_left_hand(s)
        for i in left_fixed:
            ret_data.update(solve_right_hand(i))
        return list(ret_data)

def fix_broken_cases(s, locs):
    options = set()
    for i in locs:
        options.add(s[0:i]+s[i+1:])
    return options

def solve_left_hand(s):
    if len(s) == 0:
        return {""}
    open_have = []
    open_needed = [0]
    close_location = []
    if s[0] == '(':
        open_have.append(1)
    elif s[0] == ')':
        return solve_left_hand(s[1:])
    else:
        open_have.append(0)
    for cur_char in range(1, len(s)):
        if s[cur_char] == '(':
            open_needed.append(open_needed[-1])
            open_have.append(open_have[-1]+1)
        elif s[cur_char] == ')':
            close_location.append(cur_char)

            open_needed.append(open_needed[-1] +1)
            open_have.append(open_have[-1])
            if open_needed[cur_char] > open_have[cur_char]:
                variations = fix_broken_cases(s[0:cur_char+1], close_location)
                sols = set()
                for j in variations:
                    sols.update(solve_left_hand(j + s[cur_char+1:]))
                return sols
        else:
            open_have.append(open_have[-1])
            open_needed.append(open_needed[-1])
    return {s}

def solve_right_hand(s):
    if len(s) == 0:
        return {""}
    close_have = []
    close_needed = [0]
    open_location = []
    if s[-1] == ')':
        close_have.append(1)
    elif s[-1] == '(':
        return solve_right_hand(s[:-1])
    else:
        close_have.append(0)
    for cur_char in range(1, len(s)):
        if s[-(1+cur_char)] == ')':
            close_needed.append(close_needed[-1])
            close_have.append(close_have[-1] + 1)
        elif s[-(1+cur_char)] == '(':
            open_location.append(-(1+cur_char))

            close_needed.append(close_needed[-1] + 1)
            close_have.append(close_have[-1])
            if close_needed[cur_char] > close_have[cur_char]:
                variations = fix_broken_cases(s[-(1+cur_char):], open_location)
                sols = set()
                for j in variations:
                    sols.update(solve_right_hand( s[:-(1+cur_char)]+ j))
                return sols
        else:
            close_have.append(close_have[-1])
            close_needed.append(close_needed[-1])
    return {s}

#
# # temp_str = "(a)())()"
# temp_str = ")("
# sol = Solution()
# print(sol.removeInvalidParentheses(temp_str))


# This solution was in the fastest bracken on leet code... I am kind of suprised since I didn't do any optimizations
# like at all ~ I could've done stuff to give a quick start to the subunits to not repeat iterations. this will be prob
# ~15% faster. I will implement this and test on leet code to see if I can make a new bracket of speeds!

# class Solution(object):
#     def removeInvalidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         ret_data = set()
#         left_fixed = solve_left_hand(s)
#         for i in left_fixed:
#             ret_data.update(solve_right_hand(i))
#         return list(ret_data)
#
# def fix_broken_cases(s, locs):
#     options = set()
#     for i in locs:
#         options.add(s[0:i]+s[i+1:])
#     return options
#
# def solve_left_hand(s, safe_before = 0):
#     if len(s) == 0:
#         return {""}
#     if len(s) == safe_before:
#         return {s}
#     open_have = []
#     open_needed = [0]
#     close_location = []
#     if s[0 + safe_before] == '(':
#         open_have.append(1)
#     elif s[0 + safe_before] == ')':
#         data = set(s[:safe_before]+ i for i in solve_left_hand(s[safe_before+1:]))
#         return data
#     else:
#         open_have.append(0)
#     for cur_char in range(1+safe_before, len(s)):
#         if s[cur_char] == '(':
#             open_needed.append(open_needed[-1])
#             open_have.append(open_have[-1]+1)
#         elif s[cur_char] == ')':
#             close_location.append(cur_char)
#
#             open_needed.append(open_needed[-1] +1)
#             open_have.append(open_have[-1])
#             if open_needed[-1] > open_have[-1]:
#                 variations = fix_broken_cases(s[0:cur_char+1], close_location)
#                 sols = set()
#                 for j in variations:
#                     sols.update(solve_left_hand(j + s[cur_char+1:], len(j)))
#                 return sols
#         else:
#             open_have.append(open_have[-1])
#             open_needed.append(open_needed[-1])
#     return {s}
#
# def solve_right_hand(s, safe_before = 0):
#     if len(s) == 0:
#         return {""}
#     if len(s) == safe_before:
#         return {s}
#     close_have = []
#     close_needed = [0]
#     open_location = []
#     if s[-(1+safe_before)] == ')':
#         close_have.append(1)
#     elif s[-(1+safe_before)] == '(':
#         # data = set(s[:safe_before] + i for i in solve_left_hand(s[save_before+1:]))
#         # return data
#         if safe_before != 0:
#             return set(s[-safe_before:] + i for i in solve_right_hand(s[:-(1+safe_before)]))
#         else:
#             return solve_right_hand(s[:-1])
#     else:
#         close_have.append(0)
#     for cur_char in range(1+safe_before, len(s)):
#         if s[-(1+cur_char)] == ')':
#             close_needed.append(close_needed[-1])
#             close_have.append(close_have[-1] + 1)
#         elif s[-(1+cur_char)] == '(':
#             open_location.append(-(1+cur_char))
#
#             close_needed.append(close_needed[-1] + 1)
#             close_have.append(close_have[-1])
#             if close_needed[-1] > close_have[-1]:
#                 variations = fix_broken_cases(s[-(1+cur_char):], open_location)
#                 sols = set()
#                 for j in variations:
#                     sols.update(solve_right_hand( s[:-(1+cur_char)]+ j, len(j)))
#                 return sols
#         else:
#             close_have.append(close_have[-1])
#             close_needed.append(close_needed[-1])
#     return {s}
#
#
# # temp_str = "(a)())()"
# # temp_str = ")(((abc(("
# temp_str = "())"
#
# sol = Solution()
# print(sol.removeInvalidParentheses(temp_str))

# this is a lot harder to implement than I initially thought since it opens up so many other edge cases- the first one
# was fast and good enough that i think I am happy

# there is a lot of possible optimization here but I have spent longer trying to put together a mild optimization with
# little upside then coming up with the algo itself. I think I am going to call it for today.

# Question to solution ~35 min
# getting mixed up in optimization land ~hr

# wasted a bit too much time with the optimzaiton attempts after - not necessary and wouldn't do in an interview so was
# kind of just brain game but I did fail it lmfao
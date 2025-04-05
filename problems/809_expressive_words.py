# Analysis of issues I ran into with this problem

# Straight out of the bat I found a good solution but I sped read through the problem and missed a critical point
# "add some number of characters c to the group so that the size of the group is three or more." I thought meant that
# the number of characters for the one being stretched MUST be 1->3+ not that if you had cc -> ccc is valid because there
# are three c-s. This still really messed me up as it was a single set of changes to my if statements but I didn't
# understand the question quite right so I technically got it wrong on my first attempt.

# Future improvements

# Jot out the parts of the solution as they match to the question rather than whatever I am interpreting in my head -
# this will FORCE me to slow down a bit while I am reading the question and hopefully make me a little better at
# matching the right edge cases to the problem.


def expressiveWords(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: int
    """
    solve_for = dev_stuff(s)
    ctr = 0
    for i in words:
        if check_work(i, solve_for):
            ctr+=1
    return ctr

def check_work(s, enforce):
    ctr = 0
    amount = 0
    for i in s:
        if i == enforce[ctr][0]:
            amount += 1
        elif ctr < len(enforce)-1:
            if (enforce[ctr][1] - amount == 1 and enforce[ctr][1] < 3) or enforce[ctr][1] - amount < 0:
                return False
            else:
                ctr += 1
                amount = 0
                if i != enforce[ctr][0]:
                    return False
                else:
                    amount += 1
        else:
            return False
    if ctr != len(enforce) -1 or (enforce[ctr][1] - amount == 1 and enforce[ctr][1] < 3) or enforce[ctr][1] - amount < 0:
        return False
    
    return True


def dev_stuff(s):
    data = [[s[0],0]]
    ctr = 0
    for i in s:
        if i == data[ctr][0]:
            data[ctr][1] += 1
        else:
            data.append([i,1])
            ctr += 1
    return data
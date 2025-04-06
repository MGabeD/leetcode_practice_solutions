# Problems

# I didn't know that python has a function for automating this process. This makes my way of doing it dramatically
# slower. I should have used the inbuild function s.startswith(word). However, I feel like this is against the concept
# of leetcode questions. I feel like the reason they exist is
# A) make sure you know DSA to a reasonable level
# B) make sure that you are willing to waste enough time to get really good at something (trust in process and
# willingness to work hard)
# C) be able to show you can figure out how things can work under the hood a little bit.
# Using inbuilt functions which can do this for you is kind of against the ~ethos~ of burning the time to get good at
# this - instead of critical thinking it is now just syntactic memorization for a fast to write in language like python

# Possible improvement event though I disagree with it conceptually:

# ctr = 0
# for word in words:
#   if s.startswith(word):
#       ctr += 1
# return ctr

# The above is what I should probably do if I get something like this in a non-for fun rendition of doing these
# questions

def countPrefixes(words, s):
    """
    :type words: List[str]
    :type s: str
    :rtype: int
    """
    proper_words = 0
    for word in words:
        works = True
        for j in range(0, len(word)):
            if j >= len(s):
                works = False
                break
            elif word[j] != s[j]:
                works = False
                break
        if works:
            proper_words += 1
    return proper_words


# Came back to my computer - read what I had written, I was thinking about better ways to solve this without being stuck
# on the inbuilt short cuts. Iterating through was a bad solution I got to in about 2 min after reading it. Taking a
# step back and thinking about it kinda made me realize that there is still a lesson to learn from the super easy ones
# what I should've done is gotten this solution then thought about how to make it faster. I could've done something like
# this - which is more efficient and still sticking to my beliefs about the reasoning to do these at the top

def ct_prefixes(words, s):
    prp_words = 0
    for word in words:
        if s[:len(word)] == word:
            prp_words +=1
    return prp_words

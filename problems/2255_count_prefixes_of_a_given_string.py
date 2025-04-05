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
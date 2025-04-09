# this one can't be run locally

# but I will still put it here so that I can push that I still did a problem to hold myself accountable today


def collapse_nested_integer(nested):
    is_int = nested.isInteger()
    if is_int:
        return [nested.getInteger()]
    else:
        cur = []
        for i in nested.getList():
            cur.extend(collapse_nested_integer(i))
        return cur


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.index = 0
        cur_list = []
        for i in nestedList:
            cur = collapse_nested_integer(i)
            cur_list.extend(cur)
        self.data = cur_list

    def next(self):
        """
        :rtype: int
        """
        data = self.data[self.index]
        self.index += 1
        return data

    def hasNext(self):
        return self.index < len(self.data)

# This is my first version but I can make it faster if I cut out extend and the making of new lists - only beating
# 70% of answers and I can do this small optimization to get minorly better performacne I think

class NestedIterator(object):
    def _collapse_nested_integer(self, nested):
        is_int = nested.isInteger()
        if is_int:
            self.data.append(nested.getInteger())
        else:
            cur = []
            for i in nested.getList():
                self._collapse_nested_integer(i)

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.index = 0
        self.data = []
        for i in nestedList:
            self._collapse_nested_integer(i)

    def next(self):
        """
        :rtype: int
        """
        data = self.data[self.index]
        self.index += 1
        return data

    def hasNext(self):
        return self.index < len(self.data)

# Beating 75% but I think I can still do better

def collapse_nested_integer(nested):
    is_int = nested.isInteger()
    if is_int:
        return [nested.getInteger()]
    else:
        cur = []
        for i in nested.getList():
            cur.extend(collapse_nested_integer(i))
        return cur


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.index = 0
        cur_list = []
        for i in nestedList:
            cur = collapse_nested_integer(i)
            cur_list.extend(cur)
        self.data = cur_list

    def next(self):
        """
        :rtype: int
        """
        data = self.data[self.index]
        self.index += 1
        return data

    def hasNext(self):
        return self.index < len(self.data)

# This is my first version but I can make it faster if I cut out extend and the making of new lists - only beating
# 70% of answers and I can do this small optimization to get minorly better performacne I think

class NestedIterator(object):
    def _collapse_nested_integer(self, nested, append):
        if nested.isInteger():
            append(nested.getInteger())
        else:
            for i in nested.getList():
                self._collapse_nested_integer(i, append)

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.index = 0
        self.data = []
        for i in nestedList:
            self._collapse_nested_integer(i, self.data.append)

    def next(self):
        """
        :rtype: int
        """
        data = self.data[self.index]
        self.index += 1
        return data

    def hasNext(self):
        return self.index < len(self.data)

# got a little bit more performance I am happy enough with that now
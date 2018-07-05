#
# Input: "this and these are words"
# Output: [ "and", "are", "these", "this", "words" ]

def string_split(s):
    n = len(s)
    if n == 0:
        return []
    else:
        result = []
        start_index = 0
        end_index = None
        for i in range(n):
            if s[i] == ' ':
                end_index = i
                if end_index:
                    result.append(s[start_index:end_index])
                    end_index = None
                    start_index = i+1
        result.append(s[start_index:])
        result.sort()
    return result


print(string_split("this and these are words"))


class node:
    def __init__(self, val):
        self.data = val
        self.childrens = {}
        self.is_word = False
        if val:
            self.rank = ord(val)
        else:
            self.rank = -1

    def get_val(self):
        return self.data

    def get_child(self, ch):
        return self.childrens.get(ch)

    def add_child(self, ch):
        if self.childrens.get(ch):
            return self.childrens[ch]
        else:
            nd = node(ch)
            self.childrens[ch] = nd
            return nd


class tries:
    def __init__(self):
        nd = node(None)
        self.root = nd

    def add_word(self, word):
        n = len(word)
        if n:
            current = self.root
            for i in range(len(word)):
                next = current.get_child(word[i])
                if next:
                    current = next
                else:
                    current = current.add_child(word[i])
            current.is_word = True
import re

class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.word_cnt = 0
        self.children = [None] * 26

class Tries:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            pCrawl.word_cnt += 1

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        cnt = 0
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return cnt
            pCrawl = pCrawl.children[index]
        return pCrawl.word_cnt


n = long(raw_input().strip())
t = Tries()
result_list = []
for a0 in range(n):
    str =  raw_input().strip()
    print("""==={0}""".format(str))
    op, contact = str.split(' ')
    if op == 'add':
        t.insert(contact)
    if op == 'find':
        cnt = t.search(contact)
        result_list.append(cnt)

for cnts in result_list:
    print(cnts)

# print_bst(contact_list)

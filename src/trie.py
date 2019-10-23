
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        t = self.root
        word = word.lower()
        for w in word:
            if w not in t.children:
                t.children[w] = TrieNode()
            t = t.children[w]
        t.endOfWord = True

    def _searchString(self, word):
        t = self.root
        for w in word:
            if w not in t.children:
                return None
            t = t.children[w]
        return t

    def search(self, word):
        t = self._searchString(word)
        return t is not None and t.endOfWord

    def startsWith(self, prefix):
        t = self._searchString(prefix)
        return t is not None

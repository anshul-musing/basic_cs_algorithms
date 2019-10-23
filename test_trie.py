
from src.trie import Trie

def testTrie():
    '''
    Here we test algorithms for a trie tree
    We test insert, search, and start-with functions
    Each node of the trie tree is an object of
    the TrieNode class, which has
    a. children hash that stores characters as hash keys
    b. endOfWord boolean indicator
    '''

    print('Create an empty trie')
    t = Trie()
    print('apple exists? ' + str(t.search('apple')))
    print('\"\" exists? ' + str(t.search('')))
    print('\"\" prefix exists? ' + str(t.startsWith('')))
    print('Insert apple')
    t.insert('apple')
    print('apple exists? ' + str(t.search('apple')))
    print('app exists? ' + str(t.search('app')))
    print('app prefix exists? ' + str(t.startsWith('app')))
    print('appe prefix exists? ' + str(t.startsWith('appe')))
    print('Insert app')
    t.insert('app')
    print('app exists? ' + str(t.search('app')))
    print('Insert @pple')
    t.insert('@pple')
    print('@pple exists? ' + str(t.search('@pple')))


if __name__ == '__main__':
    print(testTrie.__doc__)
    testTrie()

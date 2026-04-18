class TrieNode:
    def __init__(self):
        self.isWord = False
        self.letters = {}

class PrefixTree:

    def __init__(self):
        self.head = TrieNode()
        self.head.val = "*"

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.letters:
                cur.letters[c] = TrieNode()
            cur = cur.letters[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur.letters:
                return False
            cur = cur.letters[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur.letters:
                return False
            cur = cur.letters[c]
        return True
        
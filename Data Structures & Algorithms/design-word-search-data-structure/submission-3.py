class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.head
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(index: int, cur: TrieNode) -> bool:
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for j in cur.children.values():
                        if dfs(i+1, j):
                            return True
                if c not in cur.children:                    
                    return False
                cur = cur.children[c]
            return cur.isWord
        return dfs(0, self.head)
        
import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        q = collections.deque([s])
        visited = set()
        while len(q) > 0:
            remaining = q.popleft()
            for word in wordDict:
                if word == remaining:
                    return True
                if remaining.startswith(word):
                    newRemaining = remaining[len(word):]
                    if newRemaining in visited:
                        continue
                    visited.add(newRemaining)
                    q.append(newRemaining)
        return False

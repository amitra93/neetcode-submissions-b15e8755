import collections

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True
        if len(edges) == 2:
            return False

        adjList = collections.defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        queue = collections.deque([(-1, 1)])
        visited = set()
        while len(queue) > 0:
            prev, cur = queue.popleft()
            if cur in visited:
                return False
            visited.add(cur)
            for i in adjList[cur]:
                if i == prev:
                    continue
                queue.append((cur, i))
        return len(visited) == len(adjList)


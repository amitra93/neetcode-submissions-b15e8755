import collections

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        print(adjList)
        
        visited = set()
        components = 0

        def findFirstNotVisited():
            for node in adjList:
                if node not in visited:
                    return node
            raise ValueError

        while len(visited) != len(adjList):
            unvisitedNode = findFirstNotVisited()
            queue = collections.deque([unvisitedNode])
            while len(queue) > 0:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in adjList[node]:
                    queue.append(neighbor)
            components += 1
        return components + (n - len(visited))


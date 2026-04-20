import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        
        cloneMap = {}
        queue = collections.deque()
        queue.append(node)
        cloneMap[node] = Node(node.val)
        while len(queue) > 0:
            curNode = queue.popleft()
            print(f"looking at {curNode.val}")
            for i in curNode.neighbors:
                if i not in cloneMap:
                    cloneMap[i] = Node(i.val)
                    queue.append(i)
                cloneMap[curNode].neighbors.append(cloneMap[i])
        return cloneMap[node]
        

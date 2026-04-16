class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visitedSet = set()
        total = 0

        def dfs(i: int, j: int):
            stack = []
            stack.append((i, j))
            visitedSet.add((i, j))
            while len(stack) > 0:
                base = stack.pop()
                dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dir in dirs:
                    newX = base[0] + dir[0]
                    newY = base[1] + dir[1]

                    if (newX, newY) in visitedSet:
                        continue
                    if newX < 0 or newX >= len(grid):
                        continue
                    if newY < 0 or newY >= len(grid[0]):
                        continue
                    if grid[newX][newY] == "0":
                        continue
                    visitedSet.add((newX, newY))
                    stack.append((base[0] + dir[0], base[1] + dir[1]))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visitedSet:
                    continue
                if grid[i][j] == "1":
                    total += 1
                    dfs(i, j)

        return total
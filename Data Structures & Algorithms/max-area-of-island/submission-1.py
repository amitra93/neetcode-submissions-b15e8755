class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        for row in grid:
            print(row)

        def dfs(i: int, j: int) -> int:
            stack = [(i, j, 1)]
            maxAreaOfThisIsland = 0
            while len(stack) > 0:
                coordAndArea = stack.pop()
                x = coordAndArea[0]
                y = coordAndArea[1]
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                grid[x][y] = 0
                maxAreaOfThisIsland += 1
                area = coordAndArea[2]
                dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                for dir in dirs:
                    newX = x + dir[0]
                    newY = y + dir[1]
                    if newX < 0:
                        continue
                    if newX >= rows:
                        continue
                    if newY < 0:
                        continue
                    if newY >= cols:
                        continue
                    if grid[newX][newY] == 0:
                        continue
                    stack.append((newX, newY, 1 + area))
            return maxAreaOfThisIsland


        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * len(cost)
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        for i in range(2, len(cost)):
            minCost[i] = min(cost[i] + minCost[i-2], cost[i] + minCost[i-1])
            print(minCost)
        return min(minCost[-1], minCost[-2])
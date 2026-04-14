import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for coord in points:
            x = coord[0]
            y = coord[1]
            distance = math.sqrt(x**2 + y**2)
            heap.append((distance, (x, y)))
        
        print(heap)
        heapq.heapify(heap)
        
        retVal = list()
        while len(retVal) < k:
            retVal.append(heapq.heappop(heap)[1])
        return retVal
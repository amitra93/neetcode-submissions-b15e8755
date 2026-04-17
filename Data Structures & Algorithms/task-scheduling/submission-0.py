import collections
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = {}
        totalTasks = 0
        for task in tasks:
            taskMap[task] = taskMap.get(task, 0) + 1
            totalTasks += 1
        taskHeap = []
        for task in taskMap:
            taskHeap.append(taskMap[task])
        heapq.heapify_max(taskHeap)

        taskQueue = collections.deque()
        numCycles = 0
        while len(taskHeap) > 0 or len(taskQueue) > 0:
            numCycles += 1
            if len(taskHeap) > 0:
                task = heapq.heappop_max(taskHeap)
                if task - 1 > 0:
                    taskQueue.append((task, n + numCycles))
            if taskQueue and taskQueue[0][1] == numCycles:
                task = taskQueue.popleft()
                heapq.heappush_max(taskHeap, task[0]-1)
        return numCycles
            
                

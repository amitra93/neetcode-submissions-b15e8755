import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 2 scenarios, either there is a cycle or there is an unreachable course
        courses = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            courses[prereq[0]].append(prereq[1])

        visited = set()

        def dfs(course):
            # Detected a cycle, need to return false
            if course in visited:
                return False
            # Base case, course has no prereqs, no need to recurse
            if len(courses[course]) == 0:
                return True

            # Add course to visited
            visited.add(course)
            # Check every prereq to see that it passes dfs
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False

            # remove the course so other courses can still visit it if needed
            visited.remove(course)
            courses[course].clear()
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

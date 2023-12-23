# There are a total of numCourses courses you
# have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where
# prerequisites[i] = [ai, bi] indicates that you must
# take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take
# course 0 you have to first take course 1.
#
# Return true if you can finish all courses.
# Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegs = {}

        for (course, prereq) in prerequisites:
            if course not in indegs:
                indegs[course] = 0
            if prereq not in indegs:
                indegs[prereq] = 0
            if course not in graph:
                graph[course] = list()
            if prereq not in graph:
                graph[prereq] = list()
            indegs[course] += 1
            graph[prereq].append(course)

        frontier = [course for course in indegs if indegs[course] == 0]
        visited = set()
        taken = 0
        while frontier:
            for node in frontier:
                if node in visited:
                    continue
                visited.add(node)
                taken += 1
                for postreq in graph[node]:
                    indegs[postreq] -= 1

            new_frontier = []
            for node in frontier:
                for postreq in graph[node]:
                    if indegs[postreq] == 0:
                        new_frontier.append(postreq)
            frontier = new_frontier

        return taken == len(graph)

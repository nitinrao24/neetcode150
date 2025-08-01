# leetcode 207
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
# that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Time Complexity:
# Space Complexity:
from collections import defaultdict
def courseschedule(numCourses,prerequisites):
    prereq_map = defaultdict(list)
    for course, prereq in prerequisites:
        prereq_map[course].append(prereq)

    visiting = set()
    resolved = set()

    def dfs(course):
        if course in resolved:
            return True

        if course in visiting:
            return False  # cycle detected

        if not prereq_map[course]:
            resolved.add(course)
            return True

        visiting.add(course)

        for prereq in prereq_map[course]:
            if not dfs(prereq):
                return False

        visiting.remove(course)
        resolved.add(course)
        prereq_map[course] = []  # memoize as done
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True
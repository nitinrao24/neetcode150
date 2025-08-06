# leetcode 210
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
# that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
# If it is impossible to finish all courses, return an empty array.

# Time Complexity:
# Space Complexity:
from typing import List
from collections import defaultdict
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # Create a mapping from each course to the list of courses that depend on it
    adj = defaultdict(list)
    for course, prereq in prerequisites:
        adj[prereq].append(course)

    # Count how many prerequisites each course has
    in_deg = [0] * numCourses
    for course, prereq in prerequisites:
        in_deg[course] += 1

    # Start with all courses that have zero prerequisites
    queue = deque()
    for course_id in range(numCourses):
        if in_deg[course_id] == 0:
            queue.append(course_id)

    # This will store the valid order of courses
    order = []

    # Process courses in order of availability
    while queue:
        current = queue.popleft()
        order.append(current)

        # "Unlock" each course that depended on the one we just took
        for next_course in adj[current]:
            # Remove one prerequisite from next_course
            in_deg[next_course] -= 1

            # If it has no more prerequisites, it's ready to take
            if in_deg[next_course] == 0:
                queue.append(next_course)

    # If we've added every course to 'order', we found a valid schedule
    if len(order) != numCourses:
        # Cycle detected or unmet prerequisite => no valid order
        return []

    return order
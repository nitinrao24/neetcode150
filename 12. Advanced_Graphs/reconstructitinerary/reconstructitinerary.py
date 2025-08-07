# leetcode 332
# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight.
# Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
# If there are multiple valid itineraries,
# you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
from collections import defaultdict
from typing import List
# Time Complexity:
# Space Complexity:

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # group all destinations by departure airport
    flights = defaultdict(list)
    # sort tickets in reverse lex order so we can pop the smallest next airport
    for frm, to in sorted(tickets, reverse=True):
        flights[frm].append(to)

    route = []          # this will store our final path in reverse
    stack = ["JFK"]     # start from JFK

    while stack:
        current = stack[-1]
        # if we still have places to go from here, go there next
        if flights[current]:
            next_stop = flights[current].pop()
            stack.append(next_stop)
        else:
            # no more flights out of current, add it to route and backtrack
            route.append(stack.pop())

    # route is built backwards, so reverse it
    return route[::-1]
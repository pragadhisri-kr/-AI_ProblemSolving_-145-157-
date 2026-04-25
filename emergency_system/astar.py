from heapq import heappush, heappop
from data import graph, heuristic

def astar(start, goal):
    open_list = []
    heappush(open_list, (0, start, []))
    visited = set()

    while open_list:
        cost, node, path = heappop(open_list)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == goal:
            return path, cost

        for neighbor in graph[node]:
            new_cost = cost + graph[node][neighbor]
            priority = new_cost + heuristic[neighbor]
            heappush(open_list, (priority, neighbor, path))

    return None, None

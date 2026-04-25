from collections import deque
from rules import move

def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited = []

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        visited.append(current)

        for block in current:
            for dest in ["table"] + list(current.keys()):
                if block != dest:
                    new_state = move(block, dest, current)

                    if new_state not in visited:
                        queue.append((new_state, path + [f"Move {block} to {dest}"]))

    return None

from collections import deque
import copy

def state_to_tuple(state):
    return tuple(tuple(stack) for stack in state)

def get_moves(state):
    moves = []
    for i in range(len(state)):
        if not state[i]:
            continue
        for j in range(len(state)):
            if i != j:
                new_state = copy.deepcopy(state)
                block = new_state[i].pop()
                new_state[j].append(block)
                move = f"Move {block} from Stack {i+1} to Stack {j+1}"
                moves.append((new_state, move))
    return moves

def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        t = state_to_tuple(current)

        if t in visited:
            continue
        visited.add(t)

        if current == goal:
            return path, current

        for new_state, move in get_moves(current):
            queue.append((new_state, path + [move]))

    return None, None

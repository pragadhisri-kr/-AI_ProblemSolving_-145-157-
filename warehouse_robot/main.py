from state import initial_state, goal_state
from planner import bfs

result = bfs(initial_state, goal_state)

if result:
    print("Steps to reach goal:")
    for step in result:
        print(step)
else:
    print("No solution found")

import streamlit as st
from collections import deque
import copy

# Convert state to tuple
def state_to_tuple(state):
    return tuple(tuple(stack) for stack in state)

# Check goal
def is_goal(state, goal):
    return state == goal

# Generate valid moves
def get_moves(state):
    moves = []
    for i in range(len(state)):
        if len(state[i]) == 0:
            continue

        for j in range(len(state)):
            if i != j:
                new_state = copy.deepcopy(state)
                block = new_state[i].pop()
                new_state[j].append(block)

                move_desc = f"Move {block} from Stack {i+1} to Stack {j+1}"
                moves.append((new_state, move_desc))

    return moves

# BFS
def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        current_tuple = state_to_tuple(current)

        if current_tuple in visited:
            continue

        visited.add(current_tuple)

        if is_goal(current, goal):
            return path, current

        for new_state, move in get_moves(current):
            queue.append((new_state, path + [move]))

    return None, None

# Convert input text to stacks
def parse_input(text):
    lines = text.strip().split("\n")
    state = []
    for line in lines:
        if line.lower() == "empty":
            state.append([])
        else:
            state.append(line.split())
    return state

# UI
st.title(" Warehouse Robot Planner")

st.subheader("Enter Initial State (one stack per line)")
initial_input = st.text_area("Example:\nA B C\nD\nempty")

st.subheader("Enter Goal State (one stack per line)")
goal_input = st.text_area("Example:\nA\nB C\nD")

if st.button("Generate Plan"):
    initial_state = parse_input(initial_input)
    goal_state = parse_input(goal_input)

    steps, final_state = bfs(initial_state, goal_state)

    st.subheader("Initial Configuration")
    for i, stack in enumerate(initial_state):
        st.write(f"Stack {i+1}: {stack if stack else 'Empty'}")

    st.subheader("Goal Configuration")
    for i, stack in enumerate(goal_state):
        st.write(f"Stack {i+1}: {stack if stack else 'Empty'}")

    if steps:
        st.subheader("Step-by-step Plan")
        for i, step in enumerate(steps):
            st.write(f"Step {i+1}: {step}")

        st.subheader("Final Configuration")
        for i, stack in enumerate(final_state):
            st.write(f"Stack {i+1}: {stack if stack else 'Empty'}")
    else:
        st.error("No solution found")

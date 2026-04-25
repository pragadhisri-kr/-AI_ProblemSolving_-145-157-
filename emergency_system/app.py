import streamlit as st
from heapq import heappop, heappush

# Graph (city map)
graph = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "D": 7, "E": 3},
    "C": {"A": 4, "F": 5},
    "D": {"B": 7},
    "E": {"B": 3, "F": 1},
    "F": {"C": 5, "E": 1}
}

# Heuristic values
heuristic = {
    "A": 7, "B": 6, "C": 2,
    "D": 1, "E": 1, "F": 0
}

# Emergency service locations
services = {
    "Fire": "D",
    "Medical": "F",
    "Police": "E"
}

# A* Algorithm
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

# UI
st.title("🚑 Smart Emergency Response System")

start = st.selectbox("Select Start Location", list(graph.keys()))
emergency = st.selectbox("Select Emergency Type", ["Fire", "Medical", "Police"])

if st.button("Find Best Route"):
    goal = services[emergency]
    path, cost = astar(start, goal)

    st.subheader("🚨 Result")

    st.write(f"**Emergency Type:** {emergency}")
    st.write(f"**Nearest Service Location:** {goal}")

    if path:
        st.write(f"**Optimal Path:** {' → '.join(path)}")
        st.write(f"**Total Cost:** {cost}")
    else:
        st.error("No path found")

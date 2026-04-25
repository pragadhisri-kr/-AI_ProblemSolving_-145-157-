def move(block, destination, state):
    new_state = state.copy()
    new_state[block] = destination
    return new_state

# -AI_ProblemSolving_-145-157-
AI Problem Solving using A* (Smart Emergency Response System) and Search-based Planning (Warehouse Robot Planner – Blocks World) with visualization and decision support in Python.

# AI Problem Solving Assignment

## Team Members

* Member 1: Pragadhisri k
* Member 2: Christinal mercy

---

##  Problem 1: Warehouse Robot Planner

### Description

A warehouse robot rearranges blocks from an initial configuration into a desired goal configuration. The robot follows valid rules where only the top block of any stack can be moved, and each move transforms the system step-by-step until the goal state is achieved.

### Algorithm Used

* State Space Search
* Breadth First Search (BFS)
  

## ▶️ Execution Steps

1. Enter initial and goal stack configurations.
2. Represent blocks as stacks internally.
3. Apply BFS to explore possible states.
4. Move only the top block between stacks.
5. Generate valid intermediate states.
6. Check for goal state after each move.
7. Display step-by-step solution when goal is reached.


### Features

* Stack-based block representation
* Valid moves (only top block)
* Step-by-step solution
* GUI using Tkinter

### Sample Output

* Move C from Stack 1 to Stack 2
* Move B from Stack 1 to Stack 2

---

##  Problem 2: Smart Emergency Response System

### Description

This system helps in selecting the nearest emergency service (Fire, Medical, Police) and finds the optimal route from a given location using intelligent search techniques.

### Algorithm Used

* A* Search Algorithm

##  Execution Steps

1. Select starting location.
2. Choose emergency type (Fire / Medical / Police).
3. Identify nearest service location.
4. Apply A* algorithm to find optimal path.
5. Calculate cost and heuristic values.
6. Determine shortest route.
7. Display path and total cost.

### Features

* Select emergency type
* Finds nearest service
* Displays optimal path and cost
* GUI using Streamlit

### Sample Output

* Path: A → B → E → F
* Cost: 6

---
Website Links (Live Demo)

 Note: These links work only within the same local network.

Emergency System:
http://10.216.19.187:8502
Warehouse Robot Planner:
http://10.216.19.187:8503

## How to Run

### Warehouse Robot

```
python app.py
```

### Emergency System

```
python -m streamlit run app.py
```

---

## Screenshots

![emergency](output.png)
![warehouse](output.png)

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
  

## Execution Steps

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

Initial State:
Stack 1: A C B
Stack 2: —
Stack 3: —

Goal State:
Stack 1: —
Stack 2: A B C
Stack 3: —

Execution Trace:
Step 1: Move C from Stack 1 → Stack 2  
Step 2: Move B from Stack 1 → Stack 2  
Step 3: Move A from Stack 1 → Stack 2  

Final Result:
Goal state achieved successfully in 3 moves.
---

##  Problem 2: Smart Emergency Response System

### Description

This system helps in selecting the nearest emergency service (Fire, Medical, Police) and finds the optimal route from a given location using intelligent search techniques.

### Algorithm Used

* A* Search Algorithm

##  Execution Steps

1.Input the source location (incident point).
2.Select the type of emergency (Fire / Medical / Police).
3.System identifies the nearest available service station.
4.Construct a weighted graph representing the city network.
5.Apply the A search algorithm* using:
g(n): actual travel cost
h(n): heuristic estimated cost
6.Evaluate and expand nodes based on minimum f(n) = g(n) + h(n).
7.Generate the optimal path with minimum response time and display results.

### Features

* Select emergency type
* Finds nearest service
* Displays optimal path and cost
* GUI using Streamlit

### Sample Output

Input:
Location: Node A  
Emergency Type: Medical  

Processing:
Nearest Hospital Identified: Hospital F  
Algorithm Used: A* Search  

Optimal Path Found:
A → B → D → F  

Performance Metrics:
Total Cost (g): 6  
Heuristic (h): 0  
Final Cost (f): 6  

Output:
Fastest emergency response route successfully computed.
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

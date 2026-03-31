# Fundamentals in AI and ML Project
# 🚀 Comparative Search Algorithm Framework
A Python-based implementation and performance analysis of Breadth-First Search (BFS) vs. A* Search in weighted graphs. This project demonstrates how heuristic functions can optimize pathfinding in AI.

# 📖 Table of Contents
- Overview
- Features
- Installation
- Algorithms Explained
- Usage
- Results

# 🌟 Overview
In Artificial Intelligence, "Search" is the process of navigating a state space to reach a goal. This project implements a comparative framework to show the difference between Uninformed (blind) search and Informed (heuristic-driven) search.

# ✨ Features
BFS Implementation: Finds the path with the fewest edges.
*A Implementation: Uses an admissible heuristic (f(n) = g(n) + h(n)) to find the path with the lowest total weight.
Heuristic Comparison: Analyzes how node expansion is reduced when "knowledge" is added to the search.

# 🛠 Installation
1- Access the given repository
2- Ensure Python 3.x is installed. No external libraries are required.

# 🧠 Algorithms Explained
1. Breadth-First Search (BFS)
BFS explores the neighbor nodes first, before moving to the next level neighbors. It is optimal for finding the shortest path in unweighted graphs.
2. A* (A-Star) Search
A* is one of the most popular search algorithms used in game dev and robotics. It uses a Heuristic—an "educated guess"—of the remaining distance to the goal to prioritize which path to explore first.

# 🚀 Usage
Run the main script to see the path comparison:

# 📊 Results
Upon execution, the framework outputs the following comparison for any chosen path from Node A to Node F. For the case demonstrated in this project, we have used Node A as the start and Node F as the goal.
A* finds a path that is more cost-effective than BFS by incorporating edge weights and heuristics.

# 🛠 Tech Stack
Language: Python 3.10+
Libraries: heapq (Priority Queue), collections (Deque)

import collections
import heapq

a = input("Enter start node from A to F")
b = input("Enter finish node from A to F")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 5), ('E', 2)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 5)],
    'E': [('B', 2), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Bredth First Search
def bfs(start, goal):
    queue = collections.deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal: return path
        for (neighbor, weight) in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

# A* Search
# Heuristic values
heuristic = {'A': 6, 'B': 5, 'C': 2, 'D': 7, 'E': 1, 'F': 0}

def a_star(start, goal):
    pq = [(0 + heuristic[start], 0, [start])] # (priority, cost, path)
    visited = {}
    
    while pq:
        (f, cost, path) = heapq.heappop(pq)
        node = path[-1]
        
        if node == goal: return path, cost
        
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for (neighbor, weight) in graph.get(node, []):
                new_cost = cost + weight
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (priority, new_cost, path + [neighbor]))

# Execute search
print("BFS Path for given nodes:", bfs(a,b))
path_astar, cost_astar = a_star(a,b)
print(f"A* Path to F: {path_astar} with Cost: {cost_astar}")

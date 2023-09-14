# Define a simple graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        visited.add(start)

        if start == goal:
            return [start]  # Found the goal, return a list with just the goal

        for neighbor in graph[start]:
            if neighbor not in visited:
                path = dfs(graph, neighbor, goal, visited)
                if path:
                    return [start] + path  # Add the current node to the path and return it

    return []  # Return an empty list if the goal is not found

# Start DFS
start = input("Choose node to start from : ")
goal = input("Choose node as a goal : ")
path = dfs(graph, start, goal)

if path:
    print("Path from", start, "to", goal, ":", "->".join(path))
else:
    print("No path found from", start, "to", goal)

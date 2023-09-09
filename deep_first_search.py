# Define a simple graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=' ')
        visited.add(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

# Start DFS from node 'A'
print("Depth-First Search starting from 'A':")
dfs(graph, 'A')
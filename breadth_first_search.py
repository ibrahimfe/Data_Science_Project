from collections import deque

# Define a simple graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque()  # Initialize a queue for BFS

    # Start with the initial node
    queue.append(start)
    visited.add(start)

    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        print(node, end=' ')

        # Visit all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Start BFS from node 'A'
print("Breadth-First Search starting from 'A':")
bfs(graph, 'A')
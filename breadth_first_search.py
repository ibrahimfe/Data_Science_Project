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

def bfs(graph, start, goal):
    visited = set()  # To keep track of visited nodes
    queue = deque()  # Initialize a queue for BFS

    # Start with the initial node
    queue.append(start)
    visited.add(start)
    if start == goal:
        print("The Start is the goal")
        return 0

    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        print(node, end=' ')

        if goal == node:
            return 0
        # Visit all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Start BFS
start = input("Choose The Start Node : ")
goal = input("Choose The Goal : ")
bfs(graph, start, goal)
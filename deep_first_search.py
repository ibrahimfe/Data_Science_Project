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
    if goal in visited:
        return 0

    if start not in visited:
        print(start, end=' ')
        visited.add(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, goal ,visited)
                
# Start DFS
start = input("Choose node to start from : ")
goal = input("Choose node as a goal : ")
dfs(graph, start, goal)
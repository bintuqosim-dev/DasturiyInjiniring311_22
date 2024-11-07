from collections import deque

def bfs(graph, start_node):
    visited = []
    
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'

result = bfs(graph, start_node)
print("Grafikdagi tugunlarni BFS tartibida ko‘rib chiqish:", result)

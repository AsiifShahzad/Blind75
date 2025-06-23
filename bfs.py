def bfs(visited, graph, start_node, goal):
    visited = []    # List to keep track of all visited nodes.
    queue = []      # Queue of paths

    # Start by visiting and enqueuing the path [start_node]
    visited.append(start_node)
    queue.append([start_node])

    # Continue until the queue is empty
    while queue:
        # Pop the first path
        path = queue.pop(0)
        node = path[-1]  # Current node is the path’s last element

        # If this node is the goal, we’ve found the shortest path
        if node == goal:
            return path

        # Otherwise, enqueue new paths for each unvisited neighbor
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.append(neighbour)
                # Build a new path appending this neighbour
                new_path = path + [neighbour]
                queue.append(new_path)

    # If we exhaust the queue without finding goal
    return None


if __name__ == "__main__":
    # Example graph represented as an adjacency list (dictionary)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start = 'A'
    goal  = 'F'

    print(f"BFS searching from {start} to {goal}:")
    path = bfs(visited, graph, start, goal)

    if path:
        print("Path found:", " → ".join(path))
    else:
        print("Goal not reachable from start.")

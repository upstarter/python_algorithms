def search(graph, start_node):
    explored = set()
    # its simple:
    # if frontier is stack(lifo), then its DFS
    # if frontier is queue(fifo), then its BFS
    frontier = set(start_node)

    while frontier:
        node = frontier.pop()

        # skip this node if we've already explored it
        if node in explored:
            next

        explored.add(node)

        for neighbor in graph[node]:
            if neighbor not in explored:
                frontier.add(neighbor)

    return explored


graph = {
    "a": ["c", "d"],
    "b": ["d", "e"],
    "c": ["a", "e"],
    "d": ["a", "b"],
    "e": ["b", "c"],
}

print(search(graph, "a"))

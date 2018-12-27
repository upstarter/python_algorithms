def search(graph, start_node):
  explored = set()
  # its simple:
  # if frontier is stack(lifo), then its DFS
  # if frontier is queue(fifo), then its BFS
  frontier = set()

  while frontier:
    node = frontier.pop()

    # skip this node if we've already explored it
    if node in explored:
      next

    explored.add(node)

    for neighbor in graph.neighbors(node):
      if neighbor not in explored:
        frontier.add(node)

  return explored

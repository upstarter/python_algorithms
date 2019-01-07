# to convert a list of tuples to a dictionary using the first value as the key.
# Looked like this (making a database of comic book files):

data = [((31), ("Amazing Spider-Man"), (481), ("Marvel")),
        ((28), ("The Incredible Hulk"), (612), ("Marvel"))] # etc, hundreds more like this.

# could have done this:

dict_data = {}
for i in data:
    dict_data[i[0]] = [i[1], i[2], i[3]]

 # a more Pythonic approach.
dict_data = {i[0]:[*i[1:]] for i in data}
print(dict_data)

# Graphs

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

# import dictionary for graph
from collections import defaultdict

# function for adding edge to graph
graph = defaultdict(list)

def addEdge(graph,u,v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    return edges


# function to find path
def find_path(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return path
  for node in graph[start]:
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath:
        return newpath
      return None


# function to generate all possible paths
def find_all_paths(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return [path]
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
    for newpath in newpaths:
      paths.append(newpath)
  return paths

 # function to find the shortest path
def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

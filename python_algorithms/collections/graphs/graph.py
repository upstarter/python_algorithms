graph = { "a" : ["c", "d"],
          "b" : ["d", "e"],
          "c" : ["a", "e"],
          "d" : ["a", "b"],
          "e" : ["b", "c"]
        }

def define_edges(graph):
    edges = []
    for vertex in graph:
        for neighbour in graph[vertex]:
            edges.append((vertex, neighbour))
    return edges

print(define_edges(graph))

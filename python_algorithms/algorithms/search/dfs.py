# DFS often used to reach whole graph
# edge classification, useful for cycle detection and topological sort
    # tree edges (parent pointer)
    # forward edge: node to descendent
    # backward edge: node to ancestor
    # cross edge: between two non-ancestor-related subtrees
# job scheduling (topological sort)
# Grapn G has a cycle if G has a backward edge

# visit only vertices reachable from s
parent = {"a": None}
def dfs_visit(s, Adj):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            print(s)
            dfs_visit(v, Adj)


# visit all vertices
def dfs(V, Adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            dfs_visit(s, Adj)


# Adjacency list representation
graph = { "a" : ["b"],
          "b" : ["c"],
          "c" : ["e", "d"],
          "d" : [],
          "e" : []
        }

print dfs(["a","b"], graph)

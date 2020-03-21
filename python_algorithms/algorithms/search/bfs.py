# BFS often used to reach portion of graph
# Shortest Path and Minimum Spanning Tree for unweighted graph
# search graph for shortest paths (fastest way to get everywhere, searches layer by layer)
# web crawlers
# solve rubiks cubes
# p2p networks
# social networking (6 degrees etc..)
# network broadcasting
# path finding
# Finding all nodes within one connected component


def bfs(s, Adj):
    # s is what can reach in 0 moves
    level = {s: 0}
    # stores parent links of visited vertices, is shortest path in reverse. Is length level of v
    parent = {s: None}
    i = 1  # just finished level 0
    frontier = [s]  # what we just reached on previous level (using i - 1 moves)
    while frontier:
        next = []  # all things can reach in i moves (next level in graph)
        for u in frontier:  # look at every node in frontier
            for v in Adj[u]:  # and then all nodes you can reach from frontier nodes
                if (
                    v not in level
                ):  # check for duplicate visits, v would be in level if already visited
                    level[v] = i  # add if not there
                    parent[v] = u  # set parent of this vertex to vertex we came from
                    print (v)  # do stuff at unexplored node
                    next.append(v)  # add to next frontier
        frontier = next  # done with this frontier, set frontier to next level
        i += 1
    return parent


# Adjacency list
graph = {
    "a": ["c", "d"],
    "b": ["d", "e"],
    "c": ["a", "e"],
    "d": ["a", "b"],
    "e": ["b", "c"],
}

print bfs("a", graph)

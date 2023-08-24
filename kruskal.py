class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

def kruskal(graph, num_vertices):
    min_spanning_tree = []
    graph.sort(key=lambda edge: edge[2])  # Sort edges by weight
    uf = UnionFind(num_vertices)

    for edge in graph:
        u, v, w = edge
        if uf.find(u) != uf.find(v):
            min_spanning_tree.append(edge)
            uf.union(u, v)

    return min_spanning_tree

# Example usage
graph = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

num_vertices = 5
min_spanning_tree = kruskal(graph, num_vertices)

print("Edges in the Minimum Spanning Tree:")
for u, v, w in min_spanning_tree:
    print(f"{u} - {v} : {w}")

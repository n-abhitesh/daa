import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # If the graph is undirected

    def prim(self):
        min_spanning_tree = []
        visited = [False] * self.V
        pq = [(0, 0)]  # Priority queue: (weight, vertex)

        while pq:
            weight, u = heapq.heappop(pq)

            if visited[u]:
                continue

            visited[u] = True

            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(pq, (w, v))
                    min_spanning_tree.append((u, v, w))

        self.print_min_spanning_tree(min_spanning_tree)

    def print_min_spanning_tree(self, min_spanning_tree):
        print("Edges in the Minimum Spanning Tree:")
        for u, v, w in min_spanning_tree:
            print(f"{u} - {v} : {w}")

# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

g.prim()

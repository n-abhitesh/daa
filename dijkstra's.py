import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # If the graph is undirected

    def dijkstra(self, src):
        distances = [float("inf")] * self.V
        distances[src] = 0
        pq = [(0, src)]  # Priority queue: (distance, vertex)

        while pq:
            dist_u, u = heapq.heappop(pq)

            if dist_u > distances[u]:
                continue

            for v, w in self.graph[u]:
                if distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    heapq.heappush(pq, (distances[v], v))

        self.print_distances(distances)

    def print_distances(self, distances):
        print("Vertex\tDistance from Source")
        for i in range(self.V):
            print(f"{i}\t{distances[i]}")

# Example usage
g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

src_vertex = 0
g.dijkstra(src_vertex)

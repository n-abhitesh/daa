INF = float("inf")

def floyd_warshall(graph):
    V = len(graph)
    dist = [[INF] * V for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0

    for u in range(V):
        for v, w in graph[u]:
            dist[u][v] = w

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
graph = [
    [(1, 3), (2, 6)],
    [(0, 3), (2, 2)],
    [(0, 6), (1, 2)]
]

shortest_distances = floyd_warshall(graph)

for row in shortest_distances:
    print(row)
